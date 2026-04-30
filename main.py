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
    legalcol = list(range(1,9))

    while True:
        move = input("Choose your next move: ").strip()
    
        if len(move) != 2:
            print("Invalid input. Please enter a move like D4.")
            continue
        
        row, col = move[0].lower() , int(move[1])

        if col not in legalcol or row not in legalrow:
            print("Column must be an integer between 1 and 8. Row must be a letter between A and H.")
            continue

        x, y = legalcol.index(col), legalrow.index(row)

        if board[y][x] != "-":
            print("That space is already taken.")
            continue

        return x, y
# evaluation function

# alpha beta search

def terminal(state):
    # returns true if someone won or the board is filled
    # if someone won, return true
    if not np.any(state == '-'):
        return True

def successors(state, player):
    # returns a list of (action, new board) for every neighbor
    # player as X or O for which player it is
    succs = []
    for row in range(8):
        for col in range(8):
            if state[row][col] == "-":
                newstate = state.copy()
                newstate[row][col] = player
                succs.append(((row, col), newstate))
    return succs

def utility(state, player):
    # return big pos number if computer wins, big neg number if computer loses, or evaluation(state) if we're still playing

def maxValue(state, alpha, beta, player):
    if terminal(state):
        return utility(state, player)
    v = -math.inf
    opp = 'O' if player == 'X' else 'X'
    for a,s in successors(state, player):
        v = max(v, minValue(s, alpha, beta, player))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValue(state, alpha, beta, player):
    if terminal(state):
        return utility(state, player)
    v = math.inf
    opp = 'O' if player == 'X' else 'X'
    for a,s in successors(state, opp):
        v = min(v, maxValue(s, alpha, beta, player))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alphaBetaSearch(board, player):
    v = maxValue(board, -math.inf, math.inf, player)
    opp = 'O' if player == 'X' else 'X'
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