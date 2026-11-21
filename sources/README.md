# sources/ 资料库说明

## 目录约定

- `standards/`：标准与法规笔记（GB/ISO/UN R/SAE/T 团标）
- `papers/`：论文蒸馏笔记
- `official/`：厂商官方技术文档笔记
- `videos/`：视频蒸馏笔记（文件名 `YYYY-MM-DD_讲者_主题.md`）
- `blogs/`：B/C 级线索资料（不得直接进入知识图谱事实层）

## 资料分级（入库必须标注）

- **A 级（规范性）**：标准、法规、厂商官方技术文档、同行评议期刊/会议论文。
- **B 级（解释性）**：权威技术媒体、头部研究机构报告、厂商技术博客。
- **C 级（线索性）**：个人博客、论坛、自媒体。仅作"待验证线索"，不能进入知识图谱事实层。

## 硬规则

1. **"读完再写"**：视频必须基于字幕/文字稿全文蒸馏；无法获取全文 → 标记 `[内容不完整，仅作线索]`，不产出有用内容。
2. 每条笔记末尾必须有：

```
INTAKE_CONFIDENCE: A/B/C | SOURCE_TYPE: paper/standard/video/official/blog | FULL_CONTENT_READ: yes/no
```

3. 来源登记：所有 A/B 级来源需登记到 `meta/source-registry.md`（S 编号），供知识图谱引用。
