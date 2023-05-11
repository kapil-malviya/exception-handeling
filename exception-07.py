"""
default except block :


=>>

	we can use default except block to handle any type of exceptions
	in default except block generally we can print normal error messages


syntax =>> 

	except:
		statements


"""



try :
	x = int(input('enter first number : '))
	y = int(input('enter second number : '))
	print(x/y)

except ZeroDivisionError :
	print("ZeroDivisionError : can't divide with zero ")
except :
	print("default except : please provide a valid input...")


'''		
=>> 

enter first number : 8
enter second number : 0
ZeroDivisionError : can't divide with zero


enter first number : 8
enter second number : two
default except : please provide a valid input...

'''


"""

if try with multiple except blocks available then default except block should be last,
otherwise we will get SyntaxError =>> 


try :
	x = int(input('enter first number : '))
	y = int(input('enter second number : '))
	print(x/y)

except :
	print("default except : please provide a valid input...")
except ZeroDivisionError :
	print("ZeroDivisionError : can't divide with zero ")


  File "D:\file handeling\exception-07.py", line 53
    except :
    ^^^^^^^^
SyntaxError: default 'except:' must be last

"""


"""

The following are various possible combinations of except blocks =>> 
	
	except ZeroDivisionError :
	except ZeroDivisionError as msg :
	except (ZeroDivisionError,ValueError) :
	except (ZeroDivisionError,ValueError) as msg :
	except :

"""