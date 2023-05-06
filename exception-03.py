"""
Customized Exception Handling by using try-except:


it is highly recommended to handle exceptions,
the code which may raise exception is called risky code and we have to take risky code
	inside try block and the corresponding handling code we have to take inside except block.


try:
	risky code
except xxx:
	handling code/alternative code




without try-except :


print('goldd')
print(8/0)
print('eight')


=>> 

goldd
Traceback (most recent call last):
  File "C:\Users\Dell\Desktop\file handeling\exception-03.py", line 20, in <module>
    print(8/0)
          ~^~
ZeroDivisionError: division by zero



with try-except :
"""


print('goldd')

try :
	print(8/0)
except ZeroDivisionError :
	print(8/2)

print('eight')


'''
=>> 

goldd
4.0
eight

'''