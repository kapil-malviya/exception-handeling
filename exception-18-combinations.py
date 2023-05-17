
# Various possible combinations of try-except-else-finally :


# case-15

'''
try :
	print('try')
except :
	print('except')
print('goldd')
finally :
	print('finally')




* Invalid *
=>> 
SyntaxError: invalid syntax    




# case-16

try :
	print("try")
except : 
	print("except")
print("Hello")
else :
	print("else")



* Invalid *
=>> 
SyntaxError: invalid syntax          



# case-17


try :
	print("try")
except :
	print("except")
try :
	print("try")
except :
	print("except")



* Valid *
=>> 
try 
try 	




# case-18

try :
	print("try")
except :
	print("except")
try :
	print("try")
finally :
	print("finally")



* Valid *
=>> 
try 
try 
finally			



# case-19

try :
	print("try")
except :
	print("except")
if 10>20 :
	print("if")
else :
	print("else")




* Valid *
=>> 
try 
else 					 '''