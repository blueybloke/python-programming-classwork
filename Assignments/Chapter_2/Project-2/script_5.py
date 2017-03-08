#Interger Stuff Program
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Input and store as variables
#3)Calculations Print result
#-------------------------------------------------------------------------------
#Greeting
print("Spicy greeting")
#Input and store as variables
num_1 = int(input("Please input the first value: "))
num_2 = int(input("Please input the second value: "))
#Calculations and Print result
print(str(num_1)+" + "+str(num_2)+" = " + format(num_1+num_2,'0.2f'))
print(str(num_1)+" - "+str(num_2)+" = " + format(num_1-num_2,'0.2f'))
print(str(num_1)+" * "+str(num_2)+" = " + format(num_1*num_2,'0.2f'))
print(str(num_1)+" / "+str(num_2)+" = " + format(num_1/num_2,'0.2f'))
print(str(num_1)+" // "+str(num_2)+" = "+format(num_1//num_2,'0.2f'))
print(str(num_1)+" % "+str(num_2)+" = " + format(num_1%num_2,'0.2f'))
print(str(num_1)+" ** "+str(num_2)+" = "+format(num_1**num_2,'0.2f'))
