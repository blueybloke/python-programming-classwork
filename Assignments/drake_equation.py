#Drake Equation Program
#Maxwell Phillips
#30 January 2017
#C Block Programming

import random
import time

responses = ["Nice job, lets do another one!", "Sounds good next value!", "Coolio, next one to go!"]

print("Hello there! Lets calculate some Drake equations!")
print("The Drake Equation is an equation created by Frank Drake in 1961")
print("to figure out the probability of there being intelligent life")
print("in the universe and whether or not we would find it.")

print("")
print("Lets put in some values for the equation. :)")
print("")

print("The first value needed is the average rate of star formation.")
R = int (input("Type it in here! : "))
print(random.choice(responses))

print("The second value is the percentage of stars with planets.")
p = int (input("Type it in here! : "))
print(random.choice(responses))

print("The thrid value is the average number of planets that can potentially support life for each star with planets.")
n = int (input("Type it in here! : "))
print(random.choice(responses))

print("The fourth value is the percentage of those planets that go on to develop life.")
f = int (input("Type it in here! : "))
print(random.choice(responses))

print("The fifth value is the percentage of those planets that go on to develop intelligent life.")
i = int (input("Type it in here! : "))
print(random.choice(responses))

print("The sixth value is the percentage of those planets that are willing and able to communicate.")
c = int (input("Type it in here! : "))
print(random.choice(responses))

print("The seventh value is the expected lifetime of those civilizations.")
L = int (input("Type it in here! : "))
print("Neat thats all of them!")


time.sleep(2.0)
print("")
print("And the answer is...")

print(str((R)*(p/100)*(n)*(f/100)*(i/100)*(c/100)*(L)))
print("")
print("Ta Da! Thanks for using!")
