#Powers of Two Program
#3 Febuary 2017
#Maxwell Phillips
#C Block IT
#---------------------
#Algorithm:
#1. Greeting/Instructions
#2. Process/Calculate
#3. Output
#-------------------------------------------------------------------------------
import time
#Introduction
print("Welcome to the Powers of Two Program! Here we will be calculating the ")
print("powers of two!")
print("So, lets begin!\n")
time.sleep(1.0)
#Begin Calculation/Output
exponent = 1
while exponent < 9:
    #calculate and output
    print("Two to the power of " + str(exponent) + " is " + str(2 ** exponent) + "!")
    exponent = exponent + 1
    time.sleep(0.5)

print("\nThats all of it! Goodbye!")
