# currency-converter
Python currency converter
- All based on data from 09-Feb-2020.
- No modules imported (yet).
- Cleaned up the code quite a bit.
- Default to USD if no input given.
- Default to 1 if no input given.

Usage - no inputs

```
bl@nuc:~/scripts/currency-converter$ ./convert.py 
Currency [USD]: 
How much [1]: 
--------------------
JPY: 110.0
PHP: 50.95
AUD: 1.5
INR: 71.52
GBP: 0.78
EUR: 0.91
```

Usage - Various

```
bl@nuc:~/scripts/currency-converter$ ./convert.py 
Currency [USD]: JPY
How much [1]: 50000
--------------------
USD: 460.0
PHP: 23000.0
bl@nuc:~/scripts/currency-converter$ ./convert.py 
Currency [USD]: EUR
How much [1]: 12345
--------------------
GBP: 10493.25
JPY: 1482757.95
EUR: 13456.05
```




### TO DO:
- Add in flags: -h (help), -c (currency), -a (amount), -t (date)

