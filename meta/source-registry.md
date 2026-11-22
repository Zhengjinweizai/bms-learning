# 来源登记表（Source Registry）

> 所有 A/B 级来源登记于此，供知识图谱节点以 S 编号引用。新增来源追加编号，不重排。

| S 编号 | 来源 | 类型 | 级别 | 登记日期 | 备注 |
|---|---|---|---|---|---|
| S-01 | GB 38031-2025《电动汽车用动力蓄电池安全要求》（替代 GB 38031-2020，2026-07-01 实施） | 标准（国标） | A | 2026-11-04 | 2026-11-16 条款要点核实（媒体汇总级，条款号待原文）：热扩散 2 小时观察期不起火不爆炸 + 监测点 ≤60 ℃ + 5 分钟内报警；新增底部撞击、300 次快充循环后短路（P-05/P-24/P-50 关闭） |
| S-02 | GB 38031-2020《电动汽车用动力蓄电池安全要求》 | 标准（国标） | A | 2026-11-04 | 已被 S-01 替代，保留用于对照 |
| S-03 | GB/T 38661-2020《电动汽车用电池管理系统技术条件》（openstd：hcno=DB3ACC49AC4A146FAA311BB468ACA290） | 标准（国标） | A | 2026-11-04 | 2026-11-15 核实：§5.5 BEV/PHEV SOC 累积误差 ≤5%（P-13 关闭）；HEV 限值待原文 |
| S-04 | GB 18384-2020《电动汽车安全要求》（§5.1.4.1：直流 ≥100 Ω/V、交流 ≥500 Ω/V + 强制绝缘监测报警，2026-11-15 核实；原文 PDF 副本见 sae-hk.org） | 标准（国标） | A | 2026-11-04 | 含绝缘电阻等整车安全要求（P-29/P-38 关闭） |
| S-05 | GB/T 27930-2023《非车载传导式充电机与电动汽车之间的数字通信协议》（现行版；openstd：hcno=6ECF725CD2BCCA2819082279F6B2E243） | 标准（国标） | A | 2026-11-04 | 2026-11-15 核实：现行版本为 2023 版（P-06 关闭）；报文周期 CHM/BHM 250ms、BCL 50ms、BCS/CCS 250ms（P-41 关闭） |
| S-06 | GB/T 20234.1~.3《电动汽车传导充电用连接装置》系列；**20234.3-2023（2023-09-07 发布即实施）：直流 800A/1500V、300~800A 档位、液冷接口** | 标准（国标） | A | 2026-11-04 | 2026-11-15 核实 2023 版要点（P-40 关闭） |
| S-07 | ISO 26262:2018《道路车辆 功能安全》 | 标准（国际） | A | 2026-11-04 | 第二版 |
| S-08 | ISO/SAE 21434:2021《道路车辆 网络安全工程》 | 标准（国际） | A | 2026-11-04 | — |
| S-09 | ISO 14229-1《统一诊断服务（UDS）》 | 标准（国际） | A | 2026-11-04 | — |
| S-10 | ISO 15118 系列《道路车辆 网络与应用协议》（含 Plug & Charge） | 标准（国际） | A | 2026-11-04 | — |
| S-11 | ISO 11898 系列（CAN / CAN FD） | 标准（国际） | A | 2026-11-04 | — |
| S-12 | ISO 17987（LIN） | 标准（国际） | A | 2026-11-04 | — |
| S-13 | UN R100（电动汽车蓄电池安全型式认证） | 法规（UN ECE） | A | 2026-11-04 | — |
| S-14 | UN R155（网络安全管理体系 CSMS） | 法规（UN ECE） | A | 2026-11-04 | — |
| S-15 | UN R156（软件升级管理体系 SWUP） | 法规（UN ECE） | A | 2026-11-04 | — |
| S-16 | G. Plett, *Battery Management Systems, Volume I: Battery Modeling* & *Volume II: Equivalent-Circuit Methods*, Artech House, 2015 | 专著 | B | 2026-11-04 | SOC/SOP 估计方法论体系 |
| S-17 | G. L. Plett, "Extended Kalman filtering for battery management systems of LiPB-based HEV battery packs" (Parts 1–3), *Journal of Power Sources* 134 (2004): 252–261 / 262–276 / 277–292 | 期刊论文（同行评议） | A | 2026-11-04 | Part 3 DOI 10.1016/j.jpowsour.2004.02.033；Part 1/2 PII S0378775304003593 / S037877530400360X；Parts 1/2 有作者自托管免费 PDF（mocha-java.uccs.edu，课程内已链接） |
| S-18 | TI 无线 BMS 官方资料（应用笔记 SSZT336、演示视频、产品页，ti.com） | 厂商官方 | B | 2026-11-04 | **2026-11-06 更正**：TI 于 2021-01 发布自家 wBMS（S-63）；GM Ultium 无线 BMS 实为 ADI 方案，与 TI 无关（P-66 关闭，90% 口径一手来源 → P-75） |
| S-19 | T/CAAMTB《电动汽车用电池管理系统设计规范》 | 标准（团标） | A | 2026-11-04 | 标准编号与年份待核对（P-01） |
| S-20 | LG Energy Solution BaaS 服务页群（lgensol.com/business/：B-Lifecare / B.around / B.once / KooRoo） | 厂商官方 | B | 2026-11-04 | 2026-11-10 核实（P-03 关闭）：B.once 2025-10~11 上线（5 分钟 SOH/SOC 快诊）、KooRoo 覆盖梯次利用 |
| S-21 | SAE 技术论文 2026-26-0382《Transforming Battery Management: Role of AI/ML and Digital Twin Technologies》 | 会议论文（SAE） | A | 2026-11-04 | 全文获取待办（P-11），可能付费墙 |
| S-22 | "Digital twin technologies for battery systems", Frontiers in Batteries and Electrochemistry, DOI 10.3389/fbael.2026.1764210 | 期刊论文（同行评议） | A | 2026-11-04 | 2026 年发表 |
| S-23 | "AI and Digital Twin Technologies for Intelligent BMS", MDPI《Batteries》, 编号 11/8/298 | 期刊论文（同行评议） | A | 2026-11-04 | 卷期/年份待核对；引用时注意 MDPI 期刊声誉争议 |
| S-24 | CATL 官网新闻：TENER Sodium 钠离子储能系统（catl.com/en/news/6861.html） | 厂商官方新闻稿 | B | 2026-11-04 | 2026-11-10 完整核实（P-10 关闭）：2026-06-22 慕尼黑发布；BMS 用斜坡电压曲线做 SOC 估计 + 过充 SOC 容忍度 +20%（BMS 安全裕度）；储能场景 |
| S-25 | EU InnoBMS 项目页（CORDIS 101137975），"situationally aware BMS" | 官方项目描述 | B | 2026-11-04 | 项目范围与伙伴待核实（P-09） |
| S-26 | INL《FreedomCAR Battery Test Manual》(2014)，inldigitallibrary.inl.gov/sites/sti/sti/6308373.pdf | 国家实验室公开技术手册 | A | 2026-11-04 | HPPC 测试权威程序，公开 PDF |
| S-27 | INL《Battery Test Manual for Plug-In Hybrid Electric Vehicles》(2010)，inldigitallibrary.inl.gov/sites/sti/sti/4655291.pdf | 国家实验室公开技术手册 | A | 2026-11-04 | 公开 PDF |
| S-28 | K. Yang et al., "Battery State of Health Estimate Strategies: From Data Acquisition to Machine Learning", *Batteries* 9(7):351, 2023，mdpi.com/2313-0105/9/7/351 | 期刊综述（开放获取） | A | 2026-11-04 | SOH 估计策略全景 |
| S-29 | X. Lei et al., SOH/RUL 文献计量综述，*Green Energy & Environment*, 2024，sciencedirect.com/science/article/pii/S2095756424001193 | 期刊综述（开放获取） | A | 2026-11-04 | 方法谱系梳理 |
| S-30 | MathWorks "Understanding Kalman Filters" 视频系列（电池 SOC 贯穿案例），mathworks.com/videos | 厂商官方教程 | B | 2026-11-04 | 免费，滤波直觉入门 |
| S-31 | R. Labbe, *Kalman and Bayesian Filters in Python*（开源在线书），github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python | 开源图书 | B | 2026-11-04 | 免费，Jupyter 可运行 |
| S-32 | CalCE Battery Data（马里兰大学公开电池数据集），calce.umd.edu/battery-data | 公开数据集 | B | 2026-11-04 | 循环/存储/动态工况数据 |
| S-33 | NASA PCoE Li-ion Battery Aging Datasets，data.nasa.gov | 公开数据集 | B | 2026-11-04 | SOH/RUL 研究标准数据源 |
| S-34 | TI 应用手册 SLUA364 / SLUA450 / SLYT402（Impedance Track 算法与 LFP 调优），ti.com/lit | 厂商官方技术文档 | A | 2026-11-04 | 量产电量计算法的官方实现文档 |
| S-35 | Battery University BU-903 "How to Measure State-of-charge"，batteryuniversity.com | 厂商教育站 | B | 2026-11-04 | 入门直觉用，不作事实层引用 |
| S-36 | ISO 21448:2022《道路车辆 预期功能安全（SOTIF）》 | 标准（国际） | A | 2026-11-04 | SAFE-02/06 引用 |
| S-37 | IEC 61508《电气/电子/可编程电子安全系统的功能安全》 | 标准（国际） | A | 2026-11-04 | 功能安全母标准 |
| S-38 | IEC 60664-1《低压系统内设备的绝缘配合》 | 标准（国际） | A | 2026-11-04 | HW-04 爬电/电气间隙方法 |
| S-39 | ISO 15765-2（DoCAN，诊断通信传输层） | 标准（国际） | A | 2026-11-04 | SW-03 引用 |
| S-40 | ISO 24089:2023《道路车辆 软件更新工程》 | 标准（国际） | A | 2026-11-04 | SW-06 引用 |
| S-41 | ISO 6469-3《电动汽车安全规范 第 3 部分：电气安全》 | 标准（国际） | A | 2026-11-04 | HV 域方法框架 |
| S-42 | GB/T 18487.1《电动汽车传导充电系统 第 1 部分》 | 标准（国标） | A | 2026-11-04 | 现行版本待核对 |
| S-43 | IEC 61851-1《电动汽车传导充电系统》 | 标准（国际） | A | 2026-11-04 | CHG 域框架 |
| S-44 | GB/T 32960 系列《电动汽车远程服务与管理系统技术规范》 | 标准（国标） | A | 2026-11-04 | 现行版本年份待核对 |
| S-45 | 《汽车数据安全管理若干规定（试行）》 | 法规（中国） | A | 2026-11-04 | 数据合规（DEV-06/GEN-2）；条款细节待核对（P-68） |
| S-46 | X. Feng et al., "Thermal runaway mechanism of lithium ion battery for electric vehicles: A review", *Energy Storage Materials*, 2018 | 期刊综述（同行评议） | A | 2026-11-04 | 卷期/DOI 待补（P-56） |
| S-47 | K. A. Severson et al., "Data-driven prediction of battery cycle life before capacity degradation", *Nature Energy*, 2019 | 期刊论文（同行评议） | A | 2026-11-04 | 卷期/DOI 待补 |
| S-48 | M. Doyle / T. F. Fuller / J. Newman, "Modeling of Galvanostatic Charge and Discharge of the Lithium/Polymer/Insertion Cell", *J. Electrochem. Soc.*, 1993 | 期刊论文（同行评议） | A | 2026-11-04 | P2D 原始文献；卷期待补 |
| S-49 | D. Andrea, *Battery Management Systems for Large Lithium-Ion Battery Packs*, Artech House, 2010 | 专著 | B | 2026-11-04 | 架构分类经典教材 |
| S-50 | ASAM MDF / ASAP2（A2L）数据与标定格式规范 | 行业规范 | A | 2026-11-04 | DEV-05/06 工具链 |
| S-51 | PyBaMM（Python Battery Mathematical Modelling，开源项目） | 开源软件 | B | 2026-11-04 | ALG-11/THM-02 动手练习 |
| S-52 | TI bq769xx / NXP MC3377x AFE 产品文档（ti.com / nxp.com） | 厂商官方技术文档 | A | 2026-11-04 | HW-01 器件参考（具体文档号待补） |
| S-53 | NEMO 项目（NExt-generation MOdels for advanced battery electronics），CORDIS 101102944 / nemoproject.eu | 官方项目描述 | B | 2026-11-05 | 已核实（P-08 关闭）；成果见 S-55 |
| S-54 | NEXTBMS 项目（nextbms.eu，NEMO 姐妹项目） | 官方项目描述 | B | 2026-11-05 | 细节待核 |
| S-55 | TU Graz 2026-06 NEMO"智能 BMS for EV"成果新闻（tugraz.at；electrive 2026-06-18；EurekAlert） | 大学官方新闻/权威媒体 | B | 2026-11-05 | [项目成果宣称] 非同行评议，引用技术细节前等论文 |
| S-56 | 2026 世界储能大会官方报道（新华网 2026-10-15；福建工信厅 2026-10-13；CNESA 活动页） | 权威媒体/主办方 | B | 2026-11-05 | 高特电子 BMS 数值为厂商口径（见 S-58） |
| S-57 | AABC US 2026 官网与 Battery Engineering 专场页（advancedautobat.com，Cambridge EnerTech） | 会议官网 | B | 2026-11-05 | 议程 PDF 待读（P-04） |
| S-58 | CNESA 高特电子 1500V 芯片级双向主动均衡 BMS 活动页 | 厂商宣称（活动页） | B | 2026-11-05 | 利益关联：宣称数值未经同行评议，仅作线索 |
| S-59 | TI bq769x2 应用文档（sluaa81/sluaa84，3~16 串）；NXP MC33771B 产品页（14 通道）；ADI ADBMS181x 产品页（18 通道） | 厂商官方产品文档 | A | 2026-11-06 | AFE 通道数核实（P-62 关闭），HW-01 已引用 |
| S-60 | UNECE UN R155 官方文本（R155e.pdf，unece.org） | 法规原文 | A | 2026-11-06 | 生效时间线核实（P-25 关闭）：新车型 2022-07 / 所有新产车辆 2024-07；SAFE-05/ARCH-W 已引用 |
| S-61 | AUTOSAR RS_Diagnostics（R20-11，autosar.org） | 行业规范文档 | A | 2026-11-06 | 0x29 Authentication 要求核实（P-26 关闭）；SAFE-05 已引用 |
| S-62 | InnoBMS 项目页群（CORDIS 101137975 / innobms.eu / 成员页：TU Graz、CIDETEC、VUB、Univ. Ljubljana、Potenza、Typhoon HIL） | 官方项目描述 | B | 2026-11-06 | P-09 关闭；+12%/+33% 为项目目标宣称；radar/conferences/innobms-project.md |
| S-63 | Assembly Magazine《TI unveils wireless battery management system》（2021-01）与 Electronic Design wBMS 文章群 | 行业媒体 | B | 2026-11-06 | wBMS 供应商归属核实的转述源 |
| S-64 | GM×ADI Ultium wBMS 发布报道：Forbes（2020-09-09）、Electronic Design（2020-09-21）、T&D World（2020-11-05） | 行业媒体（转述 GM/ADI 官方发布） | B | 2026-11-10 | "线束减约 90% / 省 15% 包体积"宣称的追溯源头（P-75 关闭）；ARCH-W 与矩阵已引用 |
| S-65 | LG Energy Solution 二手电池诊断软件获 CES 2027 创新奖——**官方新闻稿已定位**：news.lgensol.com/company-news/press-releases/5575，产品名 **Pulse**（二次生命电池评估定位） | 厂商官方新闻稿 | A | 2026-11-10 | 2026-11-18 升级：从媒体转述升级为一手来源（诊断 7h→10min） |
| S-66 | GB/T 47136-2026《纯电动汽车动力蓄电池健康与安全状态评估规范》（openstd.samr.gov.cn，hcno=F493E6BDCF7210EB024E71C0BE1BA911） | 标准（国标） | A | 2026-11-13 | 首个电池健康与安全状态评估国标，2026-05-01 实施（P-79 关闭）；ALG-05/矩阵维度 1 已引用 |
| S-67 | Microvast BMS 5.0 时间线（IR 新闻稿：2022-09-19 首发；2024-09 IAA 发布 ISO 26262 ASIL-C + ISO/SAE 21434:2021；2024-10-23 获 ASIL-C 功能安全产品认证） | 厂商官方新闻稿 | B | 2026-11-13 | P-76 关闭（日期与认证性质核实：第三方产品认证）；矩阵待第 2 独立来源 |
| S-68 | Infineon 高压 BMS 参考设计（2026-10-27，热失控前兆早期检测；infineon.com） | 厂商官方 | A | 2026-11-13 | 具体页面 URL 待补链 |
| S-69 | ISO 26262 公开转述源（分解规则：Infineon 知识库 community.infineon.com；覆盖率方法表：Ferrocene public-docs / Parasoft / Rapita） | 厂商知识库/工具文档 | B | 2026-11-13 | P-20/P-22 核实的转述源（最终以标准原文为准） |
| S-70 | arXiv 2603.21592《Battery health reporting fails independent validation》（2026-03） | 预印本论文 | B | 2026-11-14 | ALG-05 候选延伸资源；"低里程≠更健康" |
| S-72 | Li et al., "Interfacial engineering to achieve an energy density of over 200 Wh kg⁻¹ in sodium batteries", *Nature Energy* 7, 511–519 (2022) | 期刊论文（同行评议） | A | 2026-11-16 | "200 Wh/kg 无负极钠电池"里程碑（537 引用）；DOI 待补 |
| S-73 | 无负极（零过剩）钠电池新论文：~1400 循环保持 80%、−40 ℃ 可工作，*Nature Energy*（2026-11 上旬报道） | 期刊论文（同行评议） | A | 2026-11-16 | DOI/标题待补（radar/2026-11-16 #2）；报道未确认 200 Wh/kg 口径 |
| S-74 | European Commission《Cyber Resilience Act》官方页面（digital-strategy.ec.europa.eu） | 法规（EU）/官方口径 | A | 2026-11-17 | 2024-12-10 生效 / 2026-09-11 报告义务 / 2027-12-11 全面适用（P-84 关闭）；SAFE-05 已引用 |
| S-75 | CATL 专利 WO2023092416A1《动力电池充电的方法和电池管理系统》（Google Patents） | 专利文件 | A | 2026-11-17 | 充电控制周期性获取模式；矩阵 CATL 行证据之一 |
| S-76 | 虎嗅《6 万字长文剖析宁德时代（一）：核心技术》——"恒电位闭环控制算法"（充电末端防析锂）口径 | 权威技术媒体深度 | B | 2026-11-17 | 矩阵 CATL 行证据之二；原"多尺度参量耦合算法"表述未获证实（P-02 修正留档） |
| S-77 | GB/T 43568-2026《电动汽车用固态电池 第 1 部分：术语和分类》（2026-07-01 实施；全球首个车用固态电池国标） | 标准（国标） | A | 2026-11-17 | P-83 大部分关闭；openstd 原文待核对；系列性能/安全/寿命部分待发布 |
| S-78 | Federal Register（2026-06-24）：CPSC 拟议微型出行锂电池安全标准 NPR——**含 BMS 要求与反极性测试** | 法规（美国）拟议文本 | A | 2026-11-18 | federalregister.gov/documents/2026/06/24/2026-12749；11-17 雷达条目升级为一手依据 |
| S-79 | GB/T 39086-2020《电动汽车用电池管理系统功能安全要求及试验方法》 | 标准（国标） | A | 2026-11-18 | **2026-11-18 新发现**：BMS 功能安全专属国标；SAFE-01 已引用；条款细节待核 |
| S-80 | GB/T 34015-2017《车用动力电池回收利用 余能检测》及系列（34015.2 拆卸 / 34015.4-2021 标识；openstd：hcno=A62FD663BD4648CC1C026D8AEBCEE762） | 标准（国标） | A | 2026-11-18 | P-59 关闭（系列核实）；"80% 退役线"仍为综述共识口径；CHM-04 已引用 |
| S-81 | AUTOSAR SWS CAN TransportLayer（R21-11，autosar.org） | 行业规范文档 | A | 2026-11-19 | N_As/N_Bs/N_Cr 形式化定义（P-31 关闭）；SW-03 已引用 |
| S-82 | X. Feng, M. Ouyang et al., "Thermal runaway mechanism of lithium ion battery for electric vehicles: A review", *Energy Storage Materials* Vol. 10 (2018) 246–267，**DOI 10.1016/j.ensm.2017.05.003**（5100+ 引用） | 期刊综述（同行评议） | A | 2026-11-19 | P-51/P-56 关闭：T1 自产热 ~90–130 ℃ / T2 热失控触发 ~130–200 ℃ / T3 最高 >500–850 ℃；THM-05 已引用 |
| S-83 | GB/T 46991.1-2025《电动汽车车载动力电池耐久性要求及试验 第 1 部分》（2026-07-01 实施） | 标准（国标） | A | 2026-11-21 | **SOCE（可用能量状态）统一耐久性评估**：5 年/10 万公里 SOCE ≥82%；强制向消费者披露 SOCE 与虚拟里程（P-80 关闭）；ALG-05/矩阵维度 1 已引用 |
| S-84 | D. Urishov et al.（Aalto University + VTT），"A cloud based Digital Twin architecture for battery management systems with edge integration and advanced sensing"，*Internet of Things*（Elsevier），2026，PII S2666546826001850（开放获取） | 期刊论文（同行评议） | A | 2026-11-21 | P-77 关闭；GEN-3/ARCH-CE 候选证据；注意勿与同组 Energy and AI vol.25 论文混淆 |
| S-85 | Moment Energy Nova 二次生命 BESS：**首个同时获 UL 1973 + UL 9540 认证**的第二生命储能系统（2026-11-17 发布，200/500 kW 级 C&I，AI BMS） | 厂商发布/行业媒体 | B | 2026-11-21 | CHM-04 认证范本（环境+能源领袖报道，原稿待补） |
| S-86 | "End-of-life or second-life options for retired EV batteries"（ScienceDirect，PII S2666386421002484）——80%=EOL 退役口径 | 期刊文章 | B | 2026-11-21 | P-74 关闭（与 GB/T 34015 系列、综述共识互证）；CHM-04 已引用 |
| S-87 | EU Horizon ENERGETIC 项目（Next Generation Battery Management System，CORDIS 101103667），含"混合 AI 数字孪生 BMS"工作包 | 官方项目描述 | B | 2026-11-22 | P-81 关闭；EU 下一代 BMS 观察组合第五项 |
| S-88 | 钠电储能国标群：GB/T 44265-2024《电力储能电站钠离子电池技术规范》/ GB/T 48072-2026《…安全技术规范》（2027-03-01 实施）/ GB/T 48098-2026《…技术规范》（含术语，2027-03-01 实施） | 标准（国标） | A | 2026-11-22 | P-57 关闭：储能侧落地、车用动力钠电专门国标推进中；CHM-02 已引用 |
| S-89 | 内短路（ISC）检测文献群：Shen et al., *Applied Energy* (2025) SCR 度量与分级（PII S0306261925015272）/ Naha et al., *Scientific Reports* (2020) 实时 ML 检测 / Jia et al., PHM Society (2023) BMS 集成早期检测 | 期刊论文/会议论文（同行评议） | A | 2026-11-22 | P-73 部分关闭：硬 <10~20 mΩ / 软 >1 kΩ 文献口径；量产筛查判据仍待企业标准 |

## 使用规则

- 知识图谱节点通过 S 编号引用；引用时若该来源的"备注"含待核对项，节点表述需保留不确定性。
- C 级来源不登记于此，只出现在 `meta/pending-verification.md` 或 `radar/leads/`。
