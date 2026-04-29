import numpy as np
import math

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

        if col not in legalcol or row not in legalrow:
            print("Column must be an integer between 1 and 8. Row must be a letter between A and H.")
            continue

        x, y = legalcol.index(col), row-1

        if board[y][x] != "-":
            print("That space is already taken.")
            continue

        return x, y
# evaluation function

# alpha beta serach

def terminal(state):
    # returns true if someone won or the board is filled

def successors(state):
    # returns a list of (action, new board) for every neighbor

def utility(state):
    # return big pos number if computer wins, big neg number if computer loses, or evaluation(state) if we're still playing

def maxValue(state, alpha, beta):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for a,s in successors(state):
        v = max(v, minValue(s, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValue(state, alpha, beta):
    if terminal(state):
        return utility(state)
    v = math.inf
    for a,s in successors(state):
        v = min(v, maxValue(s, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alphaBetaSearch(board):
    v = maxValue(state, -inf, inf)
    # need to figure out how to identify the sucessor that gives us v value 
    return action

def printBoard(board):
    print(" 1 2 3 4 5 6 7 8")
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in range(8):
        print(rows[i], end=" ")

        for j in range(8):
            print(board[i][j], end="")

        print()



# main ()
def main():
    ...

if __name__ == "__main__":
    main()