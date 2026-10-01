# 历史案例库：叠加 vs 重组

> 第四乐章「处境与行动」的论证底稿。
> 每个案例按同一结构整理：**新技术出现 → 多数人"叠加" → 少数人"重组" → 收益滞后 → 谁赢谁输**。
>
> 证据标记：
> - **[V]** 已对照一手来源或权威来源核实；
> - **[S]** 只有二手来源（媒体、百科、博客）；
> - **[NV]** 未能核实，不进正文。
>
> 规划阶段（2026-10）由研究 agent 查证。正式写进正文前，每条再点开出处复核一次。

---

## 0. 主案例：互联网

### 诞生
- 1969-10-29 约 22:30，UCLA Kleinrock 实验室的学生 Charley Kline 向 SRI 发出第一条消息。本来要输入 "LOGIN"，只传到 "LO" 系统就崩溃了；大约一小时后才完整登录成功。[S]
  <https://www.lk.cs.ucla.edu/internet_first_words.html> · <https://samueli.ucla.edu/internet50-press/>
- 1974 年 5 月，Cerf 和 Kahn 发表 "A Protocol for Packet Network Intercommunication"（*IEEE Trans. Comm.* COM-22(5): 637–648）。TCP 和 IP 到 1978 年前后才拆成两层。[S]
  <https://ethw.org/Milestones:Transmission_Control_Protocol_(TCP)_Enables_the_Internet,_1974>
- 1983-01-01 "flag day"：ARPANET 从 NCP 整体切换到 TCP/IP，依据是 Postel 的 RFC 801。[S]
  <https://www.theregister.com/2013/01/03/operational_internet_anniversary/>
- 1989 年 3 月，Berners-Lee 提交 "Information Management: A Proposal"，上司 Mike Sendall 在上面批了 "Vague but exciting"。[V]
  <https://info.cern.ch/Proposal.html> · <https://www.cnbc.com/2019/03/12/feedback-world-wide-web-inventor-berners-lee-got-from-boss-on-the-idea.html>
- **1993-04-30，CERN 把 Web 软件放进公有领域**，包括行模式浏览器、基础服务器和公共代码库。到 1993 年底已知的 Web 服务器超过 500 台，Web 约占互联网流量的 1%。[V]
  <https://home.cern/science/computing/birth-web/licensing-web>
  → 这一步可以和 Transformer 以公开论文加开源代码（tensor2tensor）发布对照：两者是同一种扩散路径。
- 商业化的过程：
  - 1990 年 6 月以前，NSFNET 只允许"支持科研与学术"的用途；
  - 1991 年 ANS CO+RE 开始承载商业流量；
  - 1992 年 Boucher 修正案允许 NSFNET 上走商业流量；
  - 1995-04-30 NSFNET 退役。[S]
  <https://en.wikipedia.org/wiki/National_Science_Foundation_Network>
- 1995-08-09 Netscape 上市：发行价 28 美元，因为需求太大推迟了近两小时才开盘，开盘价 71 美元，收盘 58.25 美元。这家成立 16 个月、还没有盈利的公司估值约 29 亿美元。[S]
  <https://www.fool.com/investing/general/2013/08/09/the-ipo-that-inflated-the-dot-com-bubble.aspx>

### 扩散
- 美国成年人上网比例（Pew）：1995 年 14%，2000 年 52%，2005 年 68%，2010 年 76%。[S]
  注意：1995 年的数据来自早期的 Times Mirror/Pew 调查，和 2000 年以后的序列不能严格比较。
  <https://www.pewresearch.org/internet/2015/06/26/americans-internet-access-2000-2015/>
- 美国家庭上网比例（人口普查局 CPS）：1997 年 18.0%，1998 年 12 月 26.2%，2000 年 8 月 41.5%，2011 年 71.7%。[S]
  <https://www.census.gov/content/dam/Census/library/publications/2013/demo/p20-569.pdf>
- 全球（ITU）：2019 年上网人数约 41 亿，"略超 53%"。[S]
  <https://www.itu.int/en/ITU-D/Statistics/Documents/facts/FactsFigures2019.pdf>
- 滞后（自算）：
  - ARPANET 1969 → 美国成年人过半 2000，约 31 年；
  - Web 提案 1989 → 美国成年人过半 2000，约 11 年；
  - ARPANET 1969 → 全球过半 2019，约 50 年。

