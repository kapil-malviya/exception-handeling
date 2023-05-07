"""

single except block that can handle multiple exceptions:


we can write a single except block that can handle multiple different types of exceptions
=>>
	except (Exception1,Exception2,exception3,..): or
	except (Exception1,Exception2,exception3,..) as msg :
parenthesis are mandatory and this group of exceptions internally considered as tuple

"""


try :
	x=int(input('enter first number : '))
	y=int(input('enter second number : '))
	print(x/y)

except (ZeroDivisionError, ValueError) as msg :
	print('please enter valid number & the problem is : ',msg)


"""
=>> 

enter first number : 8
enter second number : two
please enter valid number & the problem is :  invalid literal for int() with base 10: 'two'


enter first number : 8
enter second number : 0
please enter valid number & the problem is :  division by zero

"""