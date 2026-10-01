"""A minimal Transformer encoder whose parts can be switched off one at a time.

Written from scratch (not torch.nn.Transformer) so that each ablation in
`ablations.py` changes exactly one thing:
  - pos:   sinusoidal positional encoding on/off            (paper §3.5)
  - scale: divide attention scores by sqrt(d_k) on/off       (paper §3.2.1)
  - norm:  "post" = LayerNorm(x + Sublayer(x)) as in §3.1, or "pre" = x + Sublayer(LayerNorm(x))
"""
import math
import torch
import torch.nn as nn
import torch.nn.functional as F


def sinusoid(n, d):
    pos = torch.arange(n).unsqueeze(1).float()
    i = torch.arange(0, d, 2).float()
    ang = pos / torch.pow(10000.0, i / d)
    pe = torch.zeros(n, d)
    pe[:, 0::2] = torch.sin(ang)
    pe[:, 1::2] = torch.cos(ang)
    return pe


class Attention(nn.Module):
    def __init__(self, d, heads, scale=True):
        super().__init__()
        self.h, self.dk, self.scale = heads, d // heads, scale
        self.qkv = nn.Linear(d, 3 * d)
        self.out = nn.Linear(d, d)
        self.last = None  # attention weights of the last forward pass

    def forward(self, x):
        B, T, D = x.shape
        q, k, v = self.qkv(x).view(B, T, 3, self.h, self.dk).permute(2, 0, 3, 1, 4)
        s = q @ k.transpose(-1, -2)
        if self.scale:
            s = s / math.sqrt(self.dk)
        a = s.softmax(-1)
        self.last = a.detach()
        y = (a @ v).transpose(1, 2).reshape(B, T, D)
        return self.out(y)


class Block(nn.Module):
    def __init__(self, d, heads, ff, scale, norm):
        super().__init__()
        self.att = Attention(d, heads, scale)
        self.ff = nn.Sequential(nn.Linear(d, ff), nn.ReLU(), nn.Linear(ff, d))
        self.n1, self.n2, self.norm = nn.LayerNorm(d), nn.LayerNorm(d), norm

    def forward(self, x):
        if self.norm == "post":
            x = self.n1(x + self.att(x))
            return self.n2(x + self.ff(x))
        x = x + self.att(self.n1(x))
        return x + self.ff(self.n2(x))


class Encoder(nn.Module):
    def __init__(self, vocab, n_out, d=64, heads=4, layers=2, ff=128, max_len=64,
                 pos=True, scale=True, norm="post"):
        super().__init__()
        self.emb = nn.Embedding(vocab, d)
        self.d, self.pos = d, pos
        self.register_buffer("pe", sinusoid(max_len, d))
        self.blocks = nn.ModuleList([Block(d, heads, ff, scale, norm) for _ in range(layers)])
        self.final = nn.LayerNorm(d) if norm == "pre" else nn.Identity()
        self.head = nn.Linear(d, n_out)

    def forward(self, x, read_at=None):
        h = self.emb(x) * math.sqrt(self.d)
        if self.pos:
            h = h + self.pe[: x.shape[1]]
        for b in self.blocks:
            h = b(h)
        h = self.final(h)
        # read_at: index of the position whose state is classified (a query slot)
        z = h.mean(1) if read_at is None else h[:, read_at]
        return self.head(z)
