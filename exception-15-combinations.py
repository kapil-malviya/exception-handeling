"""
Various possible combinations of try-except-else-finally :


1. whenever we are writing try block, compulsory we should write except or finally block, 
	i.e without except or finally block we cannot write try block.

2. wheneever we are writing except block, compulsory we should write try block,
	i.e except without try is always invalid.

3. whenever we are writing finally block, compulsory we should write try block, 
	i.e finally without try is always invalid.

4. we can write multiple except blocks for the same try, but we cannot write multiple
	finally blocks for the same try.

5. whenever we are writing else block compulsory except block should be there, 
	i.e without except we cannot write else block.

6. in try-except-else-finally order is important.

7. we can define try-except-else-finally inside try, except, else and finally blocks, 
	i.e nesting of try-except-else-finally is always possible.


"""


# case-1 


'''
try :
	print('gold')

*Invalid*

SyntaxError: expected 'except' or 'finally' block



# case-2


except :
	print('gold')

*Invalid*

SyntaxError: invalid syntax 	




# case-3 

else :
	print('gold')

*Invalid*

SyntaxError: invalid syntax 		




# case-4

finally :
	print('gold')

*Invalid*

SyntaxError: invalid syntax 			'''