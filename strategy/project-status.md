# DINWEYS Battery — Project Status

> 最后更新：2026-09-06 03:30 · 状态：内容生产 + SEO/AIO/EEAT + Pillar-Cluster 全部完成，主站扩展至 19 页（含行业应用 + 区域市场页），作者已升级为具名 Martin Wong，待部署 + 真实案例（内容无缺口，待用户决策部署/案例/外链）

## 当前状态

**内容生产线已圆满收官**。知识库 46 页 + 主站 19 页，原创度 ~75%，竞争力护城河成型（竞品全无的 AIO 全套 + JSON-LD 全链路 + 原创计算 + 选型工具 + 双指标画像）。

## 完成里程碑（按时间）

| 阶段 | 内容 | commit |
|---|---|---|
| Phase 0 | 主站 Astro 11 页 + 子站 MkDocs 脚手架 | 主站 9cd56ec / 子站 2060799 |
| 内容对齐工厂站 | 6 项认证 + 真实产品线（JIS+DIN 双主力，BCI 按需） | 主站 92f1077 / 子站 57588e2 |
| Phase 1 | P0 5 篇 + P1 20 篇长尾 | 主站 4b93a56 / 子站 5ee0c5c |
| Phase 2 | 5 应用场景页 + 产品页互链 | 主站 6bd676e / 子站 563f44b |
| 一致性修复 | 清 BCI 导向 + DIN H8/H9 + 补 llms.txt/robots.txt/About | 主站 cd77c59 / 子站 4ef339f |
| SEO/AIO/EEAT 强化 | 31 篇权威外链 + FAQ 补齐 | 主站 25b699e / 子站 f52b79c |
| 内容广度+深度 | +7 篇广度 + 产品页 intro 正文 | 主站 5a7d081 / 子站 4746ed8 |
| 原创计算资产 | JIS vs DIN 密度分析 + CCA 气候余量 | 子站 86665dc |
| 跨源验证+中文源 | JIS −15°C 修正 + YUASA 公式 + GB 映射 + MF | 子站 48aea41 |
| CCA vs RC 双指标 | JIS Pb-Sb 双强画像 + 车队趋势 | 子站 7d45207 |
| Pillar-Cluster 架构 | 5 pillar hub 化 + 选型工具静态矩阵 | 主站 d7ba31c / 子站 aec3162 |
| 主站扩展 + EEAT 作者 | 主站 11→19 页（4 行业应用 + 4 区域市场）+ 具名 Martin Wong | 主站 87d4969 / 子站 6ef7c6f |

## 最终数据

- **知识库**：46 页面、163 JSON-LD 块全有效（35 FAQPage）、0 死链、内链 0 警告，8-pillar 簇群架构
- **主站**：19 页（home + 5 产品 + 选型工具 + about/contact + 2 法律页 + 4 行业应用页 + 4 区域市场页）、83 JSON-LD 块全有效、build 0 error
- **作者署名**：具名 Martin Wong (Sales Director, 14 年经验) 替换匿名 Technical Team（EEAT 强化）
- **原创度**：~75%（原创计算 + 跨源验证 + 中文源综合 + 反商品化对比表齐备）

## Pillar-Cluster 结构（5 Pillar）

1. **Battery Fundamentals** — `complete-guide`（11 篇簇群）
2. **Standards & Sizing** — `jis-vs-din-vs-bci`（8 篇）
3. **Selection & Buying** — `selection-guide`（7 篇）
4. **Maintenance & Life** — `how-to-maintain-truck-battery`（8 篇）
5. **Applications & Fleets** — `fleet-battery-management`（7 篇）

规划文档：`docs/pillar-cluster-strategy.md`

## 待办（"后面补充"清单）

1. **真实客户案例**（Experience 维度唯一硬缺口）——等真实反馈，模板已备
   `docs/testimonial-collection-templates.md`（WhatsApp + 邮件两版）
2. **Cloudflare Pages 部署**——用户手动 push + 连接（源码已可打包发货）
3. **行业目录外链**——需用户决策（BCI 等协会付费会员/人工注册，性价比存疑）
4. 后续可选：hreflang 多语言、更多中文源采购情报层

## 关键实体信息（真实，来自 Chengguang 工厂档案）

- **品牌**：Dinweys（鼎威）
- **母公司/工厂**：Chengguang Power Tech Co., Ltd.（陈光能源，since 2002）
- **地址**：Lvjiaying Village, Mayu Industrial Park, Jinzhou City, Shijiazhuang, Hebei, China
- **邮箱**：martin@dinweys.com · **WhatsApp**：+86 13323237275
- **规模**：200,000 m² · 18 线 · 40,000 只/天 · 1,000+ 员工 · 70+ 国家 · MOQ 1×20ft · 交期 20-45 天
- **认证 6 项**（已确认）：IATF 16949 / ISO 9001:2015 / ISO 14001:2015 / ISO 45001:2018 / OHSAS 18001 / CE

## 真实产品线（不可写错）

| 标准 | 型号 | 容量 | CCA | 尺寸 (mm) |
|---|---|---|---|---|
| JIS | 145G51 (N150) | 135Ah | 900A | 508×222×212 |
| JIS | 190H52 (N200) | 200Ah | 1100A | 520×278×220 |
| DIN | 58827 (DIN88) | 88Ah | 800A EN | 353×175×190 |
| DIN | 60038 (DIN100) | 100Ah | 870A EN | 393×175×190 |

- BCI Group 31/8D 按需（**非主打**）
- 禁止 DIN H8/H9 表述；JIS+DIN 双主力市场平等权重

## 域名 + 仓库

- 主站：`dinweysbattery.com` → `martinxionbiotech-max/dinweysbattery`（Astro）
- 子站：`docs.dinweysbattery.com` → `martinxionbiotech-max/data-dinweysbattery`（MkDocs）
- 工作目录：主站 `/home/ubuntu/.openclaw/workspace/dinweysbattery/site`，子站 `.../knowledge`
- push 脚本：`/tmp/dinwey-push.sh`（远程 OpenCode token，不持久化）

## 关键方法论文档

- `MASTER-PROMPT.md` — 生产总控提示词
- `WRITING_QUEUE.md` — 选题队列
- `docs/pillar-cluster-strategy.md` — Pillar-Cluster 规划
- `docs/testimonial-collection-templates.md` — 客户反馈模板
- `docs/daily-log.md` — 日志

## 夜间 cron

- dinweysbattery 05:00 Asia/Shanghai（跳过真实案例，只做自动打磨：内链/sitemap/JSON-LD 复核）
- Tavily web_search 已配好（`tvly-dev-*`），后续项目可用
