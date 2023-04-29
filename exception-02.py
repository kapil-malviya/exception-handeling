'''
pythons exception hierarchy : 

											BaseException

				   Exception 		SystemExit 		GeneratorExit 		KeyboardInterrupt
                       |
                       |
                       ^
                    -------

Attribute Error    Arithmetic Error    EOF Error    Name Error    Lookup Error   	 OS Error       Type Error    Value Error

				   ZeroDivision 								  Index              FileNotFound
				   Error 										  Error              Error


				   FloatingPoint 								  Key                Interrupted
				   Error   										  Error              Error


				   Overflow															 Permission 
				   Error 															 Error


				   																	 Timeout
				   																	 Error  



every exception in python is a class..
all exception classes are child classes of BaseException, i.e every exception class extends BaseException either 
	directly or indirectly. Hence BaseException acts as root for python exception hierarchy.
Most of the times being a programmer we have to concentrate exception and its child classes.