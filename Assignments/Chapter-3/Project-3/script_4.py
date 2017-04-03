#Script_4
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Get user input for numbers, and if number is >0 save as + # or if < 0 save as - #
#3)Find sum of each array
#4)Display response
#-------------------------------------------------------------------------------
#Greeting
print("""This is a program that will find the sum of a set of positive intergers
provided by the user and a set of negative integers.""")
print("="*80)
pos_numbers = []
neg_numbers = []
terminate = False
#Start error checking loop
while (terminate == False):
    pos_numbers = []
    neg_numbers = []
    entry = 0
    while True:
        #Ask for input
        entry = input("Enter an integer or leave blank to finish: ")
        if(entry == ""):
            print("The sum of your positive numbers is: ",str(sum(pos_numbers)))
            print("The sum of your negative numbers is: ",str(sum(neg_numbers)))
            break
        elif (int(entry) >= 0):
            pos_numbers.append(int(entry))
        elif (int(entry) <= 0):
            neg_numbers.append(int(entry))

    if(input("\nUse Again (y/n)?: ") == "y"):
        terminate = False
        print("="*80)
    else:
        terminate = True
