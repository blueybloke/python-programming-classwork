#Script_2
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Get user input for credits
#3)Determine response according to credits
#4)Display response
#-------------------------------------------------------------------------------
#Greeting
print("""This is a program that will allow the user to enter an amount
of credits and then figure out their grade status according to the amount.\n""")
print("="*80)
credits = 0
terminate = False
#Start error checking loop
while (terminate == False):
    while True:
        #Ask for input
        credits = int(input("Please enter the number of credits to check for: "))
        if (credits > 90):
            print("Senior Status")
            break
        if (credits > 60):
            print("Junior Status")
            break
        if (credits > 30):
            print("Sophomore Status")
            break
        if (credits < 30):
            print("Freshman Status")
            break
    if(input("\nTry again (y/n)?: ") == "y"):
        terminate = False
        print("="*80)
    else:
        terminate = True
