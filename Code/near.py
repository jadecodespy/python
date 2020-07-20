s#Create a function that when given two strings of letters, determine whether the second can be made from the first by removing one letter.
# The remaining letters must stay in the same order.
#Example
#near ("reset", "rest") => true
#near ("dragoon", "dragon") => true
#near ("eave", "leave") => false
#near ("sleet", "lets") => false



string_one= input('String One: ')
string_two= input('String Two: ')

#print(string_one == string_two)
#print (string_one.find(string_two))

#if string_one.find(string_two) == -1:
    #print (True)

#print(string_two in string_one)


for i in string_two:
    i=i in string_one
    
