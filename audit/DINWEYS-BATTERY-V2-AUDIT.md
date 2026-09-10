# DINWEYS Battery V2.0 — Full Site Audit

> 生成日期：2026-09-07 · 审计范围：dinweysbattery.com + docs.dinweysbattery.com
> 依据：DINWEYS Battery V2.0 Prompt（SEO + AIO + EEAT + Knowledge Graph Optimization）
> 原则：**只审计，不改站**（PHASE 1）

---

## 1. Executive Summary

DINWEYS 已从"普通中国电池工厂站"升级为一套**内容成熟的双站体系**：主站 19 页（Astro 5）+ 知识库 46 页（MkDocs Material），技术 SEO 基础扎实（robots.txt 放行全部 AI 爬虫、sitemap、canonical、组织/商品/FAQ/Article 全套 JSON-LD、具名作者 Martin Wong）。

但对照 V2.0 的终极目标——**Truck Battery OEM & Fitment Intelligence Platform**——当前存在一个**结构性缺口**：

> 现有内容是「**知识**」（What is CCA / JIS vs DIN / 选型指南），但缺少「**数据/实体关系**」（Battery Master DB / Vehicle Fitment / Cross-Reference / 车型适配页）。

这正是 V2.0 Prompt 反复强调的护城河：**Real Factory + Real Product Data + Real Vehicle Fitment + Real Cross-Reference**。当前护城河是「反商品化的知识原创（~75%）」，尚缺「结构化的数据实体层」。

**结论**：技术 SEO + 内容质量已达 P2-P3 阶段的高水平；真正需要新增的是 **PHASE 2-8 的数据层与实体关系层**（Battery DB → Vehicle DB → Fitment → Cross-Reference → 实体页），而非继续堆文章。

---

## 2. Current Score vs Target Score

