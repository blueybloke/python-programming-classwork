#Script 1
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Declare Variables
#3)Ask for integers until user types q
#4)For each integer entered, check if it is within the range and if so append to a list
#5)Afterwards loop over and print the list
#-------------------------------------------------------------------------------
#Greeting
print("="*80)
print("This is a program that prompts the user for a list of integers,\
stores in another list only those values between 1 - 100,\
and displays the resulting list.")
#Decalre variables
my_list = []
user_input = ""
end = False
while (end == False):
    user_input = input("Please enter an integer or q to exit
    #Check if the user entered q
    if(user_input == "q"):
        end = True
    else:
        #If the variable is within range append it to the list
        user_input_int = int(user_input)
        if (user_input_int >= 1 and user_input_int <= 100):
            my_list.append(user_input_int)

#Print the list
print("\nHere is your list:")
for i in my_list:
    print(i)
