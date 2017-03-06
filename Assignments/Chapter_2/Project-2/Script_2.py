#Float Divison
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
print("This program takes two float values and divides them by each other. \n")
#Request Input
float_1 = float(input("Please input the first number here: "))
float_2 = float(input("Please input the second number here: "))
#Divide and store result
result = float_1/float_2
#Print result
print("The answer is: "+str(format(result,'0.6f')))
#End Program
