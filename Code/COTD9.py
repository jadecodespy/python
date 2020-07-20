def squared(odd):
    newodd=list()
    for i in odd:
        if i%2 !=0:
            newodd.append(i*i)
    return newodd
        
        
num1=[1,3,5]
print(squared(num1))