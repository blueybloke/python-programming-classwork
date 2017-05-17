#Conversion Calculator
#Maxwell Phillips
#13 April 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Create Variables
#3)Ask which conversion to do
#4)Ask for input
#5)Calculate result
#6)Print result
#7)Ask to run again
#-------------------------------------------------------------------------------
#Greeting and print divider line
print("="*80)
print("""
This is a program to do a conversion of your choice, from a selection of:
Pounds to grams
Inches to Centimeters
and Kilometers to miles\n
""")
#Create stop variable for ask again feature
stop = False
while(stop == False):
    #Create Variables
    choice = 0
    user_input = 0
    result = 0
    #Ask which conversion to do and error check
    while True:
        try:
            print("Please choose which conversion to do from the list below:")
            print("Pounds to grams [1]")
            print("Inches to centimeters [2]")
            print("Kilometers to miles [3]")
            choice = int(input("Enter choice: "))
        except ValueError or choice != 1 or choice != 2 or choice != 3:
            #Error in choice input
            print("Please enter a value of 1, 2, or 3 for your choice.")
            choice = 0
        else:
            break
    #Start program according to user choice

    #Pounds to grams
    if (choice == 1):
        print("="*80)
        print("You have chosen to do a pounds to grams conversion.")
        while True:
            try:
                user_input = float(input("Please enter a weight in pounds: "))
            except ValueError:
                print("Please enter a decimal or interger value and try again.")
            else:
                break
        #Calculate result
        result = user_input*453.6
        print("Your input,",user_input,"is",result,"in grams!")

    #Inches to Centimeters
    if (choice == 2):
        print("="*80)
        print("You have chosen to do a inches to centimeters conversion.")
        while True:
            try:
                user_input = float(input("Please enter a distance in inches: "))
            except ValueError:
                print("Please enter a decimal or interger value and try again.")
            else:
                break
        #Calculate result
        result = user_input*2.54
        print("Your input,",user_input,"is",result,"in centimeters!")

    #Kilometers to miles
    if (choice == 3):
        print("="*80)
        print("You have chosen to do a kilometers to miles conversion.")
        while True:
            try:
                user_input = float(input("Please enter a distance in kilometers: "))
            except ValueError:
                print("Please enter a decimal or interger value and try again.")
            else:
                break
        #Calculate result
        result = user_input*0.62
        print("Your input,",user_input,"is",result,"in miles!")

    #Ask to use again
    if(input("\nRun Again (y/n)?: ") == "y"):
        stop = False
        print("="*80)
    else:
        stop = True
