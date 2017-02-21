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
#(Percent of the universe/atoms in the universe[10e80]) * 100
#-------------------------------------------------------------------------------
#Initialize
num_atoms_universe = 10e80
#greeting
print("This program will figure out your place in the universe by telling you")
print("what percent of the universe you make up. Prepare to feel insignifigant.")
#prompt user weight in lb
weight_lb = float(input("Please enter your weight in pounds: "))
#convert to kg
weight_kg = float(weight_lb*2.2)
#calculate percent of the universe
num_atoms = float(weight_kg/70.0*7e27)
#calculate answer
ans = float((num_atoms/num_atoms_universe)*100)
#display answer
print("You contain around "+ format(num_atoms, '0.2e')+" atoms.")
print("You take up: "+format(ans, '0.2e')+"% of the universe.")
