#Drake Equation Program
#Maxwell Phillips
#30 January 2017
#C Block Programming
#-------------------------------------------------------------------------------

#import packages for effects
import random
import time
#a few responses for each time you type in a value
responses = ["Nice job, lets do another one!", "Sounds good next value!", "Coolio, next one to go!"]
#an introduction to the idea of the drake equation
print("Hello there! Lets calculate some Drake equations!")
print("The Drake Equation is an equation created by Frank Drake in 1961")
print("to figure out the probability of there being intelligent life")
print("in the universe and whether or not we would find it.")
#begining the value input part
print("")
print("Lets put in some values for the equation. :)")
print("")
#first value
print("The first value needed is the average rate of star formation.")
R = int (input("Type it in here! : "))
print(random.choice(responses))
#second value
print("The second value is the percentage of stars with planets.")
p = int (input("Type it in here! : "))
print(random.choice(responses))
#third value
print("The thrid value is the average number of planets that can potentially support life for each star with planets.")
n = int (input("Type it in here! : "))
print(random.choice(responses))
#fourth value
print("The fourth value is the percentage of those planets that go on to develop life.")
f = int (input("Type it in here! : "))
print(random.choice(responses))
#fifth value
print("The fifth value is the percentage of those planets that go on to develop intelligent life.")
i = int (input("Type it in here! : "))
print(random.choice(responses))
#sixth value
print("The sixth value is the percentage of those planets that are willing and able to communicate.")
c = int (input("Type it in here! : "))
print(random.choice(responses))
#seventh value
print("The seventh value is the expected lifetime of those civilizations.")
L = int (input("Type it in here! : "))
print("Neat thats all of them!")

#drumroll...
time.sleep(2.0)
print("")
print("And the answer is...")
#calculates and prints the result of the equation using variables from before
print(str((R)*(p/100)*(n)*(f/100)*(i/100)*(c/100)*(L)))

#line space and end message
print("")
print("Ta Da! Thanks for using!")
#-------------------------------------------------------------------------------
