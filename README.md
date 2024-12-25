# Python API wrapper for biathlonresults.com

![example workflow](https://github.com/prtkv/biathlonresults/actions/workflows/python-package.yml/badge.svg)

## Installation

```bash
pip install biathlonresults
```

## Examples

### Get WC 2024/2025 stages and races:
```python
import biathlonresults
events = biathlonresults.events("2425", level=biathlonresults.consts.LevelType.BMW_IBU_WC)
for event in events:
    print(event["ShortDescription"], event["StartDate"][:10], "-", event["EndDate"][:10])
    for race in biathlonresults.competitions(event["EventId"]):
        print("   ", race["RaceId"], race["ShortDescription"], race["StartTime"])
# output:
# Kontiolahti 2024-11-27 - 2024-12-08
#     BT2425SWRLCP01MXSR Single Mixed Relay (W+M) 2024-11-30T12:15:00Z
#     BT2425SWRLCP01MXRL Mixed Relay (W+M) 2024-11-30T14:45:00Z
#     BT2425SWRLCP01SMRL Men 4x7.5km Relay 2024-12-01T12:45:00Z
#     BT2425SWRLCP01SWRL Women 4x6km Relay 2024-12-01T16:25:00Z
#     BT2425SWRLCP01SMSI Men 15km Short Individual 2024-12-03T15:20:00Z
#     BT2425SWRLCP01SWSI Women 12.5km Short Individual 2024-12-04T15:20:00Z
# ...
```

### Get race results:
```python
import biathlonresults
race_results = biathlonresults.results(race_id="BT2425SWRLCP01SWSI")
for result in race_results['Results']:
    print(result["Rank"], result["ShortName"], result["Nat"], result["Shootings"], result["TotalTime"] if result["Rank"] == "1" else result["Behind"])
# output:    
# 1 JEANMONNOT L. FRA 0+0+0+0 35:52.3
# 2 HALVARSSON E. SWE 0+1+0+0 +12.3
# 3 OEBERG E. SWE 0+1+1+1 +56.4
# ...
```

### Find athlete:
```python
import biathlonresults
athletes = biathlonresults.athletes(family_name='bo', given_name='jo')
for i in athletes['Athletes']:
    print(i['IBUId'], i['FamilyName'], i['GivenName'])
# output:
# BTNOR11605199301 BOE Johannes Thingnes
# BTNOR11806199901 BOTN Johan-Olav
```

### Get last races of athlete:
```python
import biathlonresults
res = biathlonresults.all_results('BTNOR11605199301')
for i in res['Results']:
    print(i["RaceId"], i['Comp'], i['Season'], i['Place'], i['Rank'])
# output:
# BT2425SWRLCP03SMMS MS 24/25 Annecy 3.
# BT2425SWRLCP03SMPU PU 24/25 Annecy 1.
# BT2425SWRLCP03SMSP SP 24/25 Annecy 2.
# ...
```

### Race analytics:
```python
import biathlonresults
race_course_analytics = biathlonresults.analytic_results("BT2425SWRLCP01SWMS", type_id=biathlonresults.consts.AnalysisType.TOTAL_COURSE_TIME)
for result in race_course_analytics["Results"]:
    print(result["Rank"], result["Name"], result["TotalTime"] if result["Rank"] == "1" else result["Behind"])
# output:
# 1 OEBERG Elvira 31:20.7
# 2 BRAISAZ-BOUCHET Justine +17.0
# 3 PREUSS Franziska +20.1
# ...
```

### World Cup Scores:
```python
import biathlonresults
cups = biathlonresults.cups("2425")
for cup in cups:
    if cup["Level"] == biathlonresults.consts.LevelType.BMW_IBU_WC:
        print(cup["CupId"], cup["Description"])
# output:
# BT2425SWRLCP__SWTS Women's World Cup Total Score
# BT2425SWRLCP__SWSP Women's World Cup Sprint Score
# BT2425SWRLCP__SWPU Women's World Cup Pursuit Score
# ...

total_score_women = biathlonresults.cup_results("BT2425SWRLCP__SWTS")
for row in total_score_women['Rows']:
    print(row["Rank"], row["IBUId"], row["Name"], row["Nat"], row["Score"])
# output:
# 1 BTGER21103199401 PREUSS Franziska GER 565
# 2 BTSWE22602199901 OEBERG Elvira SWE 371
# 3 BTFRA22810199801 JEANMONNOT Lou FRA 352
# ...
```

see more examples [here](examples)

## Donations
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/prtkv)

BTC: bc1qfwe3ysmcklnujhyqfkh7japzyunvpk46h2a8ps

ETH: 0xAc41D8DbD12d96936344806F2a42f83E0Ea4Aad1
