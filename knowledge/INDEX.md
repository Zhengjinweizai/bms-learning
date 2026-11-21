# BMS 知识图谱 · 总入口（INDEX）

> **版本**：v0.2.0（2026-11-04 重构为阅读友好结构）｜ 节点 77 个 ｜ 来源 S-01~S-25 ｜ 待验证 P-01~P-12
>
> **怎么读（四选一或混用）**：
> 1. **系统学习**：进 [lessons/](lessons/README.md) 课程层——每课含直觉、公式、**手算实例**、工程实态、误区、自测题。**77/77 节点全部有对应课程**（2026-11-04：SOC 主线 4 课精写批 + 73 课批量批）；每课直达链接在下方各域文件的「课程层」小节。
> 2. **按域浏览**：下面知识树点进任意域文件，每个节点是一张卡片（定义/约束/来源分行呈现）。
> 3. **按学习路径**：每个域文件头部有该域的"最小可学习路径"，从零到能参与讨论的最少概念集。
> 4. **会话内可视化浏览器**：让主理 Agent 展示"BMS 知识浏览器"，可搜索/按成熟度筛选。
>
> 分层记忆法：**lessons/ 是教材，domains/ 是地图，sources/ 是原文库，radar/ 是新闻**。
>
> 维护约定：`graph.md` 为 v0.1.0 冻结登记表（机器可读快照）；**日常增量写入 `domains/` 并同步本文件统计**。

---

## 一、知识树（点击域名进入该域文件）

成熟度标记：`stable` 有现行标准支撑 ｜ `evolving` 已落地但快速迭代 ｜ `frontier` 未收敛 ｜ ⚠️ [需补约束]

- **跨域层 A/B：架构与代际** → [00-跨域层-架构与代际.md](domains/00-跨域层-架构与代际.md)
  - 架构：ARCH-C 集中式 `stable` ｜ ARCH-MS 主从式 `stable` ｜ ARCH-D 分布式 `stable` ｜ ARCH-W 无线 wBMS `evolving` ｜ ARCH-CE 云边协同 `evolving`
  - 代际：GEN-1 传统车载 `stable` ｜ GEN-2 云端辅助 `evolving` ｜ GEN-3 AI/数字孪生 `frontier` ⚠️
