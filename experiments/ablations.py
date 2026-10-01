"""Three small ablations of the 2017 Transformer, run on CPU.

  A. pos   — "who bit whom": [X, 咬, Y] -> X.  With vs without positional encoding.
  B. scale — key-value lookup, 8 pairs, one wide head (d_k = 256). With vs without 1/sqrt(d_k).
  C. norm  — 12 layers, learning rate 3e-3: Post-LN without warmup,
             Post-LN with warmup, Pre-LN without warmup.

Every run is seeded (seeds 0, 1, 2). Results go to ../site/data/ablations.json,
which the page inlines. Usage:  python ablations.py [--quick]
"""
import json
import math
import random
import sys
import time
from pathlib import Path

import torch
import torch.nn.functional as F

from tiny import Encoder

QUICK = "--quick" in sys.argv
SEEDS = [0, 1, 2]
torch.set_num_threads(4)


def seed_all(s):
    random.seed(s)
    torch.manual_seed(s)


# ---------------------------------------------------------------- A. who bit whom
NOUNS = ["狗", "人", "猫", "马", "牛", "羊", "鸡", "鸭", "猪", "狼", "虎", "熊", "鹰", "蛇", "鼠", "兔"]
BITE = len(NOUNS)  # token id of 咬


def exp_pos():
    # Every ordered pair is both trained and tested: "狗咬人" and "人咬狗" both appear,
    # with opposite answers. Without word order the two are the same bag of tokens.
    pairs = [(a, b) for a in range(len(NOUNS)) for b in range(len(NOUNS)) if a != b]
    train = test = pairs
    xt = torch.tensor([[a, BITE, b] for a, b in test])
    yt = torch.tensor([a for a, _ in test])
    steps = 150 if QUICK else 600
    out = {}
    for pos in (True, False):
        runs = []
        for s in SEEDS:
            seed_all(s)
            m = Encoder(len(NOUNS) + 1, len(NOUNS), d=64, heads=4, layers=2, pos=pos, norm="pre")
            opt = torch.optim.Adam(m.parameters(), lr=1e-3)
            curve = []
            for step in range(steps + 1):
                if step % 25 == 0:
                    with torch.no_grad():
                        acc = (m(xt).argmax(-1) == yt).float().mean().item()
                    curve.append([step, round(acc, 4)])
                if step == steps:
                    break
                batch = [train[random.randrange(len(train))] for _ in range(128)]
                x = torch.tensor([[a, BITE, b] for a, b in batch])
                y = torch.tensor([a for a, _ in batch])
                loss = F.cross_entropy(m(x), y)
                opt.zero_grad(); loss.backward(); opt.step()
            runs.append(curve)
        out["with" if pos else "without"] = runs
    return {"task": "who-bit-whom", "nouns": NOUNS, "pairs": len(pairs),
            "steps": steps, "runs": out}


# ---------------------------------------------------------------- B/C. key-value lookup
NK = NV = 16
KV_VOCAB = NK * NV + NK  # pair tokens, then one query token per key


def kv_batch(n, pairs):
    """Each (key, value) pair is a single token k*NV+v; the last token asks for key q.
    The model must attend from the query to the one pair token with the same key."""
    xs, ys = [], []
    for _ in range(n):
        keys = random.sample(range(NK), pairs)
        vals = [random.randrange(NV) for _ in keys]
        q = random.randrange(pairs)
        xs.append([k * NV + v for k, v in zip(keys, vals)] + [NK * NV + keys[q]])
        ys.append(vals[q])
    return torch.tensor(xs), torch.tensor(ys)


def train_kv(m, steps, lr, pairs, warmup=0, eval_every=25):
    opt = torch.optim.Adam(m.parameters(), lr=lr, betas=(0.9, 0.98), eps=1e-9)
    xe, ye = kv_batch(512, pairs)
    curve = []
    for step in range(steps + 1):
        if step % eval_every == 0:
            with torch.no_grad():
                lo = m(xe, read_at=-1)
                acc = (lo.argmax(-1) == ye).float().mean().item()
                l = F.cross_entropy(lo, ye).item()
            curve.append([step, round(acc, 4), round(l if math.isfinite(l) else 99.0, 4)])
        if step == steps:
            break
        f = min(1.0, (step + 1) / warmup) if warmup else 1.0
        for g in opt.param_groups:
            g["lr"] = lr * f
        x, y = kv_batch(64, pairs)
        loss = F.cross_entropy(m(x, read_at=-1), y)
        opt.zero_grad(); loss.backward(); opt.step()
    return curve


def attn_peak(m, pairs):
    """mean of the largest attention weight per query row, first layer, at the current weights"""
    x, _ = kv_batch(256, pairs)
    with torch.no_grad():
        m(x, read_at=-1)
    a = m.blocks[0].att.last  # B,H,T,T
    return round(a.max(-1).values.mean().item(), 4)


def exp_scale():
    pairs, steps = 8, (300 if QUICK else 1500)
    out, peaks = {}, {}
    for scale in (True, False):
        runs, pk = [], []
        for s in SEEDS:
            seed_all(s)
            m = Encoder(KV_VOCAB, NV, d=256, heads=1, layers=2, ff=256, pos=True, scale=scale, norm="pre")
            pk.append(attn_peak(m, pairs))
            runs.append(train_kv(m, steps, 5e-4, pairs))
        key = "with" if scale else "without"
        out[key], peaks[key] = runs, pk
    return {"task": "key-value lookup", "pairs": pairs, "d_k": 256, "steps": steps,
            "runs": out, "init_attention_peak": peaks}


def exp_norm():
    pairs, steps, lr = 8, (300 if QUICK else 1500), 3e-3
    conds = [("post", 0, "post_nowarm"), ("post", 400, "post_warm"), ("pre", 0, "pre_nowarm")]
    out = {}
    for norm, warm, key in conds:
        runs = []
        for s in SEEDS:
            seed_all(s)
            m = Encoder(KV_VOCAB, NV, d=128, heads=4, layers=12, ff=256, pos=True, scale=True, norm=norm)
            runs.append(train_kv(m, steps, lr, pairs, warmup=warm))
        out[key] = runs
    return {"task": "key-value lookup", "pairs": pairs, "layers": 12, "lr": lr, "warmup": 400,
            "steps": steps, "runs": out}


if __name__ == "__main__":
    t0 = time.time()
    res = {"generated_by": "experiments/ablations.py", "seeds": SEEDS, "torch": torch.__version__}
    for name, fn in (("pos", exp_pos), ("scale", exp_scale), ("norm", exp_norm)):
        t = time.time()
        res[name] = fn()
        print(f"{name}: {time.time() - t:.0f}s", flush=True)
    dst = Path(__file__).resolve().parent.parent / "site" / "data" / "ablations.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(res, ensure_ascii=False, separators=(",", ":")))
    print("wrote", dst, f"in {time.time() - t0:.0f}s")
