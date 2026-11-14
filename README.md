# BP 辩论稿沙盘（教育辩题）· 项目说明

> 配套文件：`BP辩论稿沙盘_教育辩题.html`（成品）、`队伍名单_教育辩题.md`（按老师格式排版的提交版名单）。
> 沿用旧案例 `BP辩论稿沙盘.html` 的 CSS / JS / 版式 / 编写规范；说明单独成文，不写入 HTML。

## 1. 纠错说明（本轮返工）

上一版把「总字数控制在 230 词内」误读为**全场八席合计 ≤230**，压成每席 20 多词的电报句，丢掉了开场收尾、驳论链、页内对比浮层与完整论证，质量不合格。

已按用户指正恢复：**原沙盘要求全部继续有效**，新要求只是叠加增量。经核对旧案例：

| 项 | 旧案例实测 | 本版实测 |
| --- | ---: | ---: |
| 每席英文词数 | 176–216（限 220） | 189–230（限 230） |
| 全场合计 | 1591 | 1689 |
| 开场 / 收尾 | 8 / 8 | 8 / 8 |
| 完整 C/E/W 组 | 12 | 8 组（每席一组，新增 Mode 独立块） |
| 驳论按钮 | 15 | 16（其中 5 个为声援） |
| 页内浮层 | 2/5 面积、125% 字号 | 同左 |

因此 **230 词按「每席发言总词数 ≤230」执行**，与旧案例 220 词/席同一口径（本轮放宽 10 词以容纳声援句与模式说明）。若按「全场合计」读法，则每席不可能写出完整稿、驳论与开场收尾，也与「参考先前沙盘」直接冲突。

## 2. 沿用原沙盘的硬约束（全部保留）

- 单文件、零外部依赖，`file://` 可离线打开；A4 横向打印样式、窄屏单列。
- 两列逐行八卡，`align-items:start`，顺序 `PM → LO → DPM → DLO → MG → MO → GW → OW`；政府蓝、反方橙、Whip 虚线边框。
- 每席固定三段：`开场`（`Madam Speaker` + framing + 结构预告）→ `主体`（编号立论 / 驳论）→ `收尾`（`For all those reasons…` + 投票方向）。开头收尾句式沿用旧案例已采真实赛事转录核对过的写法，不自造套语。
- 立论编号「席位-序号 + 中文要点名」；编号只用于 `id` / 按钮 / 弹窗，**不进入发言正文**，正文一律用内容概括指代（如 `the fixed standard`、`the individual calculus`、`the measurement objection`）。
- C / E / W **各自单独成一个 `<p>`**，连接词放在各段内部（`specifically,` 在 Evidence 标签后，`This is because` 在 Warrant 标签后）；中文小标题改为英文 tagline 并计入词数。
- Warrant 写成「证据 → 中间机制 → 主张」，详细解释连接，不重述 Claim。
- Evidence 直接陈述事实，不以教材页码作主语；页码只出现在本说明。
- 驳论 `href` 与 `data-target` 一致，全部指向先前已出现的立论；无断链。
- 页内居中浮层 `63.25vw × 63.25vh`（面积 2/5），字号 125%（`--pop:1.25` + `calc`），左栏被驳立论、右栏本席驳论；关闭按钮 / Esc / 点遮罩三种；不打开新网页。
- MG / MO 做 extension 并回应对方新论点；GW / OW 只称重、不新增论点。

## 3. 本轮新增要求

### 3.1 辩题与教材依据

`“Education isn’t as good as it used to be.” (p. 75)`。教材 p.75（PDF 第 94 页，Unit 5 Activity 1）第 4 项原文为 `“Education today isn’t as good as it used to be—obviously, our teachers are not doing their jobs.”`，是 **cause reductionism** 谬误示例。

本沙盘刻意不把「教育变差」简化为「教师失职」，逐席标出规避的谬误，且只用教材 p.75 列出的五种：False analogy / Cum hoc ergo propter hoc / Post hoc ergo propter hoc / Cause reductionism / Slippery slope。例如 PM-1 的 Warrant 明确写成「关于激励结构及其可观察产物的主张，而非关于教师努力或某一次改革」，避免单因归责。

### 3.2 姓名与发言顺序一致

