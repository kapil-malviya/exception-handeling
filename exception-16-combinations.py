
# Various possible combinations of try-except-else-finally :


# case-5 

'''
try :
	print('gold')
except :
	print('silver')


* Valid *
=>> 
gold            



# case-6

try :
	print('gold')
finally :
	print('dollar')


* Valid *
=>> 
gold 
dollar              



# case-7

try :
	print('try')
except :
	print('except')
else :
	print('else')


* Valid *
=>> 
try 
else            



# case-8

try :
	print('try')
else :
	print('else')


* Invalid *
=>> 
SyntaxError: expected 'except' or 'finally' block          




# case-9 

try :
	print('try')
else :
	print('else')
finally :
	print('finally')



* Invalid *
=>> 
SyntaxError: expected 'except' or 'finally' block

  '''