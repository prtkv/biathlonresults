biathlonresults.com API for Python
==================================

Find athlete:
-------------

```python
import biathlonresults
athletes = biathlonresults.athletes('boe')
for i in athletes['Athletes']:
    print(i['IBUId'], i['FamilyName'], i['GivenName'])
# output:
# BTNOR11605199301 BOE Johannes Thingnes
# BTNOR12307197201 BOE Karl Gunnar
# BTNOR12107199801 BOE Magnus
# BTNOR12907198801 BOE Tarjei
# ...
```

Get last races of athlete:
--------------------------

```python
import biathlonresults
res = biathlonresults.all_results('BTNOR11605199301')
for i in res['Results'][:3]:
    print(i['Comp'], i['Season'], i['Place'], i['Rank'])
# output:    
# MS 18/19 Oslo 1.
# PU 18/19 Oslo 1.
# SP 18/19 Oslo 1.
```

Get WC 2019/2020 stages:
------------------------

```python
import biathlonresults
events = biathlonresults.events(1920, 1)
for i in events:
    print(i['StartDate'][:10], i['ShortDescription'])
# output:
# 2019-12-01 Oestersund
# 2019-12-12 Hochfilzen
# 2019-12-16 Annecy-Le Grand Bornand
# 2020-01-06 Oberhof
# 2020-01-13 Ruhpolding
# 2020-01-20 Pokljuka
# 2020-02-12 Antholz-Anterselva
# 2020-03-02 Nove Mesto
# 2020-03-09 Kontiolahti
```