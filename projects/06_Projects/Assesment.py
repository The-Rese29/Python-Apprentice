#1. Create 3 variables, 1 each of String, and Boolean
x = 15
l = "MynameisTherese"
Happy = True

#2. Write a for loop that pronts the numbers 1-100 except numbers that are divisible by 7

for i in range(100):
    print(i)
    if i%7 == 0:
        print(" ")

#3. Write a loop that prints every other letter of the string you created in first task

for i in range(1):
    if i%2 == 0:
        print(l[0:15:2])


#count = 0
#for x in len(l):
    #if count % 2 == 0:
    #print(l[x])
#4.a Create a function that takes in 2 arguments, both integers, and returns the sum of those 2 arguments

def Add_numbers(int_1, int_2):
    return int_1 + int_2


#4.b Call the function from task 4.a
Add_numbers(10,15)

#Ec_1.a Create a function that takes in a string as an argument and returns a list containing each  letter of the string

def create_list(string):
    return list(string)

#Thank you! -Therese