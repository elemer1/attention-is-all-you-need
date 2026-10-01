# 把论文当工程文本来读：原文核实底稿

> 对应第二乐章 2.5「标注版论文」，组件 ⑤。
> 原文引自 arXiv 1706.03762v7，均已核实 [V]。PDF 换行处断开的连字符已合并。
> 标签说明：
> - 「新东西」
> - 「调参」
> - 「事后解释」：论文给出猜测或启发式的理由
> - 「后来被改掉」

| 节 | 原文 | 标签 | 后来 |
|---|---|---|---|
| 摘要 | "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." | 新东西 | 减法式创新：拿掉了循环和卷积 |
| §3.2.1 | "We suspect that for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients." 脚注 4 用方差论证："their dot product … has mean 0 and variance d_k." | 事后解释 | 论文里少有的理论片段，用的动词是 "suspect" |
| §3.2.2 | "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions." | 新东西 | 由 Shazeer 提出 |
| §3.1 | "the output of each sub-layer is LayerNorm(x + Sublayer(x))" | 后来被改掉 | Xiong et al. 2020（arXiv 2002.04745）发现 Post-LN 输出层附近的梯度很大，所以需要 warmup，而 Pre-LN 不需要 warmup。tensor2tensor 早期的超参数是 Post-LN（`transformer_base_v1`），后来默认改成了 Pre-LN（v2）。LLaMA 2023 用的是 Pre-norm 加 RMSNorm。**不要声称论文里的 BLEU 结果是用 Pre-LN 跑出来的。** |
| §3.3 | 前馈网络 "consists of two linear transformations with a ReLU activation in between"，作用没有解释 | 事后解释（由后人补上） | Geva et al. 2021（arXiv 2012.14913）："Feed-forward layers constitute two-thirds of a transformer model's parameters, yet their role in the network remains under-explored … operate as key-value memories" |
| §3.5 | "we hypothesized it would allow the model to easily learn to attend by relative positions"；可学习的位置编码 "produced nearly identical results (see Table 3 row (E))"；选正弦是因为 "it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training" | 后来被改掉 | Press et al. 2022（ALiBi，arXiv 2108.12409）正文中说："sinusoidal position embeddings have very weak extrapolation abilities"。RoPE（arXiv 2104.09864）成为 LLaMA 的选择，但 RoPE 的外推也有局限 |
| §4 | 三条标准：每层计算量、可并行程度（最少的顺序操作数）、长距离依赖的路径长度 | 新东西 | 这是"为什么要拿掉循环"的论证 |
| §4 | "As side benefit, self-attention could yield more interpretable models." | 事后解释 | 后来发展成一整个可解释性领域，至今远未解决 |
| §5.3 | 学习率 = d_model^−0.5 · min(step^−0.5, step · warmup^−1.5)；"We used warmup_steps = 4000." | 调参 | Xiong 2020：warmup 是 Post-LN 不稳定的补丁 |
| §5.4 | "label smoothing of value ε_ls = 0.1 … This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score." | 调参 | 为了目标指标，接受另一个指标变差 |
| §6.1 | 平均最后 5 个检查点（大模型平均 20 个）；"beam size of 4 and length penalty α = 0.6 … These hyperparameters were chosen after experimentation on the development set." | 调参 | |
| §6.2 表 3 | "single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads"；"reducing the attention key size d_k hurts model quality … a more sophisticated compatibility function than dot product may be beneficial"；"dropout is very helpful in avoiding over-fitting" | 调参 | 消融表就是调试日志 |
| §6.3 | 英文句法分析："despite the lack of task-specific tuning our model performs surprisingly well" | 新东西 | 通用性的第一个迹象 |
| §7 | "We plan to extend the Transformer to problems involving input and output modalities other than text … images, audio and video. Making generation less sequential is another research goals of ours."（原文语法如此） | 用于 2.6 | 野心只放在翻译和多模态上，没有提到语言模型和对话 |
| §5.2 | 8 块 NVIDIA P100；base 模型 10 万步、12 小时；big 模型 30 万步、3.5 天 | — | |

## 配套读物
- *The Annotated Transformer*（Harvard NLP；Sasha Rush 2018 年原作，2022 年由 Huang 等人更新）：<https://nlp.seas.harvard.edu/annotated-transformer/>。注意它的代码用的是 Pre-LN："the norm is first as opposed to last"。
- Jay Alammar，*The Illustrated Transformer*（2018-06-27）：<https://jalammar.github.io/illustrated-transformer/>
- Raschka，"Why the original transformer figure…"（2023）：<https://magazine.sebastianraschka.com/p/why-the-original-transformer-figure>（[S]；所链接的提交只引入了可配置项，默认值仍是 Post-LN）
- LLaMA（arXiv 2302.13971）§2.2：列出了相对原始架构的改动，包括 Pre-norm 加 RMSNorm、SwiGLU 和 RoPE。
