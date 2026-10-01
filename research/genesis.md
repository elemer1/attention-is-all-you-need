# 生成史：《Attention Is All You Need》是怎么被造出来的

> 对应第二乐章 2.1–2.4、2.7，以及组件 ④「生成时间线」。
>
> 主要来源：
> - **[V-Levy]**：Steven Levy, "8 Google Employees Invented Modern AI. Here's the Inside Story", *Wired*, 2024-03-20。作者采访了全部八位作者，直接引语较多，属于强二手来源。
>   <https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/>
> - **[V]**：arXiv 1706.03762 各版本的 PDF。<https://arxiv.org/abs/1706.03762>
> - **[S]**：其他二手来源。FT 2023（Murgia）原文在付费墙后，只看到了转述。
> - **[NV]**：没能核实。

## 时间线

| 时间 | 事件 | 来源 |
|---|---|---|
| 约 2014 | Uszkoreit 开始构思他称为 self-attention 的做法 | [V-Levy] |
| 2016-06 | Parikh、Täckström、Das、Uszkoreit 发表 *Decomposable Attention*：不用循环，可以并行，不依赖词序，在 SNLI 上拿到 SOTA，参数少了近一个数量级。合作者随后转去把它用在搜索和广告上，没有继续推进 | [V] arXiv 1606.01933；[V-Levy] |
| 2016 某日 | Uszkoreit 和 Polosukhin 吃午饭。Polosukhin 回忆："He suggested, why not use self-attention?" 随后 Vaswani（Google Brain，1965 号楼）听说后加入 | [V-Levy] |
| 2016–17 | 三人写了一份设计文档，题为 **"Transformers: Iterative Self-Attention and Processing for Various Tasks"**，结尾画着六个变形金刚在山间发射激光 | [V-Levy] |
| 2017 年初 | Polosukhin 离开 Google，与人联合创办 NEAR | [V-Levy] |
| 2017 某日 | 团队卡在瓶颈上，效果和 LSTM 差不多但没有更好。Shazeer 走过 1965 号楼 Kaiser 工位旁边的走廊，听到了他们的讨论，随后自己重写了一版代码。Gomez 说："That kicked off a sprint." | [V-Levy]；月份 [NV] |
| 截稿前两周 | "frantic"。大家挤在 1965 号楼，因为那里的咖啡机更好；Gomez 说 "People weren't sleeping" | [V-Levy] |
| 截稿前几晚 | Jones 想出了标题："It literally took five seconds of thought. I didn't think they would use it." | [V-Levy] |
| 2017-05-19 | NIPS 截稿。英法翻译的结果是在提交前约五分钟才出来的，提交时只剩约两分钟 | [V-Levy] |
| 2017-06-12 | arXiv v1 | [V] |
| 2017-08-31 | Uszkoreit 在 Google Research 博客发文介绍 Transformer | [V] |
| 2017-12-06 | NIPS 海报展示："Security had to tell us to leave."（Uszkoreit）同一天提交 v5（camera-ready 版本），**详细的贡献脚注是这一版才加上的** | [V-Levy]；[V] |
| 2018 | Google 把它用进翻译，发布 BERT；OpenAI 发布 GPT-1（2018-06-11） | [V-Levy]；[V] |

## 人物与分工

**贡献脚注全文**（v5 起；v1–v4 只有 "Equal contribution. Listing order is random."）[V]：

> Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research.

脚注之外的人物细节（均来自 [V-Levy]，另有标注的除外）：

- **Jakob Uszkoreit**
  - 提出这个想法，"Transformer"这个名字从第一天就是他定的。
  - 理由有两个：这个机制会转换信息；另外，"I had two little Transformer toys as a very young kid."
  - 同事的反应是："People raised their eyebrows, because it dumped out all the existing neural architectures."
  - 他的父亲 Hans Uszkoreit 是著名的计算语言学家（1968 年因抗议入侵捷克在东德坐牢 15 个月）。两人在餐桌上讨论时 "weren't necessarily seeing eye to eye"。**父亲是怀疑者，不是这个想法的来源。**
- **Illia Polosukhin**：和 Vaswani 一起做出了第一批模型。论文提交前已经离开 Google。用电影《降临》（Arrival）里的外星语言作类比，这一点只有 FT 的转述 [S]，Levy 没有提到；不能写成"《降临》是想法的来源"。
- **Ashish Vaswani**：参与了每一个环节。截稿前一晚睡在办公室沙发上，盯着窗帘上像突触一样的花纹，对 Gomez 说这项工作的意义会远远超出翻译。
- **Noam Shazeer**：提出 scaled dot-product attention、multi-head attention 和无参数的位置编码。他说的是："I took the basic idea and made the thing up myself… 'Look, it works.'" Jones 的评价是 "Noam is a wizard."
- **Niki Parmar**：USC 硕士毕业，做了"无数"的模型变体。"The English-French numbers came, like, five minutes before we submitted… I was sitting in the micro-kitchen in 1965."
- **Llion Jones**：威尔士人，主管是 Polosukhin；最初的代码库、推理加速和可视化由他负责。标题是他起的。
- **Łukasz Kaiser**：波兰出生的理论计算机科学家，带着 Gomez 做 tensor2tensor。
- **Aidan Gomez**：多伦多大学本科生，Hinton 实验室出身，在 Kaiser 手下实习。这个实习本来只招博士生。

