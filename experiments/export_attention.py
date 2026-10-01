"""Export real attention weights from BERT-base (uncased) for the page's attention game.

BERT (2018) is a Transformer encoder, the half of the 2017 architecture that reads
the whole sentence in both directions. Weights come straight from the model;
nothing is smoothed or hand-edited. Each weight is stored as an integer 0-1000
(weight x 1000, rounded).

Usage:  python export_attention.py        -> ../site/data/attention.json
"""
import json
from pathlib import Path

import torch
from transformers import BertModel, BertTokenizer

NAME = "google-bert/bert-base-uncased"
SENTENCES = [
    ("tired", "The animal didn't cross the street because it was too tired."),
    ("wide", "The animal didn't cross the street because it was too wide."),
    ("dogman", "The dog bit the man."),
    ("mandog", "The man bit the dog."),
]


def main():
    tok = BertTokenizer.from_pretrained(NAME)
    model = BertModel.from_pretrained(NAME, attn_implementation="eager").eval()
    out = {"model": NAME, "layers": 12, "heads": 12, "scale": 1000, "sentences": []}
    with torch.no_grad():
        for key, text in SENTENCES:
            enc = tok(text, return_tensors="pt")
            att = model(**enc, output_attentions=True).attentions  # 12 x (1,12,T,T)
            a = torch.stack([x[0] for x in att])  # L,H,T,T
            toks = tok.convert_ids_to_tokens(enc["input_ids"][0])
            out["sentences"].append({
                "key": key, "text": text, "tokens": toks,
                "att": (a * 1000).round().int().tolist(),
            })

    # Find, without hand-picking, the head that best tells the two "it" sentences apart:
    # in "tired" it should look at "animal", in "wide" at "street".
    s = {x["key"]: x for x in out["sentences"]}
    t, w = s["tired"], s["wide"]
    it_t, an_t, st_t = t["tokens"].index("it"), t["tokens"].index("animal"), t["tokens"].index("street")
    it_w, an_w, st_w = w["tokens"].index("it"), w["tokens"].index("animal"), w["tokens"].index("street")
    best = None
    for L in range(12):
        for H in range(12):
            at, aw = t["att"][L][H][it_t], w["att"][L][H][it_w]
            score = (at[an_t] - at[st_t]) + (aw[st_w] - aw[an_w])
            if best is None or score > best[0]:
                best = (score, L, H, at[an_t], at[st_t], aw[an_w], aw[st_w])
    out["it_head"] = {"layer": best[1] + 1, "head": best[2] + 1,
                      "tired_animal": best[3], "tired_street": best[4],
                      "wide_animal": best[5], "wide_street": best[6],
                      "searched": "all 144 heads; score = (tired: animal - street) + (wide: street - animal)"}
    dst = Path(__file__).resolve().parent.parent / "site" / "data" / "attention.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    print("wrote", dst, dst.stat().st_size // 1024, "KB; it-head:", out["it_head"])


if __name__ == "__main__":
    main()
