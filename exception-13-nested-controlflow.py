"""
# Control flow in nested try-except-finally block :


try :
	statement-1
	statement-2
	statement-3
	try :
		statement-4
		statement-5
		statement-6
	except XXX :
		statement-7
	finally :
		statement-8
	statement-9
except YYY :
	statement-10
finally :
	statement-11
statement-12



# various possible cases : 

1.  =>>  if there is no exception :
output :
		1,2,3,4,5,6,8,9,11,12, normal termination



(within the try block if the database connection opened, then to close that database connection
 finally block executes for cleanup the activities related to try block., 
		if an exception raised at statement-2, then the control won't enter into inner try block,
		so.. here inner database connection not opened so why it would require to close that 
		database conncetion by the inner finally block & control will directly go to the outer 
		except block.,, so the inner try-except-finally block won't execute..)


2.  =>>  if exception raised at statement-2 & corresponding except block matched  
output :
		1,10,11,12, normal termination



3.  =>>  if an execption raised at statement-2 & corresponding except bock not matched
output :
		1,11, abnormal termination



4.  =>>  if an exception raised at statement-5 & corresponding inner except bock matched
output :
		1,2,3,4,7,8,9,11,12, normal termination



5.  =>>  if an exception raised at statement-5 & corresponding inner except block not matched 
		  but the outer except block matched
output :
		1,2,3,4,8,10,11,12, normal termination



6.  =>>  if an exception raised at statement-5 & both inner and outer except block not matched
output :
		1,2,3,4,8,11, abnormal termination



(in any block try/except/finally exception can be raised...)

7.  =>>  if an exception raised at statement-7 (control will go to outer exception block for this) 
		 & corresponding except block matched
output :
		1,2,3,_,_,_,8,10,11,12, normal termination
             (4,5,6) =>> if exception is raised at statement-7, it maybe because of exception
                         raised at statement-4/5/6,. so.. for this control will got to outer
                         except block..,



8.  =>>  if an exception raised at statement-7 & corresponding (outer) except block not matched 
output :
		1,2,3,_,_,_,8,11, abnormal termination
			 (4,5,6) =>> refer case-7


9.  =>>  if an exception raised at statement-8 & corresponding except block matched
output :
		1,2,3,_,_,_,_,10,11,12, normal termination
			 (4,5,6,7)



10.  =>>  if an exception raised at statement-8 & corresponding (outer) except block not matched
output :
		1,2,3,_,_,_,_,11, abnormal termination
			 (4,5,6,7)



11.  =>>  if an exception raised at statement-9 & corresponding (outer) except blocked matched
output :
		1,2,3,_,_,_,_,8,10,11,12, normal termination
		     (4,5,6,7) & without executing statement-8 control won't go to statement-9



12.  =>>  if an exception raised at statement-9 & corresponding (outer) except block not matched
output :
		1,2,3,_,_,_,_,8,11, abnormal termination
		     (4,5,6,7) & without executing statement-8 control won't go to statement-9



13.  =>>  if an exception raised at statement-10, then it is always abnormal termination but 
		  before abnormal termination finally block (statement-11) will be executed.,



14.  =>>  if an exception raised at statement-11 or statement-12, it is always abnormal termination



## if the control entered into try block then compulsary finally block will be executed,
	if the control not entered into try block then finally block won't be executed,.


"""