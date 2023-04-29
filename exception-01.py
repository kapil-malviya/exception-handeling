'''

	Exception handeling : 


	2 types of errors are possible : 
-> syntax errors 
-> runtime errors


1. syntax errors : 

x = 88
if x = 88;
	print('number is 88')

SyntaxError: invalid syntax.




2. runtime errors : 
	(exception handeling talks about runtime errors only)

=>> while executing the program if something goes wrong because of end user input or
	programming logic or memory problems etc then we will get runtime errors.

Eg: 

print(10/0) ==>ZeroDivisionError: division by zero

print(10/"ten") ==>TypeError: unsupported operand type(s) for /: 'int' and 'str'

x=int(input("Enter Number:"))
print(x)

Enter Number:ten
ValueError: invalid literal for int() with base 10: 'ten'


=>> exception handling concept applicable for runtime errors but not for syntax errors





******************




exception : 
		   an unwanted and unexpected event that disturbs normal flow of program is called exception   

ZeroDivisionError
TypeError
ValueError
FileNotFoundError
EOFError  (end of file)
SleepingError
TyrePuncturedError


purpose of exception handeling : graceful termination of the program 


exception handeling : 
					exception handling does not mean repairing exception, we have to define alternative
					 way to continue rest of the program normally..

	for example our programming requirement is reading data from remote file locating at
	london, at runtime if london file is not available then the program should not be
	terminated abnormally, we have to provide local file to continue rest of the program
	normally, this way of defining alternative is nothing but exception handling..





Default Exception Handing in Python : 
	every exception in python is an object, for every exception type the corresponding classes are available.
	whevever an exception occurs PVM will create the corresponding exception object and
	will check for handling code, if handling code is not available then python interpreter
	terminates the program abnormally and prints corresponding exception information to
	the console..
	the rest of the program won't be executed...



print("Hello")
print(10/0)
print("Hi")


=>> 

Hello
Traceback (most recent call last):
  File "C:\Users\Dell\Desktop\file handeling\exception-01.py", line 91, in <module>
    print(10/0)
          ~~^~
ZeroDivisionError: division by zero


'''



# pythons exception hierarchy : 