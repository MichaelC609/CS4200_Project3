import numpy as np

# user input
def getinput():
    first = input("Would you like to go first? (y/n) : ").strip()
    while first != "y" and first != "n":
        first = input("Would you like to go first? (y/n) : ").strip()

    # think = input("How long should the computer think about its moves (in seconds)? : ")
    think = 5
    return first, think

def getmove(board):
    legalrow = ['a','b','c','d','e','f','g','h']
    legalcol = range(1,9)

    while True:
        move = input("Choose your next move: ").strip()
    
        if len(move) != 2:
            print("Invalid input. Please enter a move like D4.")
            continue
        
        col, row = move[0].lower , int(move[1])

        if col not in legalcol or row inot in legalrow:
            print("Column must be an integer between 1 and 8. Row must be a letter between A and H.")
            continue

        x, y = legalcol.index(col), row-1

        if board[y][x] == "-":
            print("That space is already taken.")
            continue

        return x, y
    

    # translate to the coordinate on an 8x8 grid

    # make sure the move is legal 
    
    # check the board to make sure space isn't filled

    # if all checks out, then return the move as a coordinate
    return 

# evaluation function

# search tree 
## alpha beta pruning

# print board

# main ()
