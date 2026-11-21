---
name: bms-daily-radar
description: BMS 每日前沿雷达扫描与入库。当用户要求抓取 BMS 最新动态、跑"今日雷达"、更新 radar/ 目录、或询问 BMS 领域最近有什么新进展时必须使用本技能。覆盖 AI/云/数字孪生 BMS、后市场与商业模式、安全与功能安全、新兴电池化学体系四个方向。
---

# Skill: BMS 每日前沿雷达

## 抓取范围（按优先级）

1. **AI / 云 / 数字孪生 BMS**：机器学习、深度学习、强化学习在 SOC/SOH/SOP 估计中的应用；cloud-assisted BMS、digital-twin-based BMS、无线 BMS 的架构进展。
2. **后市场与商业模式**：BMS 数据上云后的远程诊断、SoH 评估、剩余寿命预测、电池订阅 / BaaS / 残值评估。LG Energy Solution 的 B-Lifecare、B.once、B.around 和 KooRoo 是这一方向的标志性产品，其逻辑是"车端实时控制、云端数据分析"的分工架构（细节见 `meta/pending-verification.md`）。
3. **安全与功能安全**：AI 验证、通信可靠性、cloud-edge coordination、网络安全、传感器故障与不确定性处理。
4. **新兴电池化学体系对 BMS 的冲击**：跨化学体系可迁移性、第二寿命电池的 BMS 适配。

## 每日执行步骤

1. 检索过去 24～72 小时内的新内容。若某领域当日无新增，明确写"今日无新增，最近一条为 X 月 X 日"。
2. 每条条目必须包含：标题 / 来源 / 发布日期 / 一句话核心 / 与知识图谱哪个 node 相关 / 为什么值得关注（1 句判断）。
3. 按"信号强度"排序：**产品化落地 > 头部厂商官方动作 > 同行评议论文 > 行业媒体分析 > 自媒体评论**。C 级来源不进入当日 Radar 主列表，放入 `radar/leads/`。
4. 写入 `radar/YYYY-MM-DD.md`，并在文件头写 `SCAN_DATE` 和 `COVERAGE_WINDOW`。

## 输出示例 schema

```
- [信号强度] 标题 | 来源 | 日期
  核心：…
  关联 node：…
  判断：…
```
