#Chess Program
#Maxwell Phillips
#14 March 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Greeting
#2)Calculate, there are 64 squares on a chess board.
#3)Loop that doubles value  each time until all 64 squares are covered
#4)Print output and format
#-------------------------------------------------------------------------------
#Greeting
print("Hello, this is a script to estimate how much wheat the creator of the "
"board game Chess would have received from an Indian king in exchange for the "
"game. He came up with a deal where for each square on the chess board the "
"amount of grain he would receive would be doubled, leading to him getting a "
"LOT of wheat. This program shows exactly how much wheat that is.")
#Assign variables
num_of_grains = 1
i = 0
#Begin loop
while (i < 64):
    #Double the amount of grain
    num_of_grains = num_of_grains * 2
    #Add one to the iteration value
    i = i + 1
    #Uncomment line below to get the debug text.
    print("Now on iteration "+str(i)+" I have "+str(num_of_grains)+" grains.\n")
#Convert to pounds
weight = num_of_grains/7000
#Format & print
print("\nThe final weight of the wheat would be: "+ format(weight,'0.0f')+" pounds!")
#End Script
