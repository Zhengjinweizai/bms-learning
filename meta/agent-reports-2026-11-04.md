# 子代理课程写作报告汇总（2026-11-04，待主理 Agent 审核合并）

> 说明：课程批量生产时子代理不得自行修改 meta，其建议汇总于此，由主理 Agent 审核后并入 pending-verification / source-registry。

## 批次 A1：SYS + SAFE（✅ 已完成，11 课）

**产出文件**（knowledge/lessons/，均 85~102 行）：
SYS-01-功能清单.md ｜ SYS-02-系统边界与接口.md ｜ SYS-03-需求管理.md ｜ SYS-04-整车网络节点.md ｜ SYS-05-平台化策略.md ｜ SAFE-01-功能安全流程.md ｜ SAFE-02-HARA.md ｜ SAFE-03-ASIL分解.md ｜ SAFE-04-安全机制与FTTI.md ｜ SAFE-05-网络安全.md ｜ SAFE-06-AI安全论证.md

**自检声明**：9 项结构齐备；S 编号均在 S-01~S-35 内；延伸资源无未核实 URL；文末均有"待核对项"。

**建议新增 P 项（待合并入 pending-verification.md）**：
- P-16 整车网络超时惯例 T_timeout=3×T_cycle 的规范出处（SYS-02/04）
- P-17 CAN 8 字节帧开销 ≈130 bit 与总线负载经验值（单节点 10~15%、整车 40~50%）出处（SYS-04）
- P-18 CAN FD 整车典型速率档位（示意 2~5 Mbit/s）（SYS-04）
- P-19 DIA 在 ISO 26262-2:2018 的具体条款（SYS-03）
- P-20 ISO 26262-6:2018 结构覆盖率与 ASIL 对应表（A→语句/B→分支/D→MC/DC）
- P-21 ISO 26262-5:2018 的 SPFM/LFM/PMHF 各 ASIL 目标数值
- P-22 ISO 26262-9:2018 分解规则表与 Part 5/9 衔接条款
- P-23 接触器分断时间与 kA 级短路耐受器件规格（SAFE-04 示意值）
- P-24 GB 38031 热扩散"5 min 报警提前量"精确条款口径（建议并入 P-05）
- P-25 UN R155 对欧盟所有新产车辆的生效时间点（2024-07 口径）
- P-26 UDS Authentication（0x29）在 ISO 14229-1:2020 中的可用性
- P-27 ISO 21448:2022 与 UL 4600 对 AI 安全论证的适用边界

**建议新增来源（候选）**：ISO 21448:2022（SOTIF，A）、IEC 61508（A）、Smith & Simpson《The Safety-Critical Systems Handbook》（B）、Bosch CAN Specification 2.0（B/A）、Wiegers & Beatty《Software Requirements》3e（B）、Pohl《Software Product Line Engineering》（B）、《The Car Hacker's Handbook》（B）、Uptane 框架（B）、GSN Community Standard（A/B）、UL 4600（A/B）

## 批次 A2：HW + SW（✅ 已完成，14 课）

**产出文件**（knowledge/lessons/，88~106 行，手算数字已复算自校）：
HW-01-AFE模拟前端.md ｜ HW-02-主控MCU.md ｜ HW-03-电流传感.md ｜ HW-04-高压采样与隔离.md ｜ HW-05-执行器驱动.md ｜ HW-06-通信收发器.md ｜ HW-07-传感器冗余.md ｜ SW-01-软件架构.md ｜ SW-02-任务调度.md ｜ SW-03-通信协议栈.md ｜ SW-04-状态机设计.md ｜ SW-05-标定与诊断.md ｜ SW-06-Bootloader与OTA.md ｜ SW-07-数据记录与上云.md

