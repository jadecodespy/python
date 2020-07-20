def five():
	import random
	for i in range (100,201):
		if i%2==0:
            ran= random.sample(i,5)
    	    return ran
     else:
         return []
print(five())



if input > 1:
		for i in range (2,input):
			if(input % i)== 0:
				return(False)
		else:
			return (True)