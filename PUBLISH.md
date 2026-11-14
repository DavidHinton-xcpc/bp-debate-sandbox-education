# BP 辩论稿沙盘 · 发布说明（2026-11-15）

本目录是本次「教育辩题 BP 辩论稿沙盘」任务的完整落盘成果，用于 GitHub Pages 发布。

## 在线页面

| 文件 | 用途 |
| --- | --- |
| `index.html` | **双语版（默认英文）**——Pages 首页。标题行右侧按钮切中文，页内浮层可对比立论 / 驳论 / 声援 |
| `en.html` | 纯英文交付稿（无切换按钮），供交作业 / 打印 |
| `README.md` | 完整项目说明：任务依据、教材页码、mode 层级、席位分配、数据来源、词数表、历轮返工与校验记录 |
| `team-list.md` | 按老师邮件格式排版的提交版名单 |
| `src/build_en.py` | 英文稿生成器（内容数据 + HTML 渲染 + 词数统计） |
| `src/build_bilingual.py` | 双语版生成器（读取英文稿，挂 `data-en` / `data-zh` 与切换逻辑） |

## 关键约束落实

- 沿用旧案例 `BP辩论稿沙盘.html` 的版式、开场/收尾语体、立论编号、驳论指向、页内对比浮层（面积 2/5、字号 125%）。
- 辩题 `“Education isn’t as good as it used to be.” (p. 75)`；教材 p.75 第 4 题是 cause reductionism 谬误示例，全稿逐席标出规避的谬误，不把「教育变差」简化为「教师失职」。
- 八席按 BP 发言顺序 `PM→LO→DPM→DLO→MG→MO→GW→OW` 与给定姓名顺序一一对应：房俊杰、耿韵清、海涵、季佳慧、李佳琪、李思涵、梁程、梁涵。
- 每席三成分独立分段：`Here is my evaluative/relational argument claim:` / `Here is my evidence:` / `Here is my warrant:`；mode 落在 claim 标签上（教材 p.48 的三种模式），课本技术原词以 `.method` 小字标注，共 26 处。
- 每席英文词数 `215/217/230/227/189/207/195/209`，均 ≤230；`specifically` 与 `This is because` 均为 0 次。
- Evidence 含可核查数据（World Bank API，2026-11-14 取数）：成人识字率 74.6%→87.6%、小学净入学率 82.0%→89.2%、高等教育毛入学率 13.3%→43.2%；未取得原文的 PISA 分数不写。

## 移动端适配

`@media (max-width:600px)`：标题行两行布局（按钮固定右侧）、单列卡片、标签自动换行、`overflow-wrap:anywhere` 防长英文词溢出、浮层改 `94vw×82vh` 且左右对比改上下双栏。

实测视口 `390×844 / 360×740 / 320×568 / 768×1024`：横向溢出均为 `false`，按钮始终在标题行右上，浮层单列，中文切换与弹窗无报错。

## 本地复现

```bash
python3 src/build_en.py        # 生成英文稿（写桌面 BP辩论稿沙盘_教育辩题.html）
python3 src/build_bilingual.py # 读取英文稿生成双语版
```

两个生成器为单文件、零外部依赖；成品 HTML 可离线 `file://` 打开，A4 横向打印样式内置。
