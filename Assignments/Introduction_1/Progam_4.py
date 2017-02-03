#Binary Translator
#3 Febuary 2017
#Maxwell Phillips
#C Block Programming
#-------------------
#Algorithm:
#1. Instructions text
#2. Request input
#3. Calculate result
#4. Output Result
#-------------------------------------------------------------------------------
#Instructions
print("Hello welcome to this Binary Translator! Lets translate some binary!")
print("Enter in each binary digit below in order from left to right.")
#Ask for input
val_1 = int(input("Enter the leftmost digit: "))
val_2 = int(input("Enter the next digit: "))
val_3 = int(input("Enter the next digit: "))
val_4 = int(input("Enter the rightmost digit: "))

n_1= int(val_1 * 2**3)
n_2= int(val_2 * 2**2)
n_3= int(val_3 * 2**1)
n_4= int(val_4 * 2**0)
#Calculate Result
result = str(n_1 + n_2 + n_3 + n_4)
print(result)
