"""

# Else block with try-except-finally :

=>>  else block will be executed if and only if there are no exceptions inside try block..
=>>  finally block will always be executed if exception raised or not raised and handeled or not handeled
	 finally block will always execute

Syntax =>>


try :
	risky code
except :
	will be executed if exception in try block
else :
	will be executed if there is no exception inside try block
finally :
	will be executed wheteher exception raised or not raised and handeled or not handeled



try :
	print('try')
	#print(8/0)
except :
	print('except')
else :
	print('else')
finally :
	print('finally')


"""

'''
try
else
finally

'''


try :
	print('try')
	print(8/0)
except :
	print('except')
else :
	print('else')
finally :
	print('finally')

'''
try
except
finally

'''