### 生产率
- Oliner & Sichel（*JEP* 14(4), 2000）：美国劳动生产率增长 1995–2000 年为 2.5%/年，1972–95 年为 1.4%/年；加速的约三分之二来自 IT。[V]
  <https://www.aeaweb.org/articles?id=10.1257%2Fjep.14.4.3>
- Byrne, Oliner & Sichel（Fed FEDS 2013-36），非农商业部门：[V]

  | 时段 | 劳动生产率年增长 | IT 贡献 |
  |---|---|---|
  | 1974–95 | 1.56% | 0.77 个百分点 |
  | 1995–2004 | 3.06% | 1.50 个百分点 |
  | 2004–12 | 1.56% | 0.64 个百分点 |

  <https://www.federalreserve.gov/pubs/feds/2013/201336/index.html>
- 反方：Gordon（*JEP* 14(4): 49–74, 2000）"Does the 'New Economy' Measure Up to the Great Inventions of the Past?" 持怀疑立场。[V，仅核实了引文]

### 读到信号并重组：微软
- 1995-05-26，Gates 写给高管的备忘录 "The Internet Tidal Wave"。[S，来源是转录；原件是司法部诉讼的证物]
  <https://www.cnbc.com/2020/05/26/how-bill-gates-described-the-internet-tidal-wave-in-1995.html>
  - "Now I assign the Internet the highest level of importance."
  - "The Internet is the most important single development to come along since the IBM PC was introduced in 1981."
  - "The Internet is a tidal wave. It changes the rules. It is an incredible opportunity as well as incredible challenge."
  - "A new competitor 'born' on the Internet is Netscape. Their browser is dominant, with 70% usage share…"
  - 意义：在位者晚了一步，但还来得及读到信号并重组。可以和第 12 条的 Google 对照。

### 失败的在位者
- **百视达**：2000 年，Hastings 和 Randolph 在达拉斯以约 5000 万美元向 CEO Antioco 出售 Netflix，被拒。百视达 2010 年 9 月申请破产。[S]
  <https://fortune.com/2023/04/14/netflix-cofounder-marc-randolph-recalls-blockbuster-rejecting-chance-to-buy-it>
  - **神话**："被当场笑出门"。Randolph 的原话是对方在 "struggling not to laugh"，Hastings 也说哄笑的场面是他事后想象出来的。
- **Borders**：2001–2008 年把网上销售外包给亚马逊；破产时网上收入只占约 3%；2011 年 7 月清算，关闭 399 家门店，约 10,700 人失业。[S]
  <https://www.npr.org/sections/thetwo-way/2011/07/18/138491830/headed-for-liquidation-borders-will-close-its-doors>
  - 反方：Slate 认为它主要败在自身管理。<https://slate.com/business/2011/07/borders-bankruptcy-done-in-by-its-own-stupidity-not-the-internet.html>
- **报纸**：分类广告收入 2000 年达到峰值 196 亿美元，约占总收入三分之一；2012 年降到 46 亿，2018 年约 22 亿。[S]
  <http://www.minnpost.com/business/2014/02/how-craigslist-killed-newspapers-golden-goose/> · CRS R47018
- **《大英百科全书》**：2012-03-13 宣布停印纸质版，结束 244 年的历史（首版 1768 年）；当时它的主要业务已经在线上运营了近 20 年。[V]
  <https://www.businesswire.com/news/home/20120314005227/en/Encyclopaedia-Britannica-Print-Edition-Completely-Digital>

### 重组者
- 1994 年 Bezos 创立亚马逊。他后来回忆当时的想法："I knew that if I failed I wouldn't regret that, but I knew the one thing I might regret is not ever having tried."（Academy of Achievement 访谈，2001）[S]
- 最大的回报来得很晚：Facebook 2004 年，iPhone 2007 年带来移动互联网，都在 1995 年热潮之后 10–15 年。[待查日期，属常识级]

### 行动 ≠ 投资（4.4 的核心例证）
- 纳斯达克：2000-03-10 收盘 5,048.62（盘中最高 5,132.52）；2002-10-09 跌到 1,114.11，约 −78%；**2015-04-23 才再创收盘新高（5,056.06），用了 15 年。**[V]
  <https://www.npr.org/sections/thetwo-way/2015/04/23/397113284/15-years-after-the-dot-com-bust-nasdaq-closes-at-new-record>
