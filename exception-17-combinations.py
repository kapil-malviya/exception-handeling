
# Various possible combinations of try-except-else-finally :


# case-10

'''
try :
	print("try")
except XXX :
	print("except-1")
except YYY :
    print("except-2")


* Valid *
=>> 
try 



# case-11 

try :
	print("try")
except :
    print("except-1")
else :
    print("else")
else :
	print("else")


* Invalid *
=>> 
SyntaxError: invalid syntax  

( in try-except-else-finally block =>> only except can be multiple times and try, else, finally
	compulsory it should only once )		



# case-12

try :
    print("try")
except :
    print("except-1")
finally :
    print("finally")
finally :
    print("finally")


* Invalid *
=>> 
SyntaxError: invalid syntax



# case-13

try :
	print("try")
print("Hello")
except :
	print("except")


* Invalid *
=>> 
SyntaxError: expected 'except' or 'finally' block  





#  case-14

try :
	print('try')
except :
	print('except-1')
print('gold')
except :
	print('except-2')



* Invalid *
=>> 
SyntaxError: invalid syntax           '''