- **域一 边界、接口、功能与架构设计** → [01-边界与架构.md](domains/01-边界与架构.md)：SYS-01 功能清单 `stable` ｜ SYS-02 系统边界 `stable` ｜ SYS-03 需求管理 `stable` ｜ SYS-04 网络节点 `stable` ｜ SYS-05 平台化 `evolving`
- **域二 安全设计** → [02-安全设计.md](domains/02-安全设计.md)：SAFE-01 ISO 26262 流程 `stable` ｜ SAFE-02 HARA `stable` ｜ SAFE-03 ASIL 分解 `stable` ｜ SAFE-04 安全机制 `stable` ｜ SAFE-05 网络安全 `evolving` ｜ SAFE-06 AI 安全论证 `frontier` ⚠️
- **域三 基础硬件** → [03-硬件设计.md](domains/03-硬件设计.md)：HW-01 AFE ｜ HW-02 主控 MCU ｜ HW-03 电流传感 ｜ HW-04 高压隔离 ｜ HW-05 执行器 ｜ HW-06 收发器 ｜ HW-07 传感器冗余（全 `stable`）
- **域四 基础软件** → [04-软件设计.md](domains/04-软件设计.md)：SW-01 架构 `stable` ｜ SW-02 调度 `stable` ｜ SW-03 协议栈 `stable` ｜ SW-04 状态机 `stable` ｜ SW-05 标定诊断 `stable` ｜ SW-06 Boot/OTA `evolving` ｜ SW-07 数据上云 `evolving`
- **域五 高压** → [05-高压.md](domains/05-高压.md)：HV-01 HVIL ｜ HV-02 预充 ｜ HV-03 绝缘监测 ｜ HV-04 粘连检测 ｜ HV-05 上下电时序（全 `stable`）
- **域六 核心算法** → [06-核心算法.md](domains/06-核心算法.md)：ALG-01 安时积分 `stable` ｜ ALG-02 模型估计 `stable` ｜ ALG-03 数据驱动 `evolving` ｜ ALG-04 eSOC `evolving` ｜ ALG-05 SOH `stable` ｜ ALG-06 SOP `evolving` ｜ ALG-07 均衡 `stable` ｜ ALG-08 故障诊断 `evolving` ｜ ALG-09 RUL `evolving` ｜ ALG-10 ECM `stable` ｜ ALG-11 电化学模型 `evolving`
- **域七 充电** → [07-充电.md](domains/07-充电.md)：CHG-01 接口 `stable` ｜ CHG-02 协议 `stable` ｜ CHG-03 析锂抑制 `evolving` ｜ CHG-04 充电安全 `stable` ｜ CHG-05 PnC `evolving` ｜ CHG-06 末端控制 `stable`
- **域八 热管理** → [08-热管理.md](domains/08-热管理.md)：THM-01 布点 `stable` ｜ THM-02 热模型 `stable` ｜ THM-03 整车联动 `stable` ｜ THM-04 低温加热 `evolving` ｜ THM-05 热失控 `evolving`
- **域九 故障** → [09-故障处理.md](domains/09-故障处理.md)：FLT-01 分级 `stable` ｜ FLT-02 DTC `stable` ｜ FLT-03 降级 `stable` ｜ FLT-04 断高压 `stable` ｜ FLT-05 归属判定 `evolving` ｜ FLT-06 远程诊断 `evolving`
- **域十 开发验证** → [10-开发验证.md](domains/10-开发验证.md)：DEV-01 V 模型 `stable` ｜ DEV-02 验证阶梯 `stable` ｜ DEV-03 HIL `stable` ｜ DEV-04 合规测试 `stable` ｜ DEV-05 标定耐久 `stable` ｜ DEV-06 场景库 `evolving` ｜ DEV-07 AI 验证 `frontier` ⚠️
- **域十一 化学体系** → [11-化学体系.md](domains/11-化学体系.md)：CHM-01 锂电基准 `stable` ｜ CHM-02 钠离子 `evolving`（约束已实证）｜ CHM-03 固态 `frontier` ⚠️ ｜ CHM-04 梯次利用 `evolving`

## 二、覆盖统计

| 指标 | 数值 |
|---|---|
| 节点总数 | 77 |
| stable / evolving / frontier | 51 / 22 / 4 |
| ⚠️ [需补约束] | 4（GEN-3 / SAFE-06 / DEV-07 / CHM-03）——CHM-02 已于 2026-11-10 解除 |
| 一级域 | 10 + 跨域层 2 + 附加域 1（CHM） |

## 三、[需补约束] 清单

| 节点 | 缺什么 | 候选证据（待核对） |
|---|---|---|
| GEN-3 | 数字孪生 BMS 工程化约束（保真度指标、车云算力分配、认证路径） | S-21 / S-22 / S-23 → P-11；NEMO/InnoBMS 项目级路线（S-53/S-55/S-62） |
| SAFE-06 | AI 安全论证（Safety Case）方法与判据 | S-21 → P-11 |
| DEV-07 | AI 验证指标（不确定度量化、OOD 检测）与接受准则 | S-21 → P-11 |
| ~~CHM-02~~ | ~~钠电 BMS 标准化要求与公开工程实践~~ | **2026-11-10 解除**：公开工程实践已核实（S-24 TENER Sodium）；标准化要求保留为普通待验证 P-57 |
| CHM-03 | 固态电池对 BMS 建模的实证差异 | 学术论文（未定位） |

## 四、配套目录

- [../meta/changelog.md](../meta/changelog.md) 版本日志 ｜ [../meta/source-registry.md](../meta/source-registry.md) 来源登记 ｜ [../meta/pending-verification.md](../meta/pending-verification.md) 待验证清单
- [../radar/](../radar/) 每日雷达 ｜ [../compare/matrix.md](../compare/matrix.md) 厂商对比 ｜ [../sources/](../sources/) 资料库
