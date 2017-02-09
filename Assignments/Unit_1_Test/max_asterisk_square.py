#Asterisk Rectangle Program
#Maxwell Phillips
#9 Febuary 2017
#Programming I Class
#---------------------------
#Algorithm
#1). Display introduction and explaination text
#2). Request input for x axis dimesions and save as a interger variable
#3). Request input for y axis dimensions and save as a interger variable
#4). Print the number of asterisks the user inputted for the width
#5). Use a loop to create the left and right sides of the box
#6). Add a bottom to the box same as in step four
#7). End Program
#------------------------------------------------------------------------
#Introduction Text
print("Hello, welcome to this program to create pretty rectangles out of asterisks.")
#Requests width value and stores as a variable
print("Please enter a width for the rectangle you wish to create!")
w = int(input("Please use an interger(i.e:15): "))
#Request height value and store as a variable
print("Neat! Now can you please put in a height for the rectangle!")
h = int(input("Please use an interger(i.e:7): "))
print("Cool! Thats all of it! Here is your rectangle!")
print("")
#Output top side
print("*"*w)
#Output right/left sides
n = h
while n != 0:
    print("*"+(" "*(w-2))+"*")
    n= n-1
#Output bottom side
print("*"*w)
#Say goodbye and end program
print("")
print("There is your rectangle! Thanks for using!")
#------------------------------------------------------------------------
