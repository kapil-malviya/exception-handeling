# various cases of finally block : 


# case 1 =>> if there is no exception : 

try :
	print('try')

except :
	print('except')

finally :
	print('finally')

print()
"""
tr y
finally

"""


# case 2 =>> if an exception raised but handeled :

try :
	print('try')
	print(10/0)

except ZeroDivisionError :
	print('except')

finally :
	print('finally')


print()

'''
try
except
finally

'''
