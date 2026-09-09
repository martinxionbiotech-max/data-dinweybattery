#!/usr/bin/env python3
"""Nightly fitment fill - Fuso/MB/DAF/Iveco/UD (T1 Club Assist + T2 corroboration)."""
import json

PATH = "/home/ubuntu/.openclaw/workspace/dinweysbattery/knowledge/data/vehicles/vehicle-master.json"

with open(PATH) as f:
    data = json.load(f)

SOURCE = "Club Assist Commercial Fitment Guide (clubassist.com.au)"
SOURCE_DATE = "2026-09-08"
NOTE_T1 = "Industry reference (T1 third-party fitment guide) — NOT DINWEY official OEM confirmation. Verify against vehicle spec before replacement."

updates = {
    "FUSO-FIGHTER": {
        "battery_standard": "JIS",
        "battery_quantity": 2,
        "battery_group": "N150 (heavy FV/FP/FS class) — light/medium Fighter FK/FM/FN use 55D23R/80D26R",
        "dinwey_recommendation": "145G51 (N150) for heavy Fighter FP/FS/FV variants; light/medium Fighter FK/FM/FN 暂无对应 (需询价)",
        "fitment_evidence": "Club Assist: Fuso FP/FS/FV Series = N150 (SN150x2/HCC150). Fuso Fighter FK1024/FK1424/FM1627/FN2427 = 55D23R/80D26R (small light/medium groups). eBay T2: N150 'Fits Mitsubishi Fighter 400HP/FU/FP/FS'.",
        "compatibility_note": "Fuso Fighter spans light(FK/FM/FN, small 55D23R/80D26R) to heavy(FP/FS/FV, N150) classes. DINWEY 145G51 only matches the heavy N150 variants. Light/medium Fighter groups have no DINWEY match — 需询价.",
        "source": SOURCE,
        "source_date": SOURCE_DATE,
        "confidence": "MEDIUM",
        "oem_battery": "N150 (heavy) / 55D23R·80D26R (light/medium)",
        "generation": "FK/FM/FN (light/medium) / FP/FS/FV (heavy)",
        "battery_dimensions": "N150 class 508x222x212mm (heavy only)"
    },
    "FUSO-SUPER-GREAT": {
        "battery_standard": "JIS",
        "battery_quantity": 2,
        "battery_group": "N150 (heavy Super Great FP/FS/FV class)",
        "dinwey_recommendation": "145G51 (N150)",
        "fitment_evidence": "Club Assist: Fuso FP/FS/FV Series = N150 (SN150x2/HCC150) — Super Great is the heavy FV/FP/FS class. eBay T2: N150 'Fits Mitsubishi FU/FP/FS' (Super Great/Fuso heavy).",
        "compatibility_note": "Super Great is the Fuso heavy-truck (FP/FS/FV) range; Club Assist lists these heavy Fuso series as N150 (2x12V series, 24V system). DINWEY 145G51 matches. Verify tray width/terminal orientation.",
        "source": SOURCE,
        "source_date": SOURCE_DATE,
        "confidence": "LOW",
        "oem_battery": "N150 (JIS)",
        "generation": "FP/FS/FV heavy class",
        "battery_dimensions": "N150 class 508x222x212mm"
    },
    "MB-ACTROS": {
        "battery_standard": "DIN",
        "battery_quantity": 2,
        "battery_group": "N150 (MFN150A) 1996-2013 / N200 (MFN200A) heavy-duty 2014-on",
        "dinwey_recommendation": "145G51 (N150) 1996-2013; 190H52 (N200) heavy-duty option 2014-on",
        "fitment_evidence": "Club Assist: Actros MP1/MP2/MP3 all models 1996-2013 = N150 (MFN150A); Actros 3240/3341/4141 MP4 2014-on = N150 (MFN150A); Actros 2651/2655/2660 & 2643/2646 heavy-duty option 2014-on = N200 (MFN200A); BlueTec 6 2016-on standard = MFN180A.",
        "compatibility_note": "Actros 24V = 2x12V series. Standard fitment N150 (MFN150A, DIN Euro-spec); heavy-duty option N200 (273mm wide); note BlueTec 6 MFN180A is a DIN 180Ah group DINWEY does not stock. DINWEY 145G51/190H52 are JIS-group matches by dimensions.",
        "source": SOURCE,
        "source_date": SOURCE_DATE,
        "confidence": "MEDIUM",
        "oem_battery": "MFN150A (N150) std / MFN200A (N200) H/D / MFN180A BlueTec6",
        "generation": "MP1/MP2/MP3 (1996-2013) / MP4 (2014-on)",
        "year": "1996-on",
        "battery_dimensions": "N150 class 508x222x212mm / N200 class 520x278x220mm"
    },
    "MB-ATEGO": {
        "battery_standard": "DIN",
        "battery_quantity": 2,
        "battery_group": "N150 (MFN150A) standard / N200 (MFN200A) heavy-duty option",
        "dinwey_recommendation": "145G51 (N150) standard; 190H52 (N200) heavy-duty option",
        "fitment_evidence": "Club Assist: Atego 1224/1229/1623-1629/2324-2329 = N150 (MFN150A); Atego heavy-duty option = N200 (MFN200A).",
        "compatibility_note": "Atego (distribution) 24V = 2x12V. Standard N150, heavy-duty option N200. DINWEY 145G51/190H52 are JIS-group matches by dimensions to the MFN150A/MFN200A DIN groups.",
        "source": SOURCE,
        "source_date": SOURCE_DATE,
        "confidence": "MEDIUM",
        "oem_battery": "MFN150A (N150) std / MFN200A (N200) H/D",
        "generation": None,
        "year": None,
        "battery_dimensions": "N150 class 508x222x212mm / N200 class 520x278x220mm"
    },
    "DAF-XF": {
        "battery_standard": "DIN",
        "battery_quantity": 2,
        "battery_group": "N150 (MFN150A) 1997-2013 / N200 (MFN200A) XF105 FAD 8x4 2013-on",
        "dinwey_recommendation": "145G51 (N150) for XF95/XF105 1997-2013; 190H52 (N200) for XF105 FAD 8x4 2013-on",
        "fitment_evidence": "Club Assist: DAF 95 XF 1997-2003 = N150 (MFN150A 4D); XF95-480 = N150; XF105-510 2001-2013 = N150; XF105 FAD 8x4 Rigid 2013-on = N200 (MFN200A).",
        "compatibility_note": "DAF XF 24V = 2x12V. XF95/XF105 standard = N150 (MFN150A DIN); XF105 FAD 8x4 rigid 2013-on = N200. DINWEY 145G51/190H52 are JIS-group matches by dimensions to DIN groups.",
        "source": SOURCE,
        "source_date": SOURCE_DATE,
        "confidence": "MEDIUM",
        "oem_battery": "MFN150A (N150) std / MFN200A (N200) FAD 8x4",
        "generation": "XF95 (1997-2003) / XF105 (2001-on)",
        "year": "1997-on",
        "battery_dimensions": "N150 class 508x222x212mm / N200 class 520x278x220mm"
    },
    "IVECO-STRALIS": {
        "battery_standard": "DIN",
        "battery_quantity": 2,
        "battery_group": "N150 (MFN150A) ATi/460 2002-2013 / N200 (MFN200A) E5 2014-on / HCC27SC (smaller D31 class) AD/AS-L/AT variants",
        "dinwey_recommendation": "145G51 (N150) ATi 360/450 & Stralis 460 2002-2013; 190H52 (N200) E5 2014-on; AD/AS-L/AT variants 暂无对应 (需询价)",
        "fitment_evidence": "Club Assist: Stralis ATi 360/450 2002-2013 = N150 (MFN150A); ATi 360/450 E5 2014-on = N200 (MFN200A); Stralis 460 2002-2013 = N150; Stralis 460 EEV 2014-on = N200; Stralis AD 505/AS-L/AT (2002-on) = HCC27SC (S95D31RHD/27H-750, smaller group).",
        "compatibility_note": "Stralis 24V = 2x12V. ATi/460 line = N150 (2002-13) -> N200 (2014-on E5). AD/AS-L/AT variants use smaller HCC27SC (95D31/D31) group — no DINWEY match, 需询价.",
        "source": SOURCE,
        "source_date": SOURCE_DATE,
        "confidence": "MEDIUM",
        "oem_battery": "MFN150A (N150) / MFN200A (N200) / HCC27SC (D31)",
        "generation": None,
        "year": "2002-on",
        "battery_dimensions": "N150 class 508x222x212mm / N200 class 520x278x220mm"
    },
    "UD-QUON": {
        "battery_standard": "JIS",
        "battery_quantity": 2,
        "battery_group": "N150 (heavy U.D. CK/CW/CWA/GK/GW class)",
        "dinwey_recommendation": "145G51 (N150)",
        "fitment_evidence": "Club Assist: U.D. CK17-380/CW26-380/CWA310/CW385/CW445/GK17-420/GW26-420 = N150 (MF150/HCC150). Battery Brands Warehouse (T2): N150 listed as common fitment for 'UD Quon'. Quon is the U.D. heavy CW/GK/GW class.",
        "compatibility_note": "Quon is U.D. Trucks' heavy range (CW/GK/GW series); Club Assist lists these U.D. heavy models as N150. 24V = 2x12V. DINWEY 145G51 matches. Verify tray before replacement.",
        "source": SOURCE + " + Battery Brands Warehouse (T2)",
        "source_date": SOURCE_DATE,
        "confidence": "LOW",
        "oem_battery": "N150 (JIS)",
        "generation": "CW/GK/GW heavy class",
        "battery_dimensions": "N150 class 508x222x212mm"
    },
}

for vid, patch in updates.items():
    for v in data["vehicles"]:
        if v["vehicle_id"] == vid:
            v.update(patch)
            break

data["meta"]["last_updated"] = SOURCE_DATE
data["meta"]["fitment_source_note"] = (data["meta"].get("fitment_source_note","") +
    " | 2026-09-08 nightly: Fuso/MB/DAF/Iveco/UD fitment added from Club Assist Commercial Fitment Guide (T1).")

with open(PATH, "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Filled:", ", ".join(updates.keys()))
