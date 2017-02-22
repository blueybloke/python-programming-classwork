#Temperature Converter
#Maxwell Phillips
#21 Febuary 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Setup variables
#2)Greeting
#3)Prompt for farenheit value
#4)Calculate to celcius
#5Ddisplay result
#-------------------------------------------------------------------------------
#Setup variables
f = float(0.0)
#Greeting
print("This is a program designed to convert a farenheit temperature to celcius.")
#Prompt for farenheit value
f= float(input("Please input a temperature in farenheit: "))
#Calculate
c=float((f-32)*(5/9))
#Display result
print("The result is: ",format(c,'0.2f')+"º")
