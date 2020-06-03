first_twelve=[9,8,3,6,5,4,3,7,6,5,3,2]
Even_digit=[]
odd_digit=[]
for i in first_twelve[1::2]:
    Even_digit.append(i*3)
for i in first_twelve[::2]:
    odd_digit.append(i)
Total= sum(Even_digit) + sum(odd_digit)
last_digit=10-(Total%10)

   
print(first_twelve)
print(Even_digit)
print(odd_digit)
print(Total)
print(last_digit)
    