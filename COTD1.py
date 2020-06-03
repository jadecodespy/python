#Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

 

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


num=int(input('Please Enter a Number: '))

factorial =1
all_factorials=[]

if num == 0:
    print('The Factorial of 0 is 1')
else:
    for i in range(1,num + 1):
        factorial= factorial * i
        

print(factorial)

for i in str(factorial):
    all_factorials.append(i)
print(all_factorials)