# BMS 学习平台

追溯式知识管理工程：以**可追溯、带日期、分层对比**三条铁律，系统学习电池管理系统（BMS，Battery Management System）。

> 三条铁律：① 每个事实/判断/数据点附来源（标准编号 / 论文 DOI / 会议+日期 / 厂商官方文档）；② 任何"最新/目前"的表述必须带日期；③ 厂商对比必须落到维度（架构/算法/硬件/集成层级/商业模式），不接受笼统结论。

## 当前规模（截至 2026-11-21）

| 资产 | 数量 | 位置 |
|---|---|---|
| 知识节点 | **77**（stable 51 / evolving 22 / frontier 4） | `knowledge/domains/`（12 个域文件）+ `knowledge/graph.md`（冻结登记表） |
| 课程 | **77 门**（每课含手算实例、工程实态、误区、自测题） | `knowledge/lessons/` |
| 学习路径 | 12 条 | 各域文件头部 |
| 每日前沿雷达 | 9 期（滚动） | `radar/YYYY-MM-DD.md` |
| 会议/项目条目 | 8 个（AABC、NEMO、InnoBMS、CBIS2026 等） | `radar/conferences/` |
| 来源登记 | **S-01~S-86**（A/B 级，含标准/论文/官方文档） | `meta/source-registry.md` |
| 待验证清单 | 50 项（诚实机制：有线索但证据不足的表述） | `meta/pending-verification.md` |
| 厂商对比矩阵 | 4 行主表（LG / TI / ADI / CATL） | `compare/matrix.md` |

## 怎么读

1. **在线交互版**：https://zhengjinweizai.github.io/bms-learning/ （GitHub Pages，开通后生效；手机可用）
2. **总入口**：[knowledge/INDEX.md](knowledge/INDEX.md)（知识树 + 统计 + 待补约束清单）
3. **离线交互版**：运行 `python3 tools/build_site.py` 生成 `site/index.html`（本地用）/ `docs/index.html`（仓库内同步副本），浏览器打开即可全文搜索、按域浏览、跟学习路径、记已读进度
4. **课程主线**：`knowledge/lessons/` 按域的最小学习路径推进（推荐从 SOC 主线 4 课开始）

## 每日自动化

每天 0 点自动执行：四方向前沿雷达扫描 → 待验证清单消化（3~5 条）→ 会议追踪 → 重建阅读站 → 更新 changelog → **git 提交并推送**（本仓库每日快照）。无增量也会诚实记录"今日无增量"。

## 目录结构

```
knowledge/   知识图谱（lessons/ 课程层 · domains/ 节点卡片 · graph.md 冻结登记表 · INDEX.md 入口）
sources/     资料库（标准 / 论文 / 官方文档 / 视频笔记，分级 A/B/C）
radar/       每日前沿与会议追踪（leads/ 为 C 级线索池）
compare/     厂商对比矩阵（电池厂 vs 主机厂角色分层）
meta/        changelog · 来源登记 · 待验证清单 · 代理报告
tools/       build_site.py（阅读站构建脚本）
site/        构建产物（不入库，一键再生成）
```

## 维护规则

- 来源分级：A（标准/法规/官方文档/同行评议论文）＞ B（权威媒体/厂商口径，须标注利益关联）＞ C（自媒体，仅作线索，不进事实层）
- 禁止编造 URL/DOI/数据；教学数字标注"教学示意值"；待核实项进 `meta/pending-verification.md`
- 前沿节点的约束以"多来源核实"为准逐日升级（示例：CHM-02 由 [需补约束] → CATL TENER Sodium 实证解除）
