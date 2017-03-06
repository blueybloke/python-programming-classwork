#Integer Divison
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Input and store as variables
#3)Divide Variables and store result
#4)Format and Print result
#-------------------------------------------------------------------------------
#Greeting
print("Welcome, this program takes two Integer numbers and divides them")
print("by each other, rounding to the 2nd decimal place. \n")
#Request Input
int_1 = int(input("Please input the first number here: "))
int_2 = int(input("Please input the second number here: "))
#Divide and store result
result = int_1/int_2
#Print result
print("The answer is: "+str(format(result,'0.2f')))
#End Program
