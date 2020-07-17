#!/usr/bin/env python3
from forex_python.converter import CurrencyRates

c = CurrencyRates()
print('--------------------')
currency = input('Currency [USD]: ')
tocurrency = input('Convert to [JPY]: ')
startingValue = input('How much [1]: ')
if startingValue == '':
    startingValue = float(1)
else:
    startingValue = float(startingValue)

if currency == '':
    startingUnit = "USD"
else:
    startingUnit = str.upper(currency)

if tocurrency == '':
    convertUnit = "JPY"
else:
    convertUnit = str.upper(tocurrency)
print('--------------------')

fxrate = c.get_rate(startingUnit , convertUnit)
convertedMath = round(startingValue * fxrate, 2)

print(convertedMath)