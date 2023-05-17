
# Various possible combinations of try-except-else-finally :


# case-20

'''
try :
	print('try')
	try :
		print('inner try')
	except :
		print('inner except block')
	finally :
		print('inner finally block')
except :
	print('except')


* Valid *
=>> 
try
inner try
inner finally block 




# case-21 


try :
	print('try')
except :
	print('except')
	try :
		print('inner try')
	except :
		print('inner except block')
	finally :
		print('inner finally block')


* Valid *
=>> 
try         



# case-22


try :
	print('try')
except :
	print('except')
finally :
	print('finally')
	try :
		print('inner try')
	except :
		print('inner except block')
	finally :
		print('inner finally block')


* Valid *
=>> 
try  
finally
inner try
inner finally block               '''