- 亚马逊股价：1999 年 12 月约 106.69 美元，2001-09-28 跌到 5.97 美元，约 −94%；公司活了下来。[S]
- Webvan：IPO 募资 3.75 亿美元，累计用掉约 12 亿美元资本、亏损超过 8 亿，2001 年 7 月关闭。Pets.com：2000 年 2 月 IPO 募资 8,250 万美元，2000 年 11 月清算，只活了 268 天。[S]
  后来 Instacart 和 DoorDash 证明了这个方向。[待查]
- 思科：2000 年 3 月市值约 5,550 亿美元，一度全球第一；2000-03-27 股价约 80 美元，此后再没回到这个高点。[S；发布前要查当日股价]
  <https://www.fool.com/investing/2016/09/23/cisco-stock-history-what-investors-need-to-know.aspx>

### 教育
- 2007 年 1 月，Middlebury College 历史系一致投票，禁止学生在论文和考试里引用 Wikipedia。系主任 Don Wyatt 说："Even though Wikipedia may have some value… it is not itself an appropriate source for citation."[V]
  <https://www.insidehighered.com/news/2007/01/26/stand-against-wikipedia>
- 2012-11-02，《纽约时报》Pappano 的文章 "The Year of the MOOC"。2019 年 1 月 Reich & Ruipérez-Valiente 在 *Science* 发表 "The MOOC Pivot"：分析了 565 门 MIT/Harvard 的 edX 课程、1,267 万注册，发现多数学习者第一年之后不再回来，完课率六年间没有改善。[S]
  <https://www.insidehighered.com/digital-learning/article/2019/01/16/study-offers-data-show-moocs-didnt-achieve-their-goals>
  - 寓意：把新技术叠加在旧教育形式上，效果远小于宣传。

---

## A. 动力：叠加 vs 重组

### 1. 电力：Paul David（1990）
"The Dynamo and the Computer", *AER* 80(2): 355–361。[V]
<https://gwern.net/doc/economics/automation/1990-david.pdf>

- 1899 年，美国电动机占工厂机械动力的 "less than 5 percent"；又过了 "another two decades, roughly speaking" 才到 50%。同年只有 3% 的住宅有电灯（城市住宅是 8%）。
- 电力对制造业生产率的影响直到 1920 年代初才出现，"four decades after the first central power station opened for business"。
- 1919–29 年美国制造业 TFP 增速加快约 5 个百分点（和 1909–19 年相比），其中 "approximately half" 在统计上可以归因于二级电动机容量的增长。
- 拖延的原因：替换"仍可使用的厂房"不划算。率先新建电气化工厂的是快速增长的行业：烟草、金属制品、运输设备、电机。
- 关键句："This sort of overlaying of one technical system upon a preexisting stratum is not unusual during historical transitions."
- 单机驱动带来的好处：
  - 去掉沉重的天轴后，建筑可以更轻；
  - 可以盖单层厂房；
  - 物料搬运变好，机器可以重新排列；
  - 维修不必全厂停工；
  - 可以开天窗，皮带事故减少。

### 2. 从传动轴到电线：Devine（1983）
*J. Econ. Hist.* 43(2): 347–372。[S，摘要和转引]

- 四个阶段：
  - 直接驱动：蒸汽机或水轮带动天轴；
  - 电动天轴：电动机替换蒸汽机，其余照旧；
  - 成组驱动：一台电动机带一组机器；
  - 单机驱动：每台机器一台电动机。
  第二、三阶段是 "short-lived intermediate stages"。
- 天轴 "rotated continuously… no matter how many machines were actually being used. If a line shaft or the steam engine broke down, production ceased in a whole room of machines or even in the entire factory."（转引自 Jovanovic & Rousseau，NBER w8676）
- 电力占机械动力的比例：约 1909 年 21%，1919 年 50%，1929 年 75%。[S，原表未见]
- Columbia Mills（南卡罗来纳，1894-04-15 投产）：第一座完全用电的纺织厂，装了 17 台 65 马力的 GE 感应电动机。[S]
- Damron（2025，*Explorations in Economic History* 96）：用北卡罗来纳 1905–26 年的工厂数据，发现电气化提高了生产率；延迟则 "point to the importance of complementary innovations"。[S]
- **[NV]** 没有找到哪家具体工厂"只把蒸汽机换成一台大电机、收益甚微"的案例，正文只能作为一般模式来写。

