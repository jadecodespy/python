#A website requires the users to input username and password to register. 
#Write a function to check the validity of password input by users.
	#Following are the criteria for checking the password:
	
	 
	
	#- At least 1 letter between [a-z]
#	- At least 1 number between [0-9]
#	- At least 1 letter between [A-Z]
#	- At least 1 character from [$#@]
#	- Minimum length of transaction password: 6
	#- Maximum length of transaction password: 12
	
	 
	
	#Your program should accept a list of passwords of an indeterminate length and will check them according to the above criteria.
    #Passwords that match the criteria are to be returned in a list.
	
	 
	
	#Example
	
	 
	
	#If the following passwords are given as input to the program:
	#["ABd1234@1","a F1#","2w3E*","2We3345"]
	#Then, the output of the program should be:
	#["ABd1234@1"]

def password_check(password):
    characters= ['$', '@', '#']
    number='0123456789'
        
    if len(password) <= 6:
        return 'lenght should be at least 6 Characters'
        
    if len(password) >=20:
        print('lenght should be not greater than 20')





def pass_check(password):
    spec_chars=['#', '@', '$']
    numbers='0123456789'
  
    
        
       







	 