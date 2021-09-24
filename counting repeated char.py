#create a program that will take any string and display the counts and the repeated letters using the .count method

#this is for the input of the string

string = input("Enter any word or string here: ") #this is ing string form

print("I am going to check this string for any repeated letter: " + string)

#defining the char variable

for char in string:

    #we use the char arguement because that what we are going to use in order to count the char of the string
    count = string.count(char) #this is for the count logic the format is String_Name.count(args)

    if count > 1: #this is for the condition of the count, that if greater than 1 it will proceed with the print function

        print(char, count) #the print function can accept 2 parameters as an output








