"""

finally block : 


open database connection 
reading data
close databse conncetion  =>>  resource deallocation code  =>>  cleanup code


Why finally block

=>> 
	it is not recommended to maintain clean up code(Resource Deallocating Code or
	Resource Releasing code) inside try block because there is no guarentee for the execution
	of every statement inside try block always,

	it is also not recommended to maintain clean up code inside except block, because if there
	is no exception then except block won't be executed..

	Hence we required some place to maintain clean up code which should be executed
	always irrespective of whether exception raised or not raised and whether exception
	handled or not handled, such type of best place is nothing but finally block.
	hence the main purpose of finally block is to maintain clean up code.

Syntax =>> 

try:
	risky code

except:
	handling code

finally:
	cleanup code


the speciality of finally block is it will be executed always whether exception raised or not
raised and whether exception handled or not handled,

"""

