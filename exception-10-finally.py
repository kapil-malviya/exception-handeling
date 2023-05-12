# case 3 =>> if an exception raised but not handeled : 

'''
try :
	print('try')
	print(10/0)

except ValueError :
	print('except')

finally :
	print('finally') 



=>> 

try
finally
Traceback (most recent call last):
  File "D:\file _____________.py", line 51, in <module>
    print(10/0)
          ~~^~
ZeroDivisionError: division by zero

''' 



"""		finally block won't execute :

there is only one situation where finally block won't be executed ie whenever we are using os._exit(0) function.   


whenever we are using os._exit(0) function then Python Virtual Machine itself will be shutdown.

in this particular case finally block won't be execute

"""

'''

try :
	print('try')
	os._exit(0)
except :
	print('except')
finally :
	print('finally')


 =>> 
try
except
finally

'''


import os
try :
	print('try')
	os._exit(0)
except :
	print('except')
finally :
	print('finally')


''' =>> 
try


os._exit(0)
	where 0 represents status code and it indicates normal termination
	there are multiple status codes are possible,

'''