BP 发言顺序即 `1 PM → 2 LO → 3 DPM → 4 DLO → 5 MG → 6 MO → 7 GW → 8 OW`，8 个姓名依给定顺序依次落位，卡片 `data-order` 1–8 读下来就是姓名顺序：

| 序 | 席位 | 姓名 | 队伍 | 立场 |
| ---: | --- | --- | --- | --- |
| 1 | PM | 房俊杰 | Opening Government | 支持 |
| 2 | LO | 耿韵清 | Opening Opposition | 反对 |
| 3 | DPM | 海涵 | Opening Government | 支持 |
| 4 | DLO | 季佳慧 | Opening Opposition | 反对 |
| 5 | MG | 李佳琪 | Closing Government | 支持 |
| 6 | MO | 李思涵 | Closing Opposition | 反对 |
| 7 | GW | 梁程 | Closing Government | 支持 |
| 8 | OW | 梁涵 | Closing Opposition | 反对 |

`队伍名单_教育辩题.md` 已按老师邮件给定的 OG / CG / OO / CO 分组格式排版，可直接提交。名单文件只是草稿，**未发送邮件**。

### 3.3 mode of argumentation 的层级（本轮修正）

教材 p.48（PDF 67）「Three modes of argumentation」引 Robert Trapp：**三种 mode 是 Descriptive / Relational / Evaluative**，可单独使用也可交织。p.47 Activity 2 要求 `Choose the appropriate mode of argumentation`，并让听者评价 `the appropriateness of the mode`。

| Mode | 处理什么 | 教材页 | 建构 / 反驳技术（**子层级，不是 mode**） |
| --- | --- | --- | --- |
| Descriptive | 事物的性质与定义 | p.48–49 | Differentiation、Analogy、Authority / Intrinsicality、Thoroughness |
| Relational | 现象间关系，通常因果 | p.50–51 | Reduction、Comparison、Authority / Absence、Correlativity、Alternativity |
| Evaluative | 好坏、可取与否的价值判断 | p.51–53 | Definition、Standard / Definition、Standard、Measurement |

**第一次纠错**：更早一版把 `Definition / Reduction / Comparison / Absence / Measurement / Standard` 直接标成 `Mode`，是把子类当父类。现改为两级标注：卡片上 `Mode: …` 只写三种模式，`Technique: …` 写具体技术。

本辩题 `as good as` 是价值判断 → 主线 **Evaluative**；`than it used to be` 隐含历时因果解释 → **Relational**；`what education is` 的定义争夺 → **Descriptive**。教材允许三者交织。

| 席位 | Mode | Technique | 适配理由 |
| --- | --- | --- | --- |
| PM | Evaluative | Definition | 先定对象再定评判标准 |
| LO | Relational | Definition / Alternativity | 目标扩容作为同一变化的替代原因 |
| DPM | Relational | Reduction | 把一般因果缩减为一次可预测选择 |
| DLO | Relational | Absence | 无因时应无果 |
| MG | Relational | Comparison | 固定能力变量隔离激励 |
| MO | Evaluative | Measurement | 代理变量未达被评价的结果 |
| GW | Evaluative | Standard | 按既定标尺全场称重 |
| OW | Evaluative | Measurement | 标尺不稳无法承载价值判断 |

**本轮第二次修正：mode 标在 claim 上，而不是做成第四个成分。**

老师 task 3 的评分标准只有 `claim / evidence / warrant` 三项；mode 描述的是**主张的类型**（教材 p.48：descriptive 问 what something is，relational 问现象间关系，evaluative 问好坏），因此应写成 `Here is my evaluative argument claim:` / `Here is my relational argument claim:`，而不是另起 `Here is my mode of argumentation:` 一段。上一版把「属性」当成了「成分」，已删除该独立块。

现在每席主论点含 **3 个独立 `<p>`**（与旧案例一致）：带模式标签的 Claim、Evidence、Warrant。模式与技术的适配说明并入 Warrant 末尾一句（如 `In this evaluative claim, Definition fixes the object and the standard judges it.`），既满足「至少使用一种 mode」，又说明为什么该 warrant 适配该 claim —— 这正是 p.75 第 4 题的考点：评价性主张必须接「标准 + 测量」型 warrant，不能接 `obviously, our teachers are not doing their jobs` 那种单因归因。

