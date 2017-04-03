#Script_1
#Maxwell Phillips
#Date
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Get user input
#3)Determine response according to entry
#4)Display response
#-------------------------------------------------------------------------------
#Greeting
print("""This is a program that will output either Apple, Banana,
or Coconut according to whether the user enters A, B, or C.\n""")
print("="*80)
entry = ""
#Start error checking loop
while not (entry == "A" or entry == "B" or entry == "C"):
    #Ask for input
    entry = input("Please enter either a letter A, B, or C: ")
else:
    #Display
    if (entry == "A"):print("Apple")
    if (entry == "B"):print("Banana")
    if (entry == "C"):print("Coconut")