**建议新增 P 项（顺延编号）**：
- P-28 800 V/PD2/材料组 III 爬电距离查表值（HW-04）
- P-29 GB 18384-2020 绝缘电阻定量要求（Ω/V 级数值与工况判据）（HW-04）
- P-30 预充判据 95%/防抖 3 周期行业惯例出处（HW-05/SW-04）
- P-31 ISO 15765-2 的 N_As/N_Bs/N_Cr 标准超时值与 ISO 14229-1 的 P2/P2* 默认时间（SW-03）
- P-32 RM 充分条件适用性说明与 WCET 静态分析工具清单（SW-02）
- P-33 AUTOSAR CP BSW 资源占用公开基准（SW-01 示意 30 KB RAM/450 KB Flash）
- P-34 ASIL 等级对应的传感器路径诊断覆盖率目标值分档（HW-07）
- P-35 GB 38031 数据记录条款细节（建议并入 P-05 核对范围）（SW-07）
- P-36 经典 CAN 节点数上限惯例与 CAN FD 整车速率档位（HW-06，与 P-18 同源）
- P-37 分流器温漂/霍尔零偏温漂/AFE 精度档位器件典型值（HW-01/03/06）

**建议新增来源（候选）**：IEC 60664-1（绝缘配合，A）、ISO 15765-2（DoCAN，A）、ISO 24089:2023（软件更新工程，A）、OSEK/VDX OS 2.2.3 与 Liu & Layland 1973 / Joseph & Pandya 1986（调度经典，A/B）、Miro Samek《Practical UML Statecharts in C/C++》（B）、Joseph Yiu《The Definitive Guide to ARM Cortex-M3/M4》（B）、Uptane 与 OpenBLT（B）、MQTT 5.0 OASIS 与 Mosquitto/EMQX（B）、TI bq769xx / NXP MC3377x AFE 产品文档（A，厂商官方）

## 批次 A3：HV + CHG（✅ 已完成，11 课）

**产出文件**（knowledge/lessons/，81~100 行，零 URL——无编造链接）：
HV-01-HVIL高压互锁.md ｜ HV-02-预充电路.md ｜ HV-03-绝缘监测.md ｜ HV-04-粘连检测.md ｜ HV-05-上下电时序.md ｜ CHG-01-充电接口.md ｜ CHG-02-充电通信协议.md ｜ CHG-03-析锂抑制.md ｜ CHG-04-充电安全.md ｜ CHG-05-即插即充.md ｜ CHG-06-充电末端控制.md

**建议新增 P 项（顺延编号）**：
- P-38 GB 18384-2020 中 HVIL/互锁条款、绝缘电阻限值（100 Ω/V DC / 500 Ω/V AC）准确条款号与工况表述（HV-01/03/04/05）
- P-39 60 V DC 人体安全限值在 GB 18384-2020 的准确表述与切断后时限要求（HV-05）
- P-40 GB/T 20234.3 现行载流档位（250 A 档与液冷扩展）及 ChaoJi 关系（CHG-01/02）
- P-41 GB/T 27930 各报文标准周期/超时值（CHM 250 ms、BCL 50 ms 等按示意处理）与 GB/T 18487.1 桩车绝缘检测时序（CHG-02/04，可与 P-06 合并）
- P-42 ISO 15118-20 与 -2 兼容性、证书更新报文名称、合同证书有效期惯例（CHG-05）
- P-43 电压弛豫判析锂阈值文献与"SOH 修正倍率地图"公开文献（CHG-03/06）
- P-44 数字式 HVIL 芯片方案、脉冲功率电阻降额规格、主动放电 ~100 ms 性能数据出处（HV-01/02/05）

**建议新增来源（候选）**：ISO 6469-3（电气安全，A）、GB/T 18487.1 与 IEC 61851-1（充电系统框架，A）、SAE J1939（27930 报文体系基础，A/B）、openV2G / Libre Solar BMS / EVerest（开源项目，延伸补链候选）

## 批次 A4：THM + FLT（✅ 已完成，11 课）