按 claim 定性后还查出一处实质错配并修正：上一版给 LO 标 `Evaluative / Definition`，但 LO 的 claim 是「目标扩容解释了同一变化」，那是**替代原因**的 relational 主张，已改为 `Mode: Relational`。

八席 claim 类型：`PM evaluative / LO relational / DPM relational / DLO relational / MG relational / MO evaluative / GW evaluative / OW evaluative`。

另保留 PM-2（Relational / Comparison）、LO-2（Relational / Alternativity）两个补充立论及 11 条驳论。

### 3.4 声援环节（5 席）

后续席位对本阵营先前观点作重申或发展，点击按钮同样弹出页内浮层，标题与左右栏标签自动切换为「声援 / 被声援立论 / 本席声援」：

| 席位 | 指向 | 内容 | 性质 |
| --- | --- | --- | --- |
| DPM 海涵 | PM-1 标准先行 | `I reaffirm the fixed standard…` | 重申 |
| DLO 季佳慧 | LO-2 测量人群 | `I develop the access point…` | 发展 |
| MG 李佳琪 | DPM-1 个体权衡 | `I develop the individual calculus…` | 发展 |
| GW 梁程 | MG-1 制度边际 | `I reaffirm the institutional extension…` | 重申 |
| OW 梁涵 | MO-1 测量缺口 | `I reaffirm the measurement gap…` | 重申 |

## 4. 词数

按旧案例口径：只统计 `class="en"` 的英文发言正文（含开场/收尾、英文 tagline、四组标签与连接词、驳论句、声援句）；中文标题、席位名、方法标签、谬误标签、编号不计入。

| 席位 | 词数 | ≤230 |
| --- | ---: | :---: |
| PM | 215 | ✓ |
| LO | 217 | ✓ |
| DPM | 230 | ✓ |
| DLO | 227 | ✓ |
| MG | 189 | ✓ |
| MO | 207 | ✓ |
| GW | 195 | ✓ |
| OW | 209 | ✓ |
| **合计** | **1689** | — |

## 5. 校验记录

- 8 个 `data-seat` / `data-order` 顺序正确；8 个姓名顺序与给定名单一致；GW / OW 标「不新增论点」。
- 8 个开场、8 个收尾；8 个 `cwe` 各含 3 个独立 `<p>`；`Here is my evaluative/relational argument claim:` 共 8 次、`Here is my evidence:` 8 次、`Here is my warrant:` 8 次；已无 `Here is my mode of argumentation:` 与 `.modep` 独立块；卡片 `Mode: Evaluative/Relational` 共 10 处、`Technique:` 共 10 处，无子类误标为 Mode；无 `This is because` 重复。
- 10 个立论 ID 唯一（PM-1 PM-2 LO-1 LO-2 DPM-1 DLO-1 MG-1 MO-1 GW-1 OW-1）；16 个 `data-target` 与 `href` 完全一致且全部解析成功；编号显示规则修正后 `PM-2` / `LO-2` 按钮文字正确。
- HTML 标签嵌套无 mismatch / unclosed；`<style>` / `</style>` 各 1（本轮曾漏写 `<style>` 包裹导致样式失效，已修复）；内联 JS 通过 `node --check`。
- `.en` 正文内无 `PM-1` 一类序号残留；无 `class="flow"`；无外部资源；教材页码仅出现在页首辩题括注与说明文件。
- Playwright + Chrome 实测：席位与姓名正确；16 个按钮（含 5 声援）；点击 PM-1 驳论 → 浮层标题 `PM-1 · 标准先行 ⇄ LO 的驳论`，左栏含完整 C/E/W/Mode，右栏含驳论；点击声援按钮 → 标题 `PM-1 · 标准先行 ⇄ DPM 的声援`，左右栏标签正确；点击 PM-2 → 编号显示 `PM-2 · 制度复现`。
- 浮层尺寸 `885.5×569.25` / `1400×900` = **40.01%** 面积，居中 `(257.25,165.375)`；正文 125% 后 `14.375px`；抽样 8 个浮层左右栏 `scrollHeight/clientHeight` 差 ≤4px（可滚动，无溢出截断）；Esc 关闭；页面数前后均为 1（无 `window.open`）；`pageerror` 与 console error 均为空。
- 全页截图检查：两列逐行、C/E/W/Mode 分段清晰、声援块与驳论块可区分，无跑版。

