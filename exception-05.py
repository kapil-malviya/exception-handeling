'''
=>> multiple exception blocks : 


the way of handling exception is varied from exception to exception, hence for every exception 
type a seperate except block we have to provide.

i.e try with multiple except blocks is possible and recommended to use...


syntax =>> 


try:
	-------
	-------
	-------

except ZeroDivisionError:
	perform alternative arithmetic operations

except FileNotFoundError:
	use local file instead of remote file


# if try with multiple except blocks available then based on raised exception the corresponding 
	except block will be executed.


'''

"""

try :
	x = int(input('enter first number : '))
	y = int(input('enter second number : '))
	print(x/y)
except ZeroDivisionError :
	print("can't divide a number by zero..")
except ValueError :
	print('please provide int value only..')




try :
	x = int(input('enter first number : '))
	y = int(input('enter second number : '))
	print(x/y)
except ArithmeticError :
	print("arithmetic error")
except ZeroDivisionError :
	print('can not divide a number by zero..')




enter first number : 10
enter second number : 0
arithmetic error


even if ZeroDivisionError(child) is comming ArithmeticError(parent) will handel
& this concept (of heirarchy of error) work from top to bottom only 

"""

try :
	x = int(input('enter first number : '))
	y = int(input('enter second number : '))
	print(x/y)
except ZeroDivisionError :
	print('can not divide a number by zero..')
except ArithmeticError :
	print("arithmetic error")


"""
enter first number : 8
enter second number : 0
can not divide a number by zero..

"""