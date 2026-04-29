import numpy as np

# user input
def getinput():
    first = input("Would you like to go first? (y/n) : ")
    while first != "y" and first != "n":
        first = input("Would you like to go first? (y/n) : ")

    # think = input("How long should the computer think about its moves (in seconds)? : ")
    think = 5
    return first, think

# evaluation function

# search tree 
## alpha beta pruning

# print board

# main ()