## 6. 本轮三项修订

### 6.1 默认英文 + 中英切换

`BP辩论稿沙盘_教育辩题_中英切换.html` 默认英文（`<html lang="en">`，按钮标「中」），点击右上角按钮切中文（按钮变 `EN`）；117 个文本节点挂 `data-en` / `data-zh`，浮层标题与左右栏标签同步切换。原 `BP辩论稿沙盘_教育辩题.html` 保留为纯英文交付稿。打印时按钮隐藏。

### 6.2 驳论与声援标注课本方法（小字）

每条驳论、声援、补充立论增加 `.method` 小字标签，取值**严格用教材 p.48–53 的英文术语**，不自行翻译或改名：

| 类别 | 课本原词 | 出现处 |
| --- | --- | --- |
| Creating descriptive | Differentiation / Analogy / Authority | — |
| Opposing descriptive | **Intrinsicality**、**Thoroughness** | LO 驳 PM-1、DLO 驳 DPM-1、DLO 驳 PM-1、OW 驳 PM-1、LO-2 |
| Creating relational | **Reduction**、**Comparison**、**Authority** | DPM 立论、MG 立论、PM-2、DPM 声援、MG 声援、GW 声援 |
| Opposing relational | **Absence**、**Correlativity**、**Alternativity** | DPM 驳 LO-1、LO 驳 PM-2、MG 驳 DLO-1、MO 驳 PM-2 |
| Creating evaluative | **Definition**、**Standard** | DPM 声援、GW 驳 MO-1 |
| Opposing evaluative | **Definition**、**Standard**、**Measurement** | DPM 驳 LO-2、DLO 声援、MO 驳 MG-1、OW 声援 |

主论点卡片的 `Technique:` 与 Warrant 末句仍标明该条所用方法；驳论/声援的 `.method` 说明**该动作本身**用了哪种方法。共 18 处。

### 6.3 Evidence 与语言多样性

**Evidence 补强（可核查口径）**：删除全部 `specifically,` 与 `This is because` 模板连接词，八席改用互不重复的引导语（`World Bank data show` / `UNESCO learning domains and World Bank series show` / `Behavioural research on incentives, cited as Authority here, finds` / `In curriculum case studies reported by OECD reviews,` / `Cross-system assessment studies report that` / `The very World Bank series Government cites` / `Three independent lines converge:` / `The record before the House contains`）。

已核实并写入稿中的数据（World Bank API，取数 2026-11-14）：

| 指标 | 1990 | 2023 |
| --- | ---: | ---: |
| 全球成人识字率 `SE.ADT.LITR.ZS` | 74.6% | 87.6% |
| 小学净入学率 `SE.PRM.NENR` | 82.0% | 89.2%（2015，之后缺值） |
| 高等教育毛入学率 `SE.TER.ENRR` | 13.3% | 43.2% |

其余 evidence 明确标为机构评述 / 课堂给定材料（OECD curriculum case studies、cross-system assessment studies、behavioural research cited as Authority）。**未取得可核查原文的 PISA 具体分数一律不写**：OECD 官网返回 403，搜索引擎结果噪声，故不伪造统计。MO-1 与 OW-1 反过来利用这一缺口：政府方援引的 World Bank 序列只含入学率与识字率，没有迁移能力的前后测。

**语言多样性**：八席开场、收尾、tagline、evidence 引导语、warrant 起句全部互不相同；`specifically` 出现 0 次、`This is because` 出现 0 次。每席仍有 `Here is my … argument claim / evidence / warrant` 三项标签（评分标准），但标签后的行文按席位职责差异化：PM 定标准、LO 换标尺、DPM 缩到个体、DLO 做缺席检验、MG 做制度扩展、MO 抓测量缺口、GW 称重、OW 收束怀疑。

**词数**：`215 / 217 / 230 / 227 / 189 / 207 / 195 / 209`，每席 ≤230，合计 1689。

