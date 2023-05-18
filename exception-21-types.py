"""
# Types of Exceptions :  & (raise keyword)

1. Predefined Exceptions/In Built Exceptions
2. User Definded Exceptions/Customised Exceptions


## Predefined Exceptions =>>

	the exceptions which are raised automatically by python virtual machine whenver a
	particular event occurs, are called pre defined exceptions.

Eg 1 =>>
	whenever we are trying to perform division by zero, automatically python will raise
	ZeroDivisionError.
 
print(10/0)

Eg 2 =>> 
	whenever we are trying to convert input value to int type and if input value is not
	int value then python will raise ValueError automatically

x=int("ten")  =>>  ValueError



## User Defined Exceptions =>>

	also known as Customized Exceptions or Programatic Exceptions
	Some time we have to define and raise exceptions explicitly to indicate that something
	goes wrong, such type of exceptions are called User Defined Exceptions or Customized
	Exceptions

	Programmer is responsible to define these exceptions and Python not having any idea
	about these. Hence we have to raise explicitly based on our requirement by using "raise"
	keyword.

Eg =>> 

	InSufficientFundsException
	InvalidInputException
	TooYoungException
	TooOldException                      """



# How to Define and Raise Customized Exceptions :


class TooYoungException (Exception) :
	def __init__ (self, arg) :
		self.msg=arg 

class TooOldException (Exception) :
	def __init__ (self, arg) :
		self.msg=arg 

age = int(input('enter age : '))
if age > 60 :
	raise TooOldException ('your age already crossed, no chance of marriage now...')
elif age < 18 :
	raise TooYoungException ('wait till your age is 18...')
else :
	print('thanks for the registration, you will get match details soon...')