**产出文件**（knowledge/lessons/，92~110 行，结构脚本校验通过）：
THM-01-温度布点.md ｜ THM-02-电池热模型.md ｜ THM-03-整车热联动.md ｜ THM-04-低温加热.md ｜ THM-05-热失控预警.md ｜ FLT-01-故障分级.md ｜ FLT-02-DTC与冻结帧.md ｜ FLT-03-降级策略.md ｜ FLT-04-断高压与安全态.md ｜ FLT-05-售后归属判定.md ｜ FLT-06-远程诊断.md

**建议新增 P 项（顺延编号）**：
- P-45 GB/T 38661-2020 温度采集条款具体数值（量程/精度/采样周期）（THM-01/02）
- P-46 GB/T 38661-2020 故障处理与降级条款（等级划分/动作要求）（FLT-01/03）
- P-47 GB/T 38661-2020 诊断与故障存储条款（FLT-02）
- P-48 GB/T 38661-2020 BMS-整车热接口条款（THM-03）
- P-49 GB 18384-2020 绝缘电阻要求数值与条款号（100 Ω/V DC 量级待核实）（FLT-04，与 P-38 同源可合并）
- P-50 GB 38031"热失控报警提前 5 分钟"原文表述（并入 P-05）（THM-05）
- P-51 T1/T2/T3 热失控特征温度文献区间（80~120 / 120~200 / 600~1000 °C 示意）（THM-05）
- P-52 熵热项低倍率占比与低温内阻倍数文献值（THM-02/04）
- P-53 脉冲自加热速率公开文献区间（3 K/min 为示意推演）（THM-04）
- P-54 云端诊断提升诊断率的定量证据（FLT-06）
- P-55 行业售后"责任矩阵"公开化程度与 OTA 归因占比数据（FLT-05）
- P-56 Feng 热失控综述准确卷期页码/DOI（THM-05）

**建议新增来源（候选）**：X. Feng et al., "Thermal runaway mechanism of lithium ion battery for electric vehicles: A review", *Energy Storage Materials*, 2018（A，登记后补 DOI）；COVESA VSS / Eclipse KUKSA / Uptane（B）；PyBaMM（B，开源）

## 批次 A5：DEV + CHM（✅ 已完成，11 课）

**产出文件**（knowledge/lessons/，80~98 行，结构程序化校验通过、无 URL）：
DEV-01-V模型.md ｜ DEV-02-验证阶梯.md ｜ DEV-03-HIL台架.md ｜ DEV-04-合规测试.md ｜ DEV-05-标定与耐久.md ｜ DEV-06-场景库与数据闭环.md ｜ DEV-07-AI验证体系.md ｜ CHM-01-锂电体系差异.md ｜ CHM-02-钠电适配.md ｜ CHM-03-固态电池适配.md ｜ CHM-04-梯次利用.md

**建议新增 P 项（顺延编号）**：
- P-57 钠电池相关国标/行标编号与制定进度；钠电正极路线电压窗口、OCV 滞回幅度、低温析钠机理文献（CHM-02）
- P-58 固态：半固态装车可靠报道、硫化物工作温度窗口、固-固界面阻抗量级、堆叠压力是否进量产 BMS 传感清单、H₂S 车规条款（CHM-03）
- P-59 梯次："70~80% 退役线"惯例出处、GB/T 34015 系列部分号、梯次典型倍率与均衡电流（CHM-04）
- P-60 ISO 26262-6 覆盖率推荐表与 -8 TCL 条款原文；量产 HIL 步长/通道典型值；标定矩阵行业统计；耐久路试里程；CLTC 标准编号；LFP 容量"台阶"现象文献（DEV 多课）
- P-61 CHM-01 滞回幅度"数十 mV 量级"的文献支撑（可与 P-14 合并核对）

**建议新增来源（候选）**：《汽车数据安全管理若干规定（试行）》（DEV-06 数据合规，A）、ASAM MDF/ASAP2（A2L）格式规范（A/B）、Janek & Zeier Nature Energy 固态综述（A，卷期需核实）、梯次利用综述/白皮书（B）、三体系参数横向对比综述（A）

