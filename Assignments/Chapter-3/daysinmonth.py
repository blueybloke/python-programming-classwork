#Days in a Month Program
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Import Package
#2)Greeting
#3)Open while for program running
#4)Ask for year
#5)Ask for month
#6)Calculate days in month
#7)Print calendar
#8)Print number of days
#-------------------------------------------------------------------------------
#Import package
import calendar
end = False
#Greeting
print("This is a program to calculate the amount of days in a given month.\n")
#Open program
while (end == False):
    #Ask for year
    while True:
        try:
            year = int(input("Input year[e.g, 2014]: "))
        except ValueError:
        #Error in input
            print("Please enter a year from 1800-present year.")
        else:
            break
    #Ask for month
    month = int(input("Input month[1-12]: "))
    if (month < 1 or month > 12):
        print("Please input a value between 1-12 for the month.")
    else:
        #calculate number of Days
        days = int(calendar.monthrange(year,month)[1])
        #Print calendar
        print("\n",calendar.month(year,month))
        #Show number of Days
        print("\nThere are "+str(days)+" days in the month of "+str(calendar.month_name[month])+".")
        #Ask to run again
        if(input("\nType [y] to run the program again or anything else exit: ") != "y"):
            print("Okay, thanks for using!")
            end = True