### 3. 福特 Highland Park
- 1910 年投产，Albert Kahn 设计。1913-10-07 启用移动底盘装配线，每辆车的装配时间从 12.5 小时（728 分钟）降到 93 分钟。1914-01-05 宣布 5 美元日薪，此前是 2.34 美元，工时从 9 小时降到 8 小时。[S]
  <https://askus.thehenryford.org/K12/faq/433848>
- **注意**：这座厂有自己的发电站，冲压机仍由天轴带动，并不是纯粹的单机驱动。正文只能说"电力使按工序流动的布局成为可能"。
- Model T 价格要带年份：常见的"850→260 美元"指 1908 年到 1920 年代中期，260 美元是最简配的 runabout。

### 4. Insull：商业模式的重组
[S] <https://en.wikipedia.org/wiki/Samuel_Insull> · Hughes, *Networks of Power* (1983)

- 1892 年离开 GE，执掌 Chicago Edison。1894 年建成 Harrison Street 电站（6,400 kW），当时全美最大。
- 1894 年在英国 Brighton 见到 Arthur Wright 的需量电表，这种电表能记下每个用户的最大负荷。之后他追求负荷率，把电车、工业、住宅的用电混在一起，并实行分类定价。
- 1898 年任 NELA 会长时推动州政府监管，换取自然垄断地位。1907 年成立 Commonwealth Edison，1920 年约有 50 万用户。
- 反面：他用 2,700 万美元股本控制了 5 亿美元资产，1932 年崩塌；1935 年《公用事业控股公司法》出台。

### 5. 蒸汽：Crafts（2004）
*Economic Journal* 114(495): 338–351。[V]

- "steam contributed little to growth before 1830 and had its peak impact about a hundred years after Watt's famous invention. Only with the advent of high-pressure steam after 1850 did the technology realise its potential."
- 蒸汽对英国劳动生产率增长的年贡献：

  | 时段 | 年贡献 |
  |---|---|
  | 1760–1800 | 0.01% |
  | 1800–30 | 0.02% |
  | 1830–50 | 0.20% |
  | 1850–70 | 0.41% |
  | 1870–1910 | 0.31% |

- 1830 年蒸汽和水力各约 16.5 万马力才持平；美国到 1860 年代蒸汽才超过水力。汽船在 1850 年以前的贡献 "entirely trivial"。

### 6. Arkwright 的 Cromford（1771）
[S]

- 1772 年起实行两班倒，每班 12 小时；起初有约 200 名工人，以妇女儿童为主，最小的 7 岁；厂方为工人建了住房。
- "The gate… was shut at precisely 6 am and 6 pm… any worker who failed to get through it not only lost a day's pay but also was fined another day's pay."
- 寓意：工厂制度本身就是一项组织发明。

---

## B. 信息与物流

### 7. 印刷术
- **Dittmar（2011，QJE 126(3): 1133–72）**[V] <https://people.bu.edu/chamley/764-23/Dittmar.pdf>
  - "Between 1500 and 1600, European cities where printing presses were established in the 1400s grew 60% faster than otherwise similar cities."
  - 印刷 "accounted for at least 18% and as much as 68% of European city growth between 1500 and 1600"。
  - 1450–1500 年间书价降了三分之二。
  - 机制：印刷的商人手册，内容是商业算术和簿记。
  - 原话："no evidence of the technology's impact in measures of aggregate productivity or per capita income — much as, until the mid-1990s, they found no evidence of productivity gains associated with computer-based information technologies."
- **Rubin（2014，REStat 96(2): 270–86）**：1500 年前有印刷所的城市 "were at minimum 29 percentage points more likely to be Protestant by 1600"。[V]
- **威尼斯**：1469–1500 年约 200 家印刷商出了约 3,800 种版本，占全部约 28,000 种摇篮本（1501 年以前印刷的书）的 10% 以上。[S]
- **Aldus Manutius**：1501 年的维吉尔是他的第一本八开本，也是第一本全书用斜体印刷的书（字模由 Griffo 刻制），把便宜、便携的开本用到了古典文学上。[S]
- **路德**：1518–23 年德意志出版物中 "a third bore Luther's name"（Edwards 1994）。1500–30 年约 1 万种小册子版本中，路德约占 20%。[S]

### 8. 计算机生产率悖论
- **Solow**："You can see the computer age everywhere but in the productivity statistics." 出处：*NYT Book Review*，1987-07-12，p.36。这是一篇书评，不是论文。[V/S]
  <https://standupeconomist.com/solows-computer-age-quote-a-definitive-citation/>
