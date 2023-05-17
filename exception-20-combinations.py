
# Various possible combinations of try-except-else-finally :


# case-23

'''
try :
	print('try')
except :
	print('except')
try :
	print('try')
else :
	print('else')


* Invalid *
=>>
SyntaxError: expected 'except' or 'finally' block 		




# case-24


try :
	print("try")
	try :
		print("inner try")
except :
	print("except")


* Invalid *
=>>
SyntaxError: expected 'except' or 'finally' block




# case-25


try :
	print('try')
else :
	print("else")
except :
	print("except")
finally :
	print("finally")



* Invalid *
=>>
SyntaxError: expected 'except' or 'finally' block 		'''