"""
Nested try-except-finally blocks:


we can take try-except-finally blocks inside try or except or finally blocks, 
i.e nesting of tryexcept-finally is possible..



Syntax =>> 

try:
	-------
	-------
	-------
 	try:
		----------
		----------
		----------
	except:
		----------
		----------
		----------
		----------
except:
	-------
	-------


general risky code we have to take inside outer try block and too much risky code we have 
to take inside inner try block, inside inner try block if an exception raised then inner 
except block is responsible to handle, if it is unable to handle then outer except block is
responsible to handle...

"""


try :
	print('outer try block')
	try :
		print('inner try block')
		print(8/0)
	except ZeroDivisionError :
		print('inner except block')
	finally :
		print('inner finally block')
except :
	print('outer except block')
finally :
	print('outer finally block')


'''
=>>	 output :

outer try block
inner try block
inner except block
inner finally block
outer finally block

'''