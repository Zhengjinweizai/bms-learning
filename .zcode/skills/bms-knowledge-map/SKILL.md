---
name: bms-knowledge-map
description: 构建、扩展与修订本项目 knowledge/graph.md 中的 BMS 知识图谱。当用户要求建立知识树、给 BMS 知识点归类、检查空节点、补充工程约束、生成最小可学习路径，或要求更新知识图谱时必须使用本技能。
---

# Skill: BMS 知识图谱构建与归类

## 任务理解

你需要在 `knowledge/` 下构建一棵可扩展的 BMS 知识树。不要按"教科书目录"平铺，而是按"BMS 工程师实际面对的决策层级"组织。

## 参考骨架（不是穷举，按此层级扩展）

依据 T/CAAMTB《电动汽车用电池管理系统设计规范》的章节结构（编号待登记，见 `meta/pending-verification.md`），BMS 知识可分为以下一级域：

1. 边界、接口、功能汇总与架构设计
2. 安全设计专题（含功能安全 / ISO 26262 相关）
3. 基础硬件设计（主控、从控、高压监测、传感器、执行器）
4. 基础软件设计
5. 高压采集与高压控制
6. 核心算法（SOC / SOH / SOP / 均衡 / 故障诊断）
7. 充电控制
8. 热管理
9. 故障检测及处理
10. 产品开发过程与验证

在此基础上，必须增设两个"跨域"层：

- **架构层**：集中式 / 分布式 / 主从式 / 无线 BMS（wBMS）的适用场景与取舍。
- **代际层**：传统车载 BMS → 云端辅助 BMS → AI/数字孪生驱动的预测型 BMS。

## 执行步骤

1. 先输出知识树草案（Markdown 缩进列表），标注每个节点的"成熟度"：稳定知识 / 演进中 / 前沿未收敛。
2. 为每个一级域写 1 条"最小可学习路径"：列出读者从零到能参与该域工作所需的最少 3～5 个概念节点。
3. 检查知识树中是否存在"只有功能名、没有工程约束"的空节点。对有功能名但缺乏约束的节点，标注 `[需补约束]`。
4. 写入 `knowledge/domains/`（按域的节点卡片文件，编号 `00~11`），并同步 `knowledge/INDEX.md`（知识树、统计、[需补约束] 清单）；`knowledge/graph.md` 是 v0.1.0 冻结登记表，仅随大版本重生成。最后在 `meta/changelog.md` 记录版本号和覆盖变化。

## 输出格式

每个知识节点使用统一 schema：

- `id`
- `name`（中/英）
- `parent`
- `maturity`（stable / evolving / frontier）
- `one_line_definition`
- `key_constraints`（至少 1 条工程/安全/成本约束）
- `linked_sources`（文件路径或 URL，或 `meta/source-registry.md` 中的 S 编号）
- `last_reviewed`（日期）

## 课程层（knowledge/lessons/）

当用户要求把节点"讲透""出实例""出课程"时，在 `knowledge/lessons/` 建课（固定结构与现有课程清单见 `knowledge/lessons/README.md`）。硬规则：

1. **手算实例**：每课必须含数字自洽、可复算的手算实例；非来源数字一律标注"教学示意值"。
2. **延伸资源**：每课必须附"延伸资源"栏——联网核实的真实链接（禁止编造 URL/DOI），标注 A/B/C 级别与免费状态，并登记 `meta/source-registry.md`。
3. **待核对登记**：课程中引用但未核实的表述，登记 `meta/pending-verification.md`。

## 成熟度定义

- `stable`：有现行标准或成熟工程实践支撑，预计 3~5 年内不会被颠覆。
- `evolving`：工程上已落地但方法仍在快速迭代（如数据驱动估计、wBMS 生态）。
- `frontier`：尚未收敛，论文与演示多于量产产品（如数字孪生 BMS、固态电池适配）。
