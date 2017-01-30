import sys
n = int(input("Number? : "))
if n > 5:
    print("That number is greater than 5!")
else:
    print("That number sure ain\'t greater than 5!")

name = str(input("Hey there! What's your name? : "))
ready = str(input("Hey "+name+"! Hope your doing fine, are you ready to begin?(Type 'yes' or 'no')"))
if ready == "yes":
    input("Awesome! Lets get started!(Press enter to continue...)")
elif ready == "no":
    input("Well that sucks :P KK cya l8tr!(press enter...)")
    sys.exit()
