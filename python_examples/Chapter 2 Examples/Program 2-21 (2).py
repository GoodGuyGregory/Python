Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Floating-point Program example 2-21
>>> monthly_pay = 5000.00
>>> annual_pay = monthly_pay * 12
>>> print('Your annual pay is $',format(annual_pay, ',.2f'))
Your annual pay is $ 60,000.00
>>> monthly_pay = 1410.00
>>> annual_pay = monthly_pay * 12
>>> print('Your annual pay is $ ',format(annual pay, ',.2f'))
SyntaxError: invalid syntax
>>> print('Your annual pay is $ ',format(annual_pay, ',.2f'))
Your annual pay is $  16,920.00
>>> monthly_pay = 720.00
>>> annual_pay = monthly_pay * 12
>>> print('Your annual pay is $',format(annual_pay, ',.2f'))
Your annual pay is $ 8,640.00
>>> 
