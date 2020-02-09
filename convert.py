#!/usr/bin/env python3

startingUnit = input('Currency: ')
startingValue = input('How much: ')
startingValue = float(startingValue)

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

if startingUnit == 'USD':
    converted_USD_JPY = round(startingValue * usd_jpy, 2)
    converted_USD_PHP = round(startingValue * usd_php, 2)
    converted_USD_AUD = round(startingValue * usd_aud, 2)
    converted_USD_EUR = round(startingValue * usd_eur, 2)
    converted_USD_INR = round(startingValue * usd_inr, 2)
    converted_USD_GBP = round(startingValue * usd_gbp, 2)
    print('JPY:', converted_USD_JPY)
    print('PHP:', converted_USD_PHP)
    print('JPY:', converted_USD_AUD)
    print('PHP:', converted_USD_INR)
    print('GBP:', converted_USD_GBP)
    print('EUR:', converted_USD_EUR)
elif startingUnit == 'usd':
    converted_USD_JPY = round(startingValue * usd_jpy, 2)
    converted_USD_PHP = round(startingValue * usd_php, 2)
    converted_USD_AUD = round(startingValue * usd_aud, 2)
    converted_USD_EUR = round(startingValue * usd_eur, 2)
    converted_USD_INR = round(startingValue * usd_inr, 2)
    converted_USD_GBP = round(startingValue * usd_gbp, 2)
    print('JPY:', converted_USD_JPY)
    print('PHP:', converted_USD_PHP)
    print('JPY:', converted_USD_AUD)
    print('PHP:', converted_USD_INR)
    print('GBP:', converted_USD_GBP)
    print('EUR:', converted_USD_EUR)
elif startingUnit == 'JPY':
    converted_JPY_USD = round(startingValue * jpy_usd, 2)
    converted_JPY_PHP = round(startingValue * jpy_php, 2)
    print('USD:', converted_JPY_USD)
    print('PHP:', converted_JPY_PHP)
elif startingUnit == 'jpy':
    converted_JPY_USD = round(startingValue * jpy_usd, 2)
    converted_JPY_PHP = round(startingValue * jpy_php, 2)
    print('USD:', converted_JPY_USD)
    print('PHP:', converted_JPY_PHP)
elif startingUnit == 'PHP':
    converted_PHP_USD = round(startingValue * php_usd, 2)
    converted_PHP_JPY = round(startingValue * php_jpy, 2)
    print('USD:', converted_PHP_USD)
    print('JPY:', converted_PHP_JPY)
elif startingUnit == 'php':
    converted_PHP_USD = round(startingValue * php_usd, 2)
    converted_PHP_JPY = round(startingValue * php_jpy, 2)
    print('USD:', converted_PHP_USD)
    print('JPY:', converted_PHP_JPY)
elif startingUnit == 'EUR':
    converted_EUR_USD = round(startingValue * eur_usd, 2)
    converted_EUR_JPY = round(startingValue * eur_jpy, 2)
    converted_EUR_GBP = round(startingValue * eur_gbp, 2)
    print('GBP:', converted_EUR_GBP)
    print('JPY:', converted_EUR_JPY)
    print('EUR:', converted_EUR_USD)
elif startingUnit == 'eur':
    converted_EUR_USD = round(startingValue * eur_usd, 2)
    converted_EUR_JPY = round(startingValue * eur_jpy, 2)
    converted_EUR_GBP = round(startingValue * eur_gbp, 2)
    print('GBP:', converted_EUR_GBP)
    print('JPY:', converted_EUR_JPY)
    print('EUR:', converted_EUR_USD)
elif startingUnit == 'GBP':
    converted_GBP_USD = round(startingValue * gbp_usd, 2)
    converted_GBP_JPY = round(startingValue * gbp_jpy, 2)
    converted_GBP_EUR = round(startingValue * gbp_eur, 2)
    print('USD:', converted_GBP_USD)
    print('JPY:', converted_GBP_JPY)
    print('EUR:', converted_GBP_EUR)
elif startingUnit == 'gbp':
    converted_GBP_USD = round(startingValue * gbp_usd, 2)
    converted_GBP_JPY = round(startingValue * gbp_jpy, 2)
    converted_GBP_EUR = round(startingValue * gbp_eur, 2)
    print('USD:', converted_GBP_USD)
    print('JPY:', converted_GBP_JPY)
    print('EUR:', converted_GBP_EUR)
else:
    print('Error. Try with caps or another currency.')
