#Breaths/Beats per min
#Maxwell Phillips
#24 April
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Set variables
#3)Ask for input
#4)Calculate breaths according to age range
#5)Calculate beats.
#6)Print results
#-------------------------------------------------------------------------------
#Greeting
print("""
This is a program that will calculate the amount of heartbeats and breaths you
have taken in your life for people under the age of 18.""")
#Divider line
print("="*80)
#Set variables
min_in_year = 525600
brpm = 0
bpm = 67.5
#Store age ranges
infant = range(0,1)
child = range(2,4)
preteen = range(5,14)
teen = range(15,18)
#Ask for input
user_age = float(input("Please enter your age(Less than 18 please.): "))
while True:
    #Calculate breaths per year
    if(user_age in infant):
        brpm = 55
        break
    elif(user_age in child):
        brpm = 25
        break
    elif(user_age in preteen):
        brpm = 27.5
        break
    elif(user_age in teen):
        brpm = 17
        break
    else:
        print("Invalid Entry!")
        user_age = float(input("Please enter your age(Less than 18 please.): "))
total_breaths = brpm * min_in_year * user_age
#Calculate beats per min
total_beats = bpm * min_in_year * user_age
#print results
print("You have breathed a total of roughly:",format(total_breaths,"0.0f"),"times!")
print("Your heart has beated a total of roughly:",format(total_beats,"0.0f"),"times!")
