#Atoms Program
#Maxwell Phillips
#17 Febuary 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Introductions to the program
#2)Initialize variables
#3)Program greeting
#4)Prompt user weight
#5)Convert weight to kg
#6)Determine number of atoms
#7)Display results
#-------------------------------------------------------------------------------
#Notes:
#atoms = weight in kg/70*7e27
#Average weight of a person= 70kg
#number of atoms in a person = 7e27
#(Percent of the universe/atoms in the universe[7e27]) * 100
#-------------------------------------------------------------------------------
#prompt user weight in lb
weight_lb = float(input("Please enter your weight in pounds: "))
#convert to kg
weight_kg = float(weight_lb*(1/2.2))
#calculate percent of the universe
percent_of_universe = float(weight_kg/70.0*7e27)
#calculate answer
ans = float((percent_of_universe/7e27)*100)
#display answer
print("You take up: "+format(ans, '0.2f')+"% of the universe.")