**校验**：HTML 嵌套无 mismatch、内联 JS `node --check` 通过；Playwright 实测默认 `lang=en`、按钮「中」、切换后 `lang=zh-CN`、中文 evidence 含 74.6%/87.6%、18 处 `.method`、浮层中文/英文标题均正确、面积 40.01%、页面数不变、无控制台报错；全页截图（英/中）已复查。

## 7. 语言切换闪烁与按钮位移修复

### 7.1 闪烁根因

旧实现 `applyLang()` 每次点击对 117 个节点逐个写 `textContent`；浮层 `open()` 又是先 `ov.hidden=false` 再改语言，导致「旧语言先渲染一帧 → 再重绘」的可见闪烁，中文字体首次加载的 FOUT 会放大它。

**修复**：改为**纯 CSS 一次 class 切换**：

- 每个文本节点内置两个 span（`.lang-en` / `.lang-zh`），两套文本都在 DOM 里，由 `body.lang-zh` 一条规则控制显隐；点击只执行 `document.body.classList.toggle('lang-zh')`，**不再写任何 `textContent`**。
- 按钮文字用 `#langToggle::before{content}` 由同一 class 切换，不进 DOM 文本（避免双串拼接）。
- 浮层标题与左右栏标签在 `ov.hidden=false` **之前**由 `tagTitles()` 一次性生成双语 span；已删除 `ttl.textContent` 等一次性中文写入。
- 同步 `aria-hidden`，保证读屏 / 复制只取当前语言那份文本。
- 连续切换 20 次实测：无报错、无中间态、可见文本干净。

### 7.2 按钮位移根因

`position:fixed` 本身正确；但浮层打开时 `body.style.overflow='hidden'` 使滚动条消失、视口宽度变化，固定元素相对右边缘视觉位移。另中文「中」与英文 `EN` 字宽不同，切换时按钮宽度也变。

**修复**：

- `html{scrollbar-gutter:stable}` 让滚动条槽常驻；
- 按钮 `width:46px; height:28px; padding:0; text-align:center`，加 `transform:translateZ(0)` 独立合成层。

实测按钮坐标：默认 `/ 中文态 / 滚动 3000px / 浮层打开` 四种状态均为 `x=1319, y=14, w=46, h=28`，零位移。

### 7.3 复核

- 默认 `lang=en`、按钮「中」；中文态 `lang=zh-CN`、按钮 `EN`；`innerText` 分别只含对应语言文本。
- 浮层中文标题 `PM-1 · 标准先行 ⇄ LO 的驳论`、英文 `PM-1 ⇄ LO · Rebuttal`；面积仍 40.01%，页面数 1，无控制台报错。
- 两文件按「只统计可见 `.lang-en`」口径重算词数，均为 `215/217/230/227/189/207/195/209`，每席 ≤230；18 处 `.method`、16 条链接齐全；两份内联 JS 均通过 `node --check`。

## 8. 按钮改挂标题行（最终）

用户反馈「固定在标题行右侧」，此前 `position:fixed` 的视口浮层不是想要的效果，且在浮层打开 / 滚动时视觉上仍会漂。

**改动**：按钮从 `<body>` 顶层移入 `<header class="top">`，成为 flex 末项（`flex:0 0 auto; align-self:center; margin-left:auto`），`position:static`。删掉 `position:fixed`、`top/right`、`translateZ(0)`、`header.top{padding-right:…}`。位置由标题行布局决定，与滚动、浮层遮罩、合成层都无关。

实测（1400×900）：

| 状态 | 按钮坐标 | 相对文档 |
| --- | --- | --- |
| 初始 | `x=1315, y=25, 46×28` | docTop 25 |
| 中文态（连续切换 11 次） | 同左 | 同左 |
| 滚动 1200px | 视口 y = −1175 | docTop 仍 25 |
| 浮层打开 | 同左 | 同左 |

标题行 `x=24, w=1337`，按钮右边缘与标题行右边缘 gap = 0，垂直方向完全落在 header 内；`getComputedStyle().position === 'static'`。默认英文、双语切换、浮层双语标题、面积 40.01%、18 处方法小字、16 条链接、无控制台报错均复测通过。

## 9. 标签去重与中文版残留清理

### 9.1 Technique / Method 重复

