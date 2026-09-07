# Nightly Fitment Research Task (夜间 fitment 深挖任务)

> 本文件是给夜间 cron agent 回合的任务说明。isolated session 无对话上下文，请严格按本文件执行。

## 任务目标

为 DINWEY 卡车电池项目（dinweybattery.com）深挖以下 5 个厂商的**商用卡车电池 fitment 证据**，填充 `vehicle-master.json` 中仍为 null 的车型 fitment 字段：

1. **Fuso**（Fighter / Super Great）
2. **Mercedes-Benz**（Actros / Atego）
3. **DAF**（XF）
4. **Iveco**（Stralis）
5. **UD Trucks**（Quon）

## 工作目录

```
/home/ubuntu/.openclaw/workspace/dinweybattery/knowledge/
```

## 数据文件

- 车型骨架：`data/vehicles/vehicle-master.json`（16 车型，7 个已填，9 个仍 null）
- 电池主库：`data/batteries/battery-master.json`
- 交叉引用：`data/batteries/cross-reference.json`
- 日志：`strategy/daily-log.md`

## 已填车型（勿重复处理，可作参考）

| 车型 | 组号 | DINWEY 推荐 |
|---|---|---|
| Hino 700 | N150 | 145G51 |
| MAN TGS/TGX | N150L/N200 | 145G51/190H52 |
| Volvo FM/FH | N150→N200 | 145G51/190H52 |
| Scania R | N150→N200 | 145G51/190H52 |
| Isuzu F | N100L（缺口）| 暂无 |

## 待深挖车型（本次目标，9 个）

- HINO-500 (Hino 500)
- ISUZU-GIGA (Isuzu Giga)
- FUSO-FIGHTER (Fuso Fighter)
- FUSO-SUPER-GREAT (Fuso Super Great)
- MB-ACTROS (Mercedes-Benz Actros)
- MB-ATEGO (Mercedes-Benz Atego)
- DAF-XF (DAF XF)
- IVECO-STRALIS (Iveco Stralis)
- UD-QUON (UD Quon)

## 硬性红线（不可违反）

1. **绝不编造 fitment** —— 只有找到 T1/T2 权威来源（官方 fitment guide、Club Assist、Century、RDP、VARTA/Banner/Exide 等正规厂商 fitment 表）才填。
2. **绝不跨标准 CCA 数值换算**（JIS/EN/SAE/BCI 测量方法不同）。
3. **绝不说 "Fits X" 绝对化表述** —— 一律标 `confidence: MEDIUM/LOW` + 写「industry reference，非 DINWEY 官方 OEM 确认，需按车型规格复核」。
4. **DINWEY 无对应型号时**（如 Isuzu 的 N100L），诚实标注「暂无对应型号，需询价」，绝不硬映射。
5. 字段 `dinwey_recommendation` 只能填 DINWEY 现有 4 个型号之一：145G51(N150)、190H52(N200)、58827(DIN88)、60038(DIN100)。

## 权威来源优先级

- **T1**：厂商官方 fitment 手册、Club Assist / Century / RDP 等专业 fitment guide
- **T2**：VARTA/Banner/Exide/Bosch 等知名电池品牌 fitment 查询结果
- 来源必须标注 `source` + `source_url` + `source_date` + `confidence`

## 执行步骤

1. 用 `tavily_search`（web_search 可能禁用）分别搜索 5 个厂商的 fitment，每组 1-2 个查询
2. 对找到的 fitment guide PDF/页面，用 `tavily_extract` 或 `web_fetch` 提取完整数据
3. 只对**有 T1/T2 证据**的车型，用 Python 脚本填充 `vehicle-master.json` 对应字段
4. 验证 JSON 合法（`python3 -c "import json; json.load(open(...))"`）
5. 追加 `strategy/daily-log.md` 记录（来源 + 日期 + 发现 + 红线遵守情况）
6. git add + commit + push

## 推送方式（关键）

knowledge 仓库：`martinxionbiotech-max/data-dinweybattery`

远程 token 获取方式（一次性，不持久化）：
```bash
TOKEN=$(curl -s --max-time 15 -u "opencode:2034864cs" "http://43.130.37.37:4096/file/content?path=/home/developer/.config/gh/hosts.yml" | python3 -c "import sys,json; d=json.load(sys.stdin); c=d.get('content',''); import re; m=re.search(r'oauth_token:\s*(\S+)', c); print(m.group(1) if m else '')")
git push "https://martinxionbiotech-max:${TOKEN}@github.com/martinxionbiotech-max/data-dinweybattery.git" main:main
```

⚠️ 不要把 token 写入 git config。

## 完成标准

- 至少填充 3-5 个有真实 T1/T2 证据的车型
- 无证据的车型保持 null，并在日志说明
- 每日日志 + commit + push 全部完成
- 最后用简短中文汇报：填了哪几个车型、来源、发现、无证据的有哪些

## 汇报格式（私信给用户）

夜间任务结束后，用中文简洁汇报：
```
🌙 夜间 fitment 深挖完成

新增 fitment 车型 X 个：
- 车型A → 组号 → DINWEY推荐 [来源，置信度]
- ...

仍无 T1 证据：车型C、车型D

commit：<hash>，已推送到 knowledge 仓库
```
