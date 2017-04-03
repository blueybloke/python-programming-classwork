#Script_3
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Get user input for numbers, and if number is >0 & <100 save it to an array
#3)Find sum of array
#4)Display response
#-------------------------------------------------------------------------------
#Greeting
print("""This is a program that will find the sum of a set of intergers
provided by the user, excluding an integers that are greater than 100 or
negative.""")
print("="*80)
numbers = []
terminate = False
#Start error checking loop
while (terminate == False):
    numbers = []
    entry = 0
    while True:
        #Ask for input
        entry = input("Enter an integer or leave blank to finish: ")
        if(entry == ""):
            print("The sum of your numbers is: ",str(sum(numbers)))
            break
        elif (int(entry) >= 0 and int(entry) < 100):
            numbers.append(int(entry))

    if(input("\nTry again (y/n)?: ") == "y"):
        terminate = False
        print("="*80)
    else:
        terminate = True
