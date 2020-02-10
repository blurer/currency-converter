#!/usr/bin/env python3

currency = input('Currency [USD]: ')
startingValue = input('How much [1]: ')
if startingValue == '':
    startingValue = float(1)
else:
    startingValue = float(startingValue)

if currency == '':
    startingUnit = "USD"
else:
    startingUnit = str.upper(currency)
print('--------------------')

# usd to other
usd_jpy = 110
usd_php = 50.95
usd_eur = 0.91
usd_aud = 1.5
usd_inr = 71.52
usd_gbp = 0.78

# eur to other
eur_usd = 1.09
eur_jpy = 120.11
eur_gbp = 0.85

# gbp to other
gbp_usd = 1.29
gbp_eur = 1.18
gbp_jpy = 141.47

# jpy to other
jpy_usd = 0.0092
jpy_php = 0.46

# php to other
php_usd = 0.02
php_jpy = 2.15

# inr to other
inr_usd = 0.014 
inr_eur = 0.013
inr_gbp = 0.011

converted_USD_JPY = round(startingValue * usd_jpy, 2)
converted_USD_PHP = round(startingValue * usd_php, 2)
converted_USD_AUD = round(startingValue * usd_aud, 2)
converted_USD_EUR = round(startingValue * usd_eur, 2)
converted_USD_INR = round(startingValue * usd_inr, 2)
converted_USD_GBP = round(startingValue * usd_gbp, 2)
converted_JPY_USD = round(startingValue * jpy_usd, 2)
converted_JPY_PHP = round(startingValue * jpy_php, 2)
converted_PHP_USD = round(startingValue * php_usd, 2)
converted_PHP_JPY = round(startingValue * php_jpy, 2)
converted_EUR_USD = round(startingValue * eur_usd, 2)
converted_EUR_JPY = round(startingValue * eur_jpy, 2)
converted_EUR_GBP = round(startingValue * eur_gbp, 2)
converted_GBP_USD = round(startingValue * gbp_usd, 2)
converted_GBP_JPY = round(startingValue * gbp_jpy, 2)
converted_GBP_EUR = round(startingValue * gbp_eur, 2)
converted_INR_USD = round(startingValue * inr_usd, 2)
converted_INR_EUR = round(startingValue * inr_eur, 2)
converted_INR_GBP = round(startingValue * inr_gbp, 2)



if startingUnit == '':
    print('Error')
elif startingUnit == 'USD':
    print('JPY:', converted_USD_JPY)
    print('PHP:', converted_USD_PHP)
    print('AUD:', converted_USD_AUD)
    print('INR:', converted_USD_INR)
    print('GBP:', converted_USD_GBP)
    print('EUR:', converted_USD_EUR)
elif startingUnit == 'JPY':
    print('USD:', converted_JPY_USD)
    print('PHP:', converted_JPY_PHP)
elif startingUnit == 'PHP':
    print('USD:', converted_PHP_USD)
    print('JPY:', converted_PHP_JPY)
elif startingUnit == 'EUR':
    print('GBP:', converted_EUR_GBP)
    print('JPY:', converted_EUR_JPY)
    print('EUR:', converted_EUR_USD)
elif startingUnit == 'GBP':
    print('USD:', converted_GBP_USD)
    print('JPY:', converted_GBP_JPY)
    print('EUR:', converted_GBP_EUR)
elif startingUnit == 'INR':
    print('USD:', converted_INR_USD)
    print('EUR:', converted_INR_EUR)
    print('GBP:', converted_INR_GBP)
else:
    print('Error. Try another currency.')
    print('Use: USD, JPY, GBP, EUR, PHP.')