  #Write a function which returns the boolean True if the input is only divisible by one and itself.
    
   # The function should return the boolean False if not.
    #two(3) → True
    #two(8) → False

#if you divide the input by any number and 
# there is a reminder then its not a prime number and the result will be false


def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return (False)
                break
            else:
                return(True)


print (prime(21))
