- **Bresnahan, Brynjolfsson & Hitt（2002，QJE 117(1)）**：IT、工作组织重组和新产品三者是互补的。[V]
- **Brynjolfsson, Rock & Syverson（2021，AEJ: Macro 13(1)）**：[V] <https://www.aeaweb.org/articles?id=10.1257/mac.20180386>
  - "General purpose technologies (GPTs) like AI enable and require significant complementary investments"；
  - 生产率呈 J 曲线：早期被低估，后期被高估；
  - 到 2017 年底，TFP 比官方数字高 15.9%。

### 9. 沃尔玛
- 1983 年用条形码扫描，1987 年建成卫星网络，1991 年推出 Retail Link。[S]
- MGI 2001：在综合百货这一块，"Wal-Mart directly and indirectly caused the bulk of the productivity acceleration through ongoing managerial innovation"。Solow："By far the most important factor in that is Wal-Mart."[S]
  - 功劳在管理，不在 IT 支出本身。
- **[NV]** 越库作业"80%"之类的数字，不用。

### 10. 电子表格
- VisiCalc 1979 年售价 99 美元。据 NPR（2015-02-27），1980 年以来 "400,000 bookkeeping and accounting clerk jobs have gone away… 600,000 accounting jobs have been added"。[S；引用 NPR，不要写成 BLS]
  <https://www.npr.org/2015/02/27/389585340/how-the-electronic-spreadsheet-revolutionized-business>

### 11. 集装箱
- 1956-04-26，Ideal X 载 58 个 35 英尺集装箱从 Port Newark 开往休斯顿。装卸成本从每吨约 5.83 美元降到 0.16 美元以下（Levinson 引用的 McLean 估算）。[S]
- 赢家和输家：
  - 曼哈顿和布鲁克林码头输给了 Newark/Elizabeth；
  - 纽约码头工人从 1950 年代初约 3.5 万人降到 1976 年不足 1 万；
  - 奥克兰崛起，旧金山衰落；伦敦码头衰落。[S]
- Bernhofen, El-Sahli & Kneller（2016，JIE 98）：[V]
  - 1966–83 年间全球扩散；
  - 对产品层面贸易的影响 "occur 10-15 years after containerization"；
  - 自由贸易协定的当期效应只有集装箱化的约三分之一；
  - **保守口径**：产品层面的估计是 17.4%（北北贸易）和 14.1%（全球）。
- **不用**："700%"和"1300%"。

---

## C. 握着信号却没行动的在位者

### 12. Google 与 Transformer（全站最有力的案例）
- 2017-06 发表论文，作者顺序随机。[V]
- 2018-06-11 OpenAI 发布 GPT-1，用的是 decoder-only 的 Transformer。[V]
  <https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf>
- 2020 年 1 月 Meena（arXiv 2001.09977）：26 亿参数，训练文本 341 GB。[V]
- WSJ（2024 年 9 月）报道：Google 以安全和公平为由拒绝发布 Meena；Shazeer 写过内部备忘录 "Meena Eats the World"。[S]
- 2021 年 Shazeer 和 De Freitas 离开，创办 Character.AI。
- 2022-11-30 ChatGPT 发布。2022-12-21 NYT 报道 Google 内部进入 "code red"。[S]
- 2023-02-08 Bard 演示出错：它说韦布望远镜拍下了第一张系外行星照片，其实第一张是 2004 年 VLT 拍的。Alphabet 当天跌约 7.7%，市值蒸发约 1,000 亿美元。[V]
  <https://www.cnn.com/2023/02/08/tech/google-ai-bard-demo-error>
- 2024 年 8 月，Google 花约 27 亿美元，以授权加回聘的方式把 Shazeer 请回来，让他出任 Gemini 联合负责人。[S]
- **2026-06-18 Shazeer 离开 Google，加入 OpenAI。**[V]
  <https://www.cnbc.com/2026/06/18/google-gemini-co-lead-noam-shazeer-leaves-for-openai.html>
- 写作时注意："所有作者都已离开 Google"要注明时点（到 2024 年初为止）。