| 维度 | 当前 | 目标 | 差距 |
|---|---|---|---|
| Technical SEO | 85 | 95 | hreflang 缺失、无 Data/DefinedTerm/HowTo schema |
| Content Quality | 80 | 90 | 知识深度够，缺数据实体页 |
| **Battery Data Layer** | **15** | 90 | **无 battery-master.json、无独立型号实体页** |
| **Vehicle/Fitment Layer** | **0** | 85 | **无 vehicle-master.json、无 /vehicle-fitment/** |
| **Cross-Reference** | **10** | 80 | **仅散落在文章里，无结构化 DB** |
| EEAT | 70 | 85 | 具名作者已做，缺 Technical Team 页/Reviewer 体系/Factory Evidence |
| AIO Readiness | 75 | 90 | Direct Answer/FAQ 齐全，缺 DefinedTerm/Dataset schema |
| Internal Linking | 70 | 85 | 有互链，但未表达实体关系（Hino→JIS→N150 链） |
| Tools | 40 | 80 | 仅 Selection Tool 静态版，缺 Cross-Reference/24V Calculator 等 |

---

## 3. Biggest Risks（最大风险）

1. **🔴 无结构化数据层** —— 一旦竞品（Songli/Tianneng/Ritar）跟进 fitment/cross-reference 页面，DINWEYS 的"反商品化知识"优势会被数据层反超。这是最大的时间窗口风险。
2. **🟠 车型适配 = 法律/信任风险** —— V2.0 Prompt 明确要求：无法验证的适配**必须写 "Potential battery configuration — verify before replacement"**。若过早推 fitment 页而无真实数据，反而伤 EEAT。
3. **🟠 本地代码 vs 线上仓储历史分叉** —— 之前 local site 落后 19 commits 的分叉事故，需持续用 `git status` 守护（现已对齐 87d4969 / 6ef7c6f）。
4. **🟡 磁盘 92%（3.1G 余）** —— 后续 build/node_modules/数据文件可能触发空间压力。

---

## 4. Biggest Opportunities（最大机会）

1. **💰 Battery Master DB + 独立型号实体页**（PHASE 3+7）—— 目前只有 JIS/DIN **分类产品页**，没有 `/batteries/jis/n150/` 这种**单型号实体页**。单型号页能捕获 "145G51"、"190H52"、"58827" 等**精确型号长尾**，是信息增益最高、竞品最缺的。
2. **💰 Vehicle Fitment 高价值车型**（PHASE 8/12）—— Hino 500 / Isuzu F 系列 / Volvo FH 等 15 个卡车品牌的高商业价值车型适配页，直接命中 "Hino 500 battery" 这类交易型长尾。
3. **💰 Cross-Reference 工具**（PHASE 6/11）—— 结构化 "JIS↔DIN↔BCI↔OEM" 换算（严格区分 Exact/Approximate），是 B2B 买家刚需、竞品几乎空白。
4. **💰 Factory Evidence + Technical Team 页**（PHASE 13）—— 真实工厂照片 + 具名工程师团队，是 EEAT 的最后一块拼图。

---

## 5. Existing Assets（现有资产盘点）

### 主站（dinweysbattery.com，Astro 5，19 页）
| 类别 | 页面 | 状态 |
|---|---|---|
| Home | `/` | 完整 hero + 产品范围 + FAQ + 知识库链接 |
| 产品页 | `/products/jis-heavy-duty/` `/din-heavy-duty/` `/bci-request/` `/24v/` `/fleet/` | 5 页，含 Product+FAQ+Breadcrumb schema |
| 工具 | `/selection-tool/` | 静态选型矩阵 + WebApplication schema（⚠️ 有 `Offer` schema 需核验真实性） |
| 场景 | `/applications/bus-coach/` `/cold-chain-refrigerated/` `/diesel-generator/` `/mining-off-highway/` | 4 页 |
| 市场 | `/markets/africa/` `/latin-america/` `/middle-east/` `/southeast-asia/` | 4 页（⚠️ 内容深度待核验，疑似偏薄） |
| 其他 | `/about/` `/contact/` `/privacy-policy/` `/terms-and-conditions/` | 4 页 |

### 知识库（docs.dinweysbattery.com，MkDocs，46 页）
- 5 大 Pillar：Fundamentals / Standards / Selection / Maintenance / Applications
- 44 篇指南 + index + about，全部带 Article/TechArticle + FAQPage + BreadcrumbList schema
- 原创计算资产：CCA 气候余量、JIS vs DIN 密度、CCA vs RC 双指标

### 技术资产（已具备）
- ✅ robots.txt 放行 GPTBot/ClaudeBot/PerplexityBot/Google-Extended 等 10+ AI 爬虫
- ✅ sitemap.xml / sitemap-index.xml（主站）+ sitemap.xml（子站）
- ✅ self-canonical 全部正确
- ✅ llms.txt（主站 45 链接 = 44 文档页 + about）
- ✅ Organization schema（含 6 项认证 hasCredential + 实体信息）
- ✅ 具名作者 Martin Wong（Sales Director，14 年）

---

## 6. Content Gaps（内容缺口）

| 缺口 | 说明 | 优先级 |
|---|---|---|
| 产品型号实体页 | 无 `/batteries/jis/n150/` 单型号页（只有分类页） | P0 |
| Vehicle Fitment 页 | 无 `/vehicle-fitment/hino/` 等 | P0 |
| Cross-Reference 结构化页 | 无独立的换算表页/工具 | P1 |
| Market 页深度 | 4 个市场页内容偏薄，缺 climate/fleet brands/replacement cycle/local term | P1 |
| OEM Process 详解 | `/fleet/` 与 OEM 流程未完全展开（MOQ/Lead Time/Packaging/Sample/QC 步骤） | P1 |

---

## 7. Product Gaps（产品缺口）

现主站产品页是**分类页**（JIS / DIN / BCI / 24V / Fleet），缺**单型号实体页**。真实产品线（来自工厂档案，已验证）：

| 标准 | 型号 | 容量 | CCA | 尺寸 | 现状 |
|---|---|---|---|---|---|
| JIS | 145G51 (N150) | 135Ah | 900A | 508×222×212 | ❌ 无独立页 |
| JIS | 190H52 (N200) | 200Ah | 1100A | 520×278×220 | ❌ 无独立页 |
| DIN | 58827 (DIN88) | 88Ah | 800A EN | 353×175×190 | ❌ 无独立页 |
| DIN | 60038 (DIN100) | 100Ah | 870A EN | 393×175×190 | ❌ 无独立页 |
| BCI | Group 31/8D | — | — | — | ❌ 无独立页（按需） |

---

## 8. Vehicle Gaps（车型缺口）

**完全空白**。无 vehicle-master.json，无任何 fitment 页。

需优先建立高商业价值车型（V2.0 Prompt 指定品牌）：
- Hino（500/700）、Isuzu（F/GIGA）、Mitsubishi Fuso（Fighter/Super Great）
- Mercedes-Benz（Actros/Atego）、Volvo（FH/FM）、Scania（R/G/P）
- MAN（TGS/TGX）、DAF（XF）、Iveco（Stralis）、Renault Trucks（T）
- UD Trucks（Quon）、Tata、Ashok Leyland

---

## 9. Data Gaps（数据缺口）

| 数据库 | 状态 | 说明 |
|---|---|---|
| `data/batteries/battery-master.json` | ❌ 未建 | 无结构化电池实体 |
| `data/vehicles/vehicle-master.json` | ❌ 未建 | 无结构化车型实体 |
| `data/fitment/fitment.json` | ❌ 未建 | 无车型↔电池映射 |
| Cross-Reference 表 | ❌ 未建 | JIS↔DIN↔BCI 换算仅在文章文字里 |

---

## 10. EEAT Gaps

| 项 | 状态 |
|---|---|
| 具名作者 Martin Wong | ✅ 已做（P0 完成） |
| `/about/technical-team/` 页面 | ❌ 缺（V2.0 要求，且**禁止虚构**，需真实团队信息） |
| Author/Reviewer 体系 | ❌ 缺 Reviewer 字段 |
| Factory Evidence（真实工厂照片） | ❌ 缺 |
| Source 系统（source/date/confidence） | ⚠️ 部分（文章有来源，但无统一 confidence 字段） |

---

## 11. AIO Gaps

| 项 | 状态 |
|---|---|
| Direct Answer 结构 | ✅ 大部分文章有 TL;DR + 提问式 H2 |
| FAQPage schema | ✅ 163 块 JSON-LD 有效（35 FAQPage） |
| DefinedTerm schema | ❌ 缺（CCA/Ah/RC 等术语未标记） |
| Dataset schema | ❌ 缺（将来 battery-master 数据可挂） |
| llms.txt | ✅ 已做 |

---

## 12. Technical SEO Issues

| Issue | 严重度 | 说明 |
|---|---|---|
| hreflang 缺失 | 🟡 Low | 单语言现阶段可接受，多语言时才需要 |
| `selection-tool` 的 `Offer` schema | 🟠 需核验 | 需确认是否有价格信息，若虚假需删（V2.0 规则：不伪造评分/价格） |
| 无 Data/DefinedTerm/HowTo schema | 🟡 Low | 增强项 |
| 内链未表达实体关系 | 🟠 中期 | 当前是"相关文章"式互链，非 Hino→JIS→N150 实体链 |

---

## 13. Programmatic SEO Risks（程序化 SEO 风险）

当前**没有**程序化 SEO 垃圾页（✅ 好）。但未来建立 fitment/车型页时，必须严守 V2.0 规则：

- 每个可索引车型页必须 ≥10 项真实内容（车型识别/电气系统/电池配置/规格/适配证据/DINWEYS 推荐/兼容警告/来源/关联电池/关联指南）
- **只有 brand/model 变化、数据为空** → **NOINDEX**
- 无法验证的适配 → 写 "Potential battery configuration — verify before replacement"

---

## 14. Internal Linking Problems

当前内链是「知识库 ↔ 主站产品页」的**内容型互链**（合格），但缺**实体关系型内链**：

```
现状：产品页 → 知识库指南（"Read complete guide"）
目标：Hino 500 → JIS → N150 → 24V → CCA → Selection → OEM
```

需在建立实体页后，构建实体关系链。

---

## 15. Schema Problems

| 项 | 状态 | 建议 |
|---|---|---|
| Organization + WebSite + Product + Article + FAQPage + BreadcrumbList | ✅ 已全有 | 保持 |
| `selection-tool` 的 `Offer` | 🟠 核查 | 无真实价格则移除 Offer |
| DefinedTerm | ❌ 缺 | CCA/Ah/RC/Group Size 等术语加 DefinedTerm |
| Dataset | ❌ 缺 | battery-master.json 上线后挂 Dataset |
| Person | ⚠️ 有但少 | 主站首页无 author Person schema（知识库有） |

---

## 16. Competitor Gaps（竞品缺口分析）

竞品（Songli/Tianneng/Ritar/等卡车电池厂）普遍状态：
- 全是"领先制造商"自嗨文案，无 fitment 数据
- 无 cross-reference 工具
- 无车辆适配页
- 无 AIO 结构（Direct Answer/FAQ schema）

**DINWEYS 的差异化机会**（V2.0 护城河）：
1. 精确型号实体页（145G51/190H52/58827/60038）—— 竞品零覆盖
2. Vehicle Fitment 高价值车型（Hino 500/Volvo FH 等）
3. Cross-Reference 结构化表（严格 Exact/Approximate）
4. 工厂证据 + 真实产品数据（含 source/confidence）

---

## 17. Recommended Architecture（推荐架构）

```
dinweysbattery.com（主站）
├── /                                    # 首页（重新优化第一屏 Who/What/CTA）
├── /products/jis-heavy-duty/            # 分类页（保留 + 深链到型号页）
├── /products/din-heavy-duty/
├── /products/bci-request/
├── /products/24v/
├── /products/fleet/
├── /batteries/                          # 🆕 电池实体总览
│   ├── /batteries/jis/n150/             # 🆕 单型号实体页
│   ├── /batteries/jis/n200/
│   ├── /batteries/din/din88/
│   └── /batteries/din/din100/
├── /vehicle-fitment/                    # 🆕 车型适配（高价值车型）
│   ├── /vehicle-fitment/hino/
│   ├── /vehicle-fitment/volvo/
│   └── /vehicle-fitment/hino/500/       # 🆕 具体车型（需足量真实数据）
├── /cross-reference/                    # 🆕 换算工具
├── /oem/                                # 🆕 OEM 独立页（从 fleet 拆出）
├── /about/technical-team/              # 🆕 技术团队（真实数据）
├── /selection-tool/                     # 保留 + 升级
└── /contact/

docs.dinweysbattery.com（知识库）       # 重构为 Knowledge Base 7 大分区
├── 01 Battery Fundamentals
├── 02 Battery Standards
├── 03 Battery Technology
├── 04 Vehicle Applications
├── 05 Fitment
├── 06 OEM
└── 07 Buying Guide
```

---

## 18. Priority Matrix（优先级矩阵）

### P0（立即，护城河核心）
1. **Battery Master DB**（`data/batteries/battery-master.json`）—— 4 个真实型号 + null 填充未知
2. **单型号实体页**（`/batteries/jis/n150/` 等 4-5 页）
3. **Vehicle Master DB 骨架**（15 品牌，先高价值车型）
4. **Cross-Reference 结构化表**（严格 Exact/Approximate）

### P1（数据层扩展）
5. Vehicle Fitment 高价值车型页（Hino 500 等，先 3-5 个有把握的）
6. `/cross-reference/` 工具页
7. Market 页内容深化（climate/fleet/local term/replacement cycle）
8. `/oem/` 独立页 + OEM Process 详解

### P2（EEAT + AIO 增强）
9. `/about/technical-team/`（**真实团队信息，禁止虚构**）
10. Factory Evidence（真实工厂照片）
11. DefinedTerm/Dataset schema
12. Reviewer 体系

### P3（优化）
13. 首页第一屏重优化（Who/What/CTA）
14. 内链实体化重构
15. 多语言（Arabic/Spanish 等，需真实搜索需求验证）

---

## 19. 第一阶段执行结论

**本阶段（PHASE 1）只做审计，已完成**：
- ✅ 爬取两站全部页面
- ✅ 建立 URL Inventory（`audit/url-inventory.csv`，主站 19 + 知识库核心 6 页首版）
- ✅ 建立站点架构图
- ✅ 提取现有电池规格
- ✅ 审计 Schema / 内链 / EEAT / AIO / 技术 SEO
- ✅ 产出本报告 `audit/DINWEYS-BATTERY-V2-AUDIT.md`

**下一阶段（PHASE 2-3）**：建立 Entity Model + Battery Master DB，需等待你确认是否继续，并**提供关键真实数据**（见下）。

---

## 20. 需要用户提供/确认的真实数据（严禁编造）

在进入 PHASE 3+（数据层）之前，以下数据**必须由用户/工厂提供**，否则按规则全部填 `null`：

1. **车型适配数据**：Hino 500 / Isuzu 等车型的实际电池配置（几块电池/电压/标准/组号），从 OEM 手册或工厂适配表获取
2. **技术团队真实信息**：Technical Director / Battery Engineer / Quality Manager 等真实姓名+职位+经验（建 `/about/technical-team/` 用）
3. **工厂照片**：生产线/组装/化成/测试/仓库/装车/包装的真实照片（禁止 AI 生成）
4. **OEM 细节**：真实 MOQ / Lead Time / 样品流程 / 包装规格（若当前内容里已有按此，无则补）
5. **认证证书**：IATF 16949 等 6 项证书文件（可选，放 Factory Evidence）

**已确认可放心的真实数据**（来自工厂档案，无需再问）：
- 产品线 4 型号规格（N150/N200/DIN88/DIN100）
- 工厂规模（200,000 m² / 18 线 / 40,000 只/天 / 1000+ 员工 / 70+ 国家）
- 认证 6 项（IATF 16949 等）
- 联系人 Martin Wong（Sales Director）

---

*报告结束。等待用户决策：是否进入 PHASE 2（Entity Model + Battery Master DB）。*
