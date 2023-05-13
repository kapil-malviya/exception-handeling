'''

# control flow in try-except-finally block :




try :
	statement-1
	statement-2
	statement-3

except XXX :
	statement-4

finally :
	statement-5

statement-6




# case 1  =>>  if there is no exception :
=>>
	1, 2, 3, 5, 6, normal termination (won't return error)



# case 2  =>>  if an exception raised at statement-2 and the corresponding except block matched
=>> 
	1, 4, 5, 6, normal termination



# case 3  =>>  if an exception raised at statement-2 but the corresponding except block not matched
=>> 
	1, 5, abnormal termination (error)



# case 4  =>> if an exception raised at statement-4 then it is always abnormal termination but before 
				that finally block (statement-5) will be executed
=>>
	abnormal termination



# case 5  =>>  if an exception raised at statement-5 or at statement-6 then it is always
				abnormal termination