## 名字与标题
- 设计文档的标题："Transformers: Iterative Self-Attention and Processing for Various Tasks"。论文草稿第一句是 "We are awesome."[V-Levy]
- 还有一个备选名叫 "CargoNet"（Convolution、Attention、Recognition、Google 的缩写），被投票认为 "horrible"。这是 Shazeer 在 GTC 2024 座谈上说的。[S]
- 标题来自披头士的 "All You Need Is Love"，是 Jones 起的。
- 作者顺序：Levy 说他们有意 "sabotage" 通常的排序惯例。早期草稿里 Shazeer 排第一，他本人也很意外。[V-Levy]

## 结果（工程上的事实）
- WMT14 英德翻译 28.4 BLEU，比此前最好结果（包括集成模型）高出 2 BLEU 以上。[V]
- 英法翻译：**v1–v4 是 41.0，v5 起改为 41.8**。在 8 块 GPU 上训练 3.5 天；正文写明是 P100，base 模型训练 12 小时就达到了新的 SOTA。[V]
- 审稿意见，据 Parmar 回忆："One was positive, one was extremely positive, and one was, 'This is OK.'"[V-Levy]

## 发表之后
- Google 高层当时把它看作 "just another interesting AI project"，上级很少过问进展；公司申请了临时专利。Uszkoreit 后来问："why didn't we do anything with the fact that we had seen it?"[V-Levy]
- 作者去向：

  | 作者 | 去向 | 来源 |
  |---|---|---|
  | Polosukhin | 2017 年初去 NEAR | [V-Levy] |
  | Gomez | 实习结束后，2019 年联合创办 Cohere | [V-Levy / S] |
  | Shazeer | 2021-10 创办 Character.AI；2024-08 回到 Google；2026-06-18 宣布加入 OpenAI | [V-Levy]；[S] |
  | Vaswani、Parmar | 2021 年底创办 Adept，后来创办 Essential AI；Parmar 2024-12 加入 Anthropic | [S] |
  | Uszkoreit | 2021 年去 Inceptive（柏林） | [S]；月份 [NV] |
  | Kaiser | 2021 年加入 OpenAI，是唯一没有创业的作者 | [V-Levy]；月份 [NV] |
  | Jones | 2023 年 7–8 月和 David Ha 在东京创办 Sakana AI | [S] |

  **写作注意**："八位作者全部离开了 Google"必须注明时间点（2023 年下半年起成立）。Shazeer 2024 年曾经回去过。

## 他们自己看清了吗？（对应 2.7，结论要比原来的计划更细）
- **看到了一部分。** Uszkoreit："we understood that this was potentially quite a big deal." Vaswani："I had a strong hunch we were onto something more general."[V-Levy]
- **但没有看到全部。**
  - Shazeer 开玩笑说，早知道会这样，他"might have worried more about the author order"。
  - Jones："I have people asking me for selfies—because I'm on a paper!"
  - 带 Jones 接触 self-attention 的 Mat Kelcey 称之为 "the biggest incorrect prediction of my life"。
  - Altman："I don't think anyone at Google realized what it meant."[V-Levy]
- GTC 2024 座谈上，Gomez 说："the world needs something better than Transformers."[S]
  <https://venturebeat.com/ai/attention-is-all-you-need-creators-look-beyond-transformers-at-nvidia-gtc-the-world-needs-something-better>
- 结论：作者们有预感，觉得这东西可能"很大"，但没有一个人预见到它的规模。论文本身的目标只是翻译，结论部分写得很克制。

## 对"生成过程"分析（2.4）有用的材料
- **减法**："dumped out all the existing neural architectures"。
- **长期的直觉**：从约 2014 年开始，2016 年有一个小规模验证（*Decomposable Attention*），2017 年爆发。
- **偶遇**：2016 年的一次午饭，2017 年的一次走廊路过。
- **怀疑**：同事挑眉，父亲不同意。
- **工程魔法**：Shazeer 重写代码之后，结果突破了瓶颈。
- **截稿压力**：最后两周，最后五分钟才出来的结果。
- **组合**：tensor2tensor、残差连接、LayerNorm、注意力机制。
- **玩笑**：草稿第一句 "We are awesome"、变形金刚漫画、五秒钟想出来的标题。

## 未核实 [NV]
- 截稿的具体时刻和时区。
- Shazeer 加入的月份。
- Polosukhin 离开的确切月份。
- FT 原文对《降临》的具体措辞。
