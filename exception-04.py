'''
control flow in try except block : 



try :
	statement-1
	statement-2
	statement-3

except xxx:
	statement-4

statement-5




case 1 =>> if there is no exception
output =>>
		  1,2,3,5 and normal termination


case 2 =>> if an exception raised at statement-2 and corresponding except block matched
output =>>
		  1,4,5 and normal termination


case 3 =>> if an exception raised at statement-2 and corresponding except block not matched
output =>>
		  1 and then abnormal termination


case 4 =>> if an exception raised at statement-4 or at statement-5 then it is always abnormal termination



Conclusions:

=>> within the try block if anywhere exception raised then rest of the try block wont be executed eventhough 
	we handled that exception. Hence we have to take only risky code inside try block and length of the try 
	block should be as less as possible.

=>> in addition to try block, there may be a chance of raising exceptions inside except and finally blocks also.

=>> if any statement which is not part of try block raises an exception then it is always abnormal termination.


'''
"""

=>> how to print exception information : 

"""


try :
	print(8/0)
except ZeroDivisionError as msg :
	print('exception raised and its description is : ',msg)


'''
exception raised and its description is :  division by zero
'''



# try with multiple except blocks : 