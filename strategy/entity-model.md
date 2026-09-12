# DINWEYS Battery — Entity Model (实体模型)

> 依据：DINWEYS Battery V2.0 Prompt PHASE 2
> 目的：从「关键词模型」升级为「实体关系模型」（Entity Graph），为 Knowledge Graph + AIO + Cross-Reference 打基础。
> 原则：所有实体必须可追溯到真实来源；无法验证的字段填 `null`，绝不猜测。

---

## 1. 实体层级（Entity Hierarchy）

```
Brand (品牌)
  └── DINWEYS
Company (公司)
  └── Chengguang Power Tech Co., Ltd. (陈光能源)
Factory (工厂)
  └── 河北石家庄晋州 Mayu 工业园
Battery (电池实体)          ← PHASE 3 建立
  └── JIS N150 / N200 · DIN88 / DIN100 · BCI G31/8D
Standard (标准)              ← 已有知识库覆盖
  └── JIS / DIN / EN / BCI / SAE / IEC / GB
Specification (规格)
  └── CCA / Ah / RC / Voltage / Dimensions / Terminal
Vehicle (车型)              ← PHASE 4 建立
  └── Hino / Isuzu / Fuso / Volvo / Scania / MAN / DAF / Iveco ...
Fitment (适配)              ← PHASE 5 建立
  └── Vehicle → OEM Battery → Standard → DINWEYS 推荐
Market (市场)               ← 已有 4 页，待深化
  └── Middle East / Africa / Europe / Latin America / SEA
Application (应用)
  └── Truck / Bus / Mining / Generator / Cold-Chain / Semi-Trailer
OEM (代工)
  └── OEM / Private Label / MOQ / QC / Certification
```

---

## 2. 核心实体定义

### 2.1 Brand — DINWEYS
| 字段 | 值 | 来源 |
|---|---|---|
| name | DINWEYS | 全站 |
| alternateName | 鼎威 | 工厂档案 |
| parentCompany | Chengguang Power Tech Co., Ltd. | llms.txt / Organization schema |
| category | Truck & heavy-duty starting batteries | 定位 |

### 2.2 Company — Chengguang Power Tech Co., Ltd.
| 字段 | 值 | confidence |
|---|---|---|
| name | Chengguang Power Tech Co., Ltd. | HIGH |
| legalName | 待确认（需工厂营业执照核实） | — |
| foundingDate | 2002 | HIGH |
| address | Lvjiaying Village, Mayu Industrial Park, Jinzhou City, Shijiazhuang, Hebei, China | HIGH |
| facility | 200,000 m² / 18 lines | HIGH |
| export | 70+ countries | MEDIUM |
| certification | IATF 16949 / ISO 9001 / ISO 14001 / ISO 45001 / OHSAS 18001 / CE | HIGH |
| contact | martin@dinweys.com / WhatsApp +86 13323237275 | HIGH |

### 2.3 Battery（详见 `data/batteries/battery-master.json`）
真实产品线 4 型号 + BCI 按需。

### 2.4 Standard（标准实体）
- **JIS**（Japanese Industrial Standard）：145G51 / 190H52 等 5-6 位型号编码
- **DIN/EN**（欧洲）：58827 / 60038 等 5 位型号编码，EN 冷启动电流
- **BCI**（北美）：Group 31 / 8D / 4D
- **SAE J537**：CCA 测试标准（−18°C/30s）
- **GB**（中国）：与 JIS 有映射关系（知识库已有 `china-gb-vs-jis`）

### 2.5 Spec（规格实体，术语）
- CCA（Cold Cranking Amps）、CA、RC（Reserve Capacity，分钟）、Ah（安时）、Voltage、Group Size、Terminal、Polarity、Dimensions（L×W×H mm）

### 2.6 Vehicle（详见 `data/vehicles/vehicle-master.json`）
15 个卡车品牌，先建高商业价值车型。

### 2.7 Fitment（详见 `data/fitment/fitment.json`）
Vehicle → OEM Battery → Standard → DINWEYS 推荐 → Reason → Confidence → Source。

---

## 3. 实体关系（Entity Relations）

```
Hino 500 ──has──> 24V system ──consistsOf──> 2 × 12V battery
Hino 500 ──uses──> JIS standard ──mapsTo──> N150 / N200
N150 ──isA──> Heavy-duty starting battery
N150 ──hasSpec──> 135Ah / 900A CCA / 508×222×212mm
DINWEYS ──manufactures──> N150 (at Chengguang factory)
N150 ──fits──> Hino 500 (confidence: MEDIUM — verify spec)
JIS ──crossRef──> DIN / BCI (Exact vs Approximate)
```

内链必须表达这些关系（V2.0 第二十六条），而非随机 "related articles"。

---

## 4. Confidence / Source 规范

所有数据字段尽量附带三元组：

| confidence | 含义 | 示例 |
|---|---|---|
| HIGH | 官方数据手册/标准/OEM 手册/工厂档案 | N150 规格 |
| MEDIUM | 专业来源/行业共识，需二次验证 | 某车型适用标准 |
| LOW | 社区/推测，禁止用于强断言 | — |

字段：`source` / `source_date` / `verified_date` / `confidence`。

---

## 5. 与知识库的关系

- 知识库（docs）＝「知识层」：What/Why/How 原理、对比、选型方法
- 数据层（data/）=「实体层」：Battery/Vehicle/Fitment/Cross-Reference 的可机读事实
- 主站实体页＝「数据层的前台呈现」：单型号页、fitment 页、cross-reference 工具

三层相互引用：知识库引用数据 → 数据页内链知识库 → 主站实体页内链两者。

---

*本文件为 PHASE 2 交付物。PHASE 3 将据此填充 `data/batteries/battery-master.json`。*