## 批次 A6：ARCH + GEN 跨域层（✅ 已完成，8 课）

**产出文件**（knowledge/lessons/，90~99 行，每课含对比表、无编造 URL）：
ARCH-C-集中式架构.md ｜ ARCH-MS-主从式架构.md ｜ ARCH-D-分布式架构.md ｜ ARCH-W-无线BMS.md ｜ ARCH-CE-云边协同.md ｜ GEN-1-传统车载BMS.md ｜ GEN-2-云端辅助BMS.md ｜ GEN-3-数字孪生BMS.md

**建议新增 P 项（顺延编号）**：
- P-62 AFE 单芯片通道数（12~18 常见）与典型从板串数配置的规格书出处（ARCH-C/MS）
- P-63 "大多数量产 BMS 是主从式"的统计口径来源（ARCH-MS）
- P-64 "乘用车小容量包仍有集中式量产"的车型实例（ARCH-C）
- P-65 乘用车纯对等分布式量产案例是否存在（ARCH-D）
- P-66 TI wBMS"线束减少约 90%"类厂商数值的一手出处（ARCH-W，S-18 备注）
- P-67 上云上传频次（30 s 级）的行业公开资料（ARCH-CE）
- P-68 《汽车数据安全管理若干规定（试行）》适用条款与云边架构对应关系（GEN-2，与 A5 建议同源）

**建议新增来源（候选）**：GB/T 32960 系列《电动汽车远程服务与管理系统技术规范》（A，现行版本需核对）、Davide Andrea《Battery Management Systems for Large Lithium-Ion Battery Packs》（Artech House, 2010，B）

## 批次 A7：ALG 剩余（✅ 已完成，7 课）

**产出文件**（knowledge/lessons/，90~110 行，无任何 URL——全部名称+[待补链]）：
ALG-03-数据驱动SOC.md ｜ ALG-04-电极级SOC.md ｜ ALG-06-SOP功率估计.md ｜ ALG-07-均衡策略.md ｜ ALG-08-故障诊断算法.md ｜ ALG-09-RUL预测.md ｜ ALG-11-电化学模型.md

**建议新增 P 项（顺延编号）**：
- P-69 GB/T 38661-2020 SOP 与均衡功能条款数值（ALG-06/07，与 P-13 同路径）
- P-70 量产被动均衡电流典型区间与标定惯例（ALG-07）
- P-71 N/P 比 1.05~1.15 设计区间与石墨固相扩散系数 1e-14 m²/s 量级文献（ALG-04/11）
- P-72 内短路等效电阻分级阈值与量产筛查判据（ALG-08）
- P-73 "EV 容量 80%=EOL"惯例的标准/质保条款出处；LFP 膝点定量文献（ALG-09）
- （另：AABC 2026 会后增量已有 P-04 承载，2026-12-16 前回填 ALG-04/ALG-06）

**建议新增来源（候选）**：Severson et al., *Nature Energy* 2019（数据驱动循环寿命里程碑，A）；Doyle/Fuller/Newman 1993 *J. Electrochem. Soc.*（P2D 原始文献，A）；TI cell balancing 应用手册（准确编号待查）；dQ/dV 电极健康诊断综述、内短路早期检测综述（B）

---

## 汇总（2026-11-04）

- 7 个批次全部完成：**73 门新课程 + 4 门精写课 = 77 门，77/77 节点全覆盖**
- 批次顺序：A1 SYS+SAFE(11) → A2 HW+SW(14) → A3 HV+CHG(11) → A4 THM+FLT(11) → A5 DEV+CHM(11) → A6 ARCH+GEN(8) → A7 ALG(7)
- 各批均自检：9 项结构、行数区间、S/P 编号不越界、无编造 URL、手算数字标"教学示意值"
- P-16~P-74 与候选来源已并入 meta（主理 Agent 执行）
