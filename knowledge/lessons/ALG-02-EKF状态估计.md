# 课程 ALG-02：用 EKF 把模型变成 SOC 估计器

> 对应节点 `ALG-02`（[../domains/06-核心算法.md](../domains/06-核心算法.md)）｜ 前置：[ALG-01](ALG-01-安时积分与OCV校正.md)、[ALG-10](ALG-10-等效电路模型与参数辨识.md) ｜ 预计用时 60~90 min（本课程包最硬的一课）

## 1. 问题重述

安时积分会漂（ALG-01），OCV 校正要等静置（停车过夜）。**能不能边开车边校正？**

能。思路：把电池模型当成"虚拟传感器"。模型说端电压应该是 3.700 V，实测是 3.690 V——这 10 mV 的差意味着我对内部状态的假设有错，用差值反向修正 SOC。这就是**观测器**；工程上最常用的是 EKF（Extended Kalman Filter，扩展卡尔曼滤波）。

## 2. 状态空间形式

把 ALG-10 的 2RC 模型写成状态空间：

- **状态** x = [SOC, U1, U2]ᵀ，**输入** u = I，**输出** y = 端电压 U_t
- 状态方程：SOC 速率 = ηI/C；极化电压按 RC 微分方程演化
- 输出方程：y = OCV(SOC) − I·R0 − U1 − U2 + v（v 为测量噪声）
- **非线性来源**：OCV(SOC) 是曲线不是直线 → 用 EKF：每个采样点在工作点做线性化，再套卡尔曼融合。

## 3. EKF 的机制直觉（先懂再推公式）

每个采样周期三步：

1. **预测**：用模型把状态推进一拍；同时把误差协方差 P 推进一拍——P 表示"我对自己估计有多不确定"。电流积分的漂移会**累积进 P**：越久没用电压观测修正，P 越大。
2. **增益**：K = P·Cᵀ / (C·P·Cᵀ + R)。直觉：K 是"这一拍听测量的比例"，由两个信任度决定——模型不确定性 P 越大 → 越信测量；测量噪声 R 越大 → 越不信测量。
3. **修正**：x ← x + K × (把电压差翻译成状态差的量)。

### 数值直觉示例（全部为教学示意值）

工况：NCM 电芯，估计 SOC=52%；该点 dOCV/dSOC = 2 mV/%；模型预测端电压 3.700 V，实测 3.690 V。

- 电压差 = −10 mV。若**完全信测量**：ΔSOC = −10 / 2 = −5% → 修正到 47%；
- 当前协方差 P 折算后取 K = 0.3（表示"三分信测量、七分信模型"）：
  SOC ← 52% + 0.3 × (−5%) = **50.5%**

注意 K 每拍自动变化：长时间无校正 → P 大 → K 自动变大 → 测量话语权上升。这正是"自适应校正"的实现方式，不需要人工开关。

## 4. 调 Q/R：算法工程师的日常

- **Q（过程噪声）**：等效于"我多信任电流积分"。Q 大 → 跟随快、但对电流噪声敏感；
- **R（测量噪声）**：电压采集噪声 + 模型失配。R 大 → 平滑但迟钝。

实车调参 = 在低温/高倍率/静置恢复等不同工况下平衡两者。常见工程手法：Q 随 |I| 自适应放大（大电流时积分误差更值得怀疑）。（工程实践观点，框架依据 S-17）

## 5. LFP 的残酷现实：可观测性崩塌

EKF 的修正能力正比于 **dOCV/dSOC**（输出方程对 SOC 的雅可比）。

LFP 平台段该值 ≈ 0 → 实测电压再准也翻译不出 SOC 差 → K → 0 → **退化回纯安时积分**（漂移照旧累积，只是不再被修正）。

量产对策（工程实践观察）：

1. **端点锚定**：满充/接近放空处 OCV 斜率大，抓住这两端做强校正；
2. **滞回建模**：把充放电 OCV 差作为附加状态，减少模型失配；
3. 弱校正机会的谨慎利用（平台段轻微修正，防发散）。

这也解释了市场上"LFP 车建议每周/每两周充满一次"的实践——本质是给 EKF 制造锚点机会。（表述为工程实践观点；具体厂商官方手册依据待核对 → P-15）

## 6. 进阶路线图

- **SPKF/UKF**：用 sigma 点采样代替雅可比，处理强非线性（框架见 S-16）；
- **联合估计 / 双 EKF**：SOC 与容量/内阻参数同时估计（Plett GLB 框架核心贡献，S-17）——这打通到 `ALG-05`（SOH 在线化）；
- **eSOC（`ALG-04`）**：把估计对象从"电池 SOC"深入到"每个电极的 SOC"，校正老化导致的电极平衡偏移——AABC 2026 Battery Engineering 专场主题（P-04 待核对，见 [../../radar/conferences/aabc-2026.md](../../radar/conferences/aabc-2026.md)）。

## 7. 自测

**Q1**：EKF 为什么要额外维护协方差 P，而不是只维护状态 x？
**Q2**：某一拍"实测电压 − 模型预测电压 = 0"，这一拍 EKF 还做什么？
**Q3**：为什么同一段代码，低温下 K 的表现会变化？

<details><summary>答案</summary>

- Q1：K 由 P（和 R）算出，P 是"该不该信这拍测量"的依据；没有 P 就退化成固定增益，失去自适应能力。
- Q2：预测步照做（状态推进 + P 推进），测量修正项为零——不做修正，但仍为下一拍积累不确定性。
- Q3：低温下 R0/极化参数变化、电压采集有效噪声假设变化 → 模型失配进入 R 的有效值、P 的传播系数变化 → K 变。参数三维性（ALG-10 第 5 节）直接作用于滤波器行为。
</details>

## 来源

- S-17：G. L. Plett, "Extended Kalman filtering for battery management systems of LiPB-based HEV battery packs" (Parts 1–3), *Journal of Power Sources* 134 (2004)。Part 3 DOI：10.1016/j.jpowsour.2004.02.033（[ScienceDirect 页面](https://www.sciencedirect.com/science/article/abs/pii/S0378775304003611)）——GLB 框架原始文献
- S-16：G. Plett, *Battery Management Systems* Vol. II（SPKF、联合估计的教材级展开）

## 延伸资源（链接已于 2026-11-04 联网核实）

| 资源 | 级别 | 免费 | 说明 |
|---|---|---|---|
| [Plett 2004 Part 3: State and parameter estimation（DOI 10.1016/j.jpowsour.2004.02.033）](https://www.sciencedirect.com/science/article/abs/pii/S0378775304003611) | A | SD 页面免费、全文付费 | GLB 联合估计框架（SOC+参数双估计）原始文献（*J. Power Sources* 134: 277–292） |
| [MATLAB Tech Talks: Understanding Kalman Filters（视频系列）](https://www.mathworks.com/videos/introduction-to-kalman-filters-with-matlab-1601281664354.html) | B | ✅ | MathWorks 官方系列，**全程用电池 SOC 估计做贯穿案例**；怕公式先看这个 |
| [rlabbe《Kalman and Bayesian Filters in Python》（开源在线书）](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) | B | ✅ | Jupyter 可运行的免费书，培养滤波直觉的最佳读物（~19k star） |
| [CalCE Battery Data（马里兰大学）](https://calce.umd.edu/battery-data) | B | ✅ | 公开数据集——动手把本课 EKF 在真实数据上复现 |