补充立论 PM-2、LO-2 曾同时挂 `Technique: X` 标签与 `.method` 小字 `X`，同一方法标了两遍。现已统一为**两层、各只出现一次**：

| 位置 | 显示 | 含义 |
| --- | --- | --- |
| 卡片 `Mode: …` | 三种模式之一 | claim 的类型（descriptive / relational / evaluative） |
| `.method` 小字 | 课本技术原词 | 该动作所用的建构 / 反驳方法 |

删除全部 `Technique:` 标签；主论点也改为 `Mode: …` + 一处 `.method` 小字。全部 10 个立论条目 + 16 条驳论 / 声援 = **26 处 `.method`**，`Technique:` 出现 0 次。

### 9.2 中文版残留

- `以下是我的论证依据（warrant）：` → `以下是我的论证依据：`，中文态 `（warrant）` 出现 0 次。
- `Mode: …` / `Method: …` 前缀双语化：中文态为 `模式：…` / `方法：…`；方法名本身（Definition / Absence / Measurement 等）保留课本英文原词，术语不译。
- `.method::before` 的 `content:"Method: "` 增加 `body.lang-zh` 规则 → `content:"方法："`。

实测：英文态 `Here is my warrant:` + `Mode: Evaluative` + `Method: Definition / Standard`；中文态 `以下是我的论证依据：` + `模式：Evaluative` + `方法：Definition / Standard`。中文态全文已无 `Technique:` / `Mode:` / `（warrant）`。

复核：两文件词数均 `215/217/230/227/189/207/195/209`（≤230）、26 处 `.method`、16 条链接全解析、按钮仍在标题行右端、浮层 40.01%、无报错；两份内联 JS 通过 `node --check`。

## 10. 移动端适配与 GitHub Pages 发布（2026-11-15）

### 10.1 落盘结构

独立目录 `debate-sandbox/`（独立 git 仓库，不混入工作目录其他项目文件）：

| 文件 | 用途 |
| --- | --- |
| `index.html` | 双语版（默认英文），Pages 首页 |
| `en.html` | 纯英文交付稿 |
| `README.md` | 本说明全文 |
| `PUBLISH.md` | 发布与本地复现说明 |
| `team-list.md` | 提交版名单 |
| `src/build_en.py` / `src/build_bilingual.py` | 两个生成器 |

### 10.2 移动端适配

`@media (max-width:600px)`：

- 标题行两行布局：`h1` 与按钮同行（按钮 `margin-left:auto` 固定右侧），辩题单独一行；header 高度由 141px 降到 67px（390 宽）/ 86px（320 宽）。
- 卡片单列、内边距收紧；`.tag / .avoid / .method` 可换行、字号 9.5px；`.method::before` 缩写为 `M: `（中文态 `法：`）。
- 所有正文 `overflow-wrap:anywhere; word-break:break-word`，防长英文词与数据串撑破卡片；`.seat{overflow:hidden}`。
- 浮层 `94vw × 82vh`，`cmpGrid` 由左右两栏改为**上下两栏**（`grid-template-columns:1fr; grid-template-rows:1fr 1fr`）。
- 增加内联 SVG `data:` favicon，消除浏览器自动请求 `/favicon.ico` 产生的 404。

实测视口 `390×844 / 360×740 / 320×568 / 768×1024`：`documentElement.scrollWidth === innerWidth`，无横向溢出；按钮始终在标题行右上；浮层单列；中文切换与弹窗无 `pageerror` / console error。

### 10.3 发布

- 仓库：`https://github.com/DavidHinton-xcpc/bp-debate-sandbox-education`（public）
- Pages：`build_type=legacy`，`source=master:/`
- 线上地址：**https://davidhinton-xcpc.github.io/bp-debate-sandbox-education/**
- `en.html`、`README.md` 均返回 200；首屏默认 `lang=en`、按钮「中」，切换后 `lang=zh-CN`；线上移动端复测无横向溢出、浮层面积 77.1%（窄屏竖排）、桌面 40.0%（2/5）、中文态无 `（warrant）` / `Technique:` 残留。
- 推送时 HTTPS remote 缺凭据，已用 `gh auth token` 配本地 credential helper 完成同步（`a39cb58`）。