### 13. 柯达与富士
- 1975 年，Sasson（当时 24 岁）做出数码相机原型：重 8 磅，10,000 像素，拍一张黑白照片要 23 秒写进磁带。专利 US 4,131,919。[V]
- "that's cute — but don't tell anyone about it"，出自 NYT 2008-05-02 的报道。[S]
- 2012-01-19 申请 Chapter 11 破产保护。[V]
- **神话**："柯达埋掉了数码"过于简化，柯达后来也是数码相机的主要卖家。
- **富士的对照**：
  - 古森重隆主导 VISION 75 计划，两轮重组裁员约 1 万人，花费超过 3,500 亿日元；
  - 2006 年改名 Fujifilm；
  - 2007 年用胶片化学技术推出 Astalift 护肤品；
  - 2008 年以约 14 亿美元收购富山化学；
  - 胶片需求 2000 年见顶，到 2013 年约只剩峰值的二十分之一。[S/V]
  <https://www.nippon.com/en/features/c00511/> · <https://www.cnbc.com/2014/10/21/audacious-makeover-helps-fujifilm-put-best-face-forward.html>

### 14. Xerox PARC
- Alto 1973-03-01；Star 8010 1981 年 4 月，售价 16,595 美元。[V]
- 1979 年 12 月乔布斯来访；作为交换，Xerox 获准以约 100 万美元认购 10 万股 Apple 上市前股票。[S]
- 苹果 Lisa 1983-01-19 推出，售价 9,995 美元。
- **神话**："乔布斯偷了图形界面"。Lisa 的开发早于这次来访，苹果的图形系统是自己重写的；Xerox 1989 年的诉讼大部分被驳回。

### 15. 铁路逼出现代管理
- Chandler，《The Visible Hand》（1977），获 1978 年普利策奖。[V]
- McCallum 和 Henshaw 1854–55 年为 New York & Erie 铁路画的树状组织图，现藏美国国会图书馆。[V]
  <https://loc.gov/pictures/item/ny1255.photos.122185p/>
- McCallum："A superintendent of a road fifty miles in length can give its business his professional attention… In the government of a road five hundred miles in length a very different state exists."[S]

---

## D. 教育面对新技术

### 16. 柏拉图《斐德罗篇》274c–275b
塔穆斯对图提说，书写 "will create forgetfulness in the learners' souls, because they will not use their memories"（Jowett 译）。[V]
<https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0174%3Atext%3DPhaedrus%3Asection%3D275a>

注意：这是柏拉图笔下的苏格拉底讲的神话，而柏拉图正是用文字把它写下来的。

### 17. 计算器
NCTM《An Agenda for Action》（1980）："mathematics programs must take full advantage of the power of calculators and computers at all grade levels." 到 1988 年还有 "The Continuing Calculator Controversy" 这样的文章，后来汇入 1990 年代的"数学战争"。[V]
<https://eric.ed.gov/?id=ED186265>

### 18. 纽约市公立学校
- 2023 年 1 月禁用 ChatGPT；2023-05-18 撤回，局长 Banks 称之为 "knee-jerk fear"。[V]
- **2026-09-02**：对学前班到八年级（约 60 万学生）暂停学生使用生成式 AI 一年；高中只允许 5 个经过批准的工具。[S]
  <https://www.beta.nyc/2026/09/04/nyc-paused-ai-in-its-classrooms-here-is-what-the-policy-actually-says/>
- 寓意：制度还在来回摇摆，说明"没有准备好"。

### 19. 学生用 AI 的数据
- HEPI/Kortext（2025-02-26，英国本科生 1,041 人）：
  - 任何 AI 使用：66% → 92%；
  - 用于作业或考核：53% → 88%；
  - 只有 29% 认为学校"鼓励"使用。[V]
  <https://www.hepi.ac.uk/reports/student-generative-ai-survey-2025/>
- Pew（2025-01-15）：美国 13–17 岁青少年用 ChatGPT 做功课的比例从 13%（2023）升到 26%。[V]
  <https://www.pewresearch.org/short-reads/2025/01/15/about-a-quarter-of-us-teens-have-used-chatgpt-for-schoolwork-double-the-share-in-2023/>

---

## 不用或慎用清单
- "帆船效应"有争议（Mendonça 2013, *Research Policy*）。要么不用，要么注明争议。
- 苏伊士运河"决定"了汽船胜过帆船：没有找到可靠来源。
- 某家具体工厂"只换一台大电机、收益甚微"：找不到实例。
- 沃尔玛越库作业的百分比；集装箱"700%"和"1300%"。
- "柯达埋掉了数码""乔布斯偷了图形界面""百视达当场哄笑"：三者都是神话或夸张。
- 互联网"诞生于哪一年"：1969、1974、1983、1991 各有说法，正文必须讲清是哪个节点。
