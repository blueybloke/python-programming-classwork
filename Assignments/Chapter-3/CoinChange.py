#Coin Change Program
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting and import
#2)Setup variables
#3)Start progam loop
#4)Set a random amount
#5)Ask for the first coin
#6)Check if coin is not 1,5,10,or 25
#7)If coin is one of those values append it to the list of coins and ask for
#next coin
#8)Otherwise output an error message and ask again
#9)Repeat until no value is entered
#10)Find the sum of the list of coins and check if it is valid
#11)Ask to run again
#-------------------------------------------------------------------------------
#Import
from random import randint

#Set variables
end = False
coins = []
valid_coins = [1,5,10,25]
#Greeting
print("""                                     
                       88              
                       ""                                                    
 ,adPPYba,  ,adPPYba,  88 8b,dPPYba,   
a8"     "" a8"     "8a 88 88P'   `"8a  
8b         8b       d8 88 88       88  
"8a,   ,aa "8a,   ,a8" 88 88       88  
 `"Ybbd8"'  `"YbbdP"'  88 88       88                                        
""")
print("The purpose of this exercise is to enter a number of coin values that",
"\nadd up to a displayed target value.\n")
#Instructions
print("\nEnter Coins values as 1-penny, 5-nickel, 10-dime, and 25-quarter.",
"\nHit return after the last entered coin value.")
print("-----------------------------------------------------------------------")
#Being program loop
while (end == False):
    #Reset amount of coins
    coins = []
    #Choose amount
    amount = randint(1,99)
    #Print amount
    print("Enter coins that add up to",amount,"cents, one per line.",
          "To see if your answer is correct just leave the coin field blank.\n")
    #Start asking for coins loop
    current_input_value = 0
    while (current_input_value != ""):
        #Ask for coin value
        current_input_value = input("Enter a coin: ")
        #Check if they entered a value that was blank
        if (current_input_value == ""):
            #keep the blank value for the while loop and break out of If statement.
            break
        else:
            current_input_value = int(current_input_value)
            #If the users input is a valid coin...
            if (current_input_value in valid_coins):
                #Add the coin to the list and break
                coins.append(current_input_value)
            else:
                #If it is not a valid coin ask for a correct value
                print("Please enter a value of 1, 5, 10, or 25.")

    #Player has entered a blank value indicating that they want to know the
    #result.

    #Check if the coins sum to the value and print if they do or not.
    if (amount == sum(coins)):
        print("\nCorrect!")
    else:
        print("\nSorry - you only entered "+str(sum(coins))+" cents!")

    #Ask to try again
    if(input("\nTry again (y/n)?: ") == "y"):
        end = False
    else:
        end = True
