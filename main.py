import numpy as np
import math
import time

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
        print()
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

def checkWinner(board):
    # check horizontal wins
    for r in range(8):
        for c in range(8 - 4 + 1):           # cols 0-4
            window = [board[r][c+k] for k in range(4)]
            if window.count("X") == 4: return "X"
            if window.count("O") == 4: return "O"

    # check vertical wins
    for c in range(8):
        for r in range(8 - 4 + 1):           # rows 0-4
            window = [board[r+k][c] for k in range(4)]
            if window.count("X") == 4: return "X"
            if window.count("O") == 4: return "O"

    # no diagonals per spec
    return None                               # no winner yet

def evaluate(board):
    ### evaluate score for human and player threats

    # check terminal states first
    winner = checkWinner(board)
    if winner == "X": return  1_000_000   # computer wins
    if winner == "O": return -1_000_000   # human wins

    # initialize score to 0
    score = 0

    # add to score for computer threat, subtract for human threat
    score += evaluatePlayer(board, "X")
    score -= evaluatePlayer(board, "O") * 2 # prefers to block human threat

    # bonus for double threats (two simultaneous 3-in-a-rows = unblockable)
    score += doubleThreatBonus(board, "X")
    score -= doubleThreatBonus(board, "O") * 2 # prefers to block human threat

    # small center bias: center columns appear in more windows
    score += centerBias(board, "X")
    score -= centerBias(board, "O")

    return score

# given a board and player, evaluate player score
def evaluatePlayer(board, player):
    # Scan all lines on board and score windows of 4 for given player
    score = 0

    for window in getAllWindows(board):
        score += scoreWindow(window, player)

    return score

def doubleThreatBonus(board, player):
    # Count open threats: windows where player has 3 pieces and 1 empty
    # Two or more at once = effectively unblockable position
    threats = sum(
        1 for w in getAllWindows(board)
        if w.count(player) == 3 and w.count("-") == 1
    )
    return 50_000 if threats >= 2 else 0

def centerBias(board, player):
    # Center columns (3 and 4, 0-indexed) participate in more windows of 4
    score = 0
    for r in range(8):
        for c in [3, 4]:
            if board[r][c] == player:
                score += 30
    return score

def getAllWindows(board):
    windows = []

    # scan all horizontal windows of 4
    for r in range(8):
        for c in range(8 - 4 + 1):           # cols 0-4 (5 starting positions)
            windows.append([board[r][c+k] for k in range(4)])

    # scan all vertical windows of 4
    for c in range(8):
        for r in range(8 - 4 + 1):           # rows 0-4 (5 starting positions)
            windows.append([board[r+k][c] for k in range(4)])

    # no diagonals — spec says diagonals do NOT count

    return windows

def scoreWindow(window, player):
    opponent = "O" if player == "X" else "X"

    # if opponent is anywhere in the window, it's blocked — worthless
    if opponent in window:
        return 0

    count = window.count(player)

    # map piece count to score (exponential so 3-in-a-row > ten 2-in-a-rows)
    if count == 4: return 100_000    # winning window
    if count == 3: return  10_000    # one away from winning
    if count == 2: return    100     # building a threat
    return 0


# alpha beta search

def terminal(state):
    if checkWinner(state) is not None:
        return True
    if all(state[r][c] != "-" for r in range(8) for c in range(8)):
        return True
    return False

def successors(state, player):
    # returns a list of (action, new board) for every neighbor
    # player as X or O for which player it is
    succs = []
    for row in range(8):
        for col in range(8):
            if state[row][col] == "-":
                newstate = [r[:] for r in state]
                newstate[row][col] = player
                succs.append(((row, col), newstate))
    return succs

def utility(state, player):
    return evaluate(state)

def maxValue(state, alpha, beta, player, depth, deadline):
    if terminal(state) or depth == 0 or time.perf_counter() >= deadline:
        return utility(state, player)
    v = -math.inf
    opp = 'O' if player == 'X' else 'X'
    for a,s in successors(state, player):
        v = max(v, minValue(s, alpha, beta, player, depth - 1, deadline))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValue(state, alpha, beta, player, depth, deadline):
    if terminal(state) or depth == 0 or time.perf_counter() >= deadline:
        return utility(state, player)
    v = math.inf
    opp = 'O' if player == 'X' else 'X'
    for a,s in successors(state, opp):
        v = min(v, maxValue(s, alpha, beta, player, depth - 1, deadline))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

def alphaBetaSearch(board, player, think_time=5):
    deadline = time.perf_counter() + think_time
    best_action = None

    for depth in range(1, 65):
        if time.perf_counter() >= deadline:
            break
        current_best_action = None
        current_best_score = -math.inf
        for action, state in successors(board, player):
            if time.perf_counter() >= deadline:
                break
            score = minValue(state, -math.inf, math.inf, player, depth - 1, deadline)
            if score > current_best_score:
                current_best_score = score
                current_best_action = action
        # only update best_action if we finished this depth completely
        if time.perf_counter() < deadline and current_best_action is not None:
            best_action = current_best_action
        if current_best_score >= 1_000_000:
            break   # found a guaranteed win, stop early

    return best_action

def printBoard(board):
    print("  1 2 3 4 5 6 7 8")
    rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    for i in range(8):
        print(rows[i], end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print()

# main ()
def main():
    board = [["-"] * 8 for _ in range(8)]
    first, think = getinput()
    human_turn = (first == "y")
    row_labels = ['a','b','c','d','e','f','g','h']

    printBoard(board)

    while True:
        if human_turn:
            x, y = getmove(board)
            board[y][x] = "O"
            printBoard(board)
            if checkWinner(board) == "O":
                print()
                print("You win! Game Over!")
                break
        else:
            print()
            print("Computer is thinking...")
            action = alphaBetaSearch(board, "X", think)
            if action:
                row, col = action
                board[row][col] = "X"
                label = f"{row_labels[row].upper()}{col+1}"
                print()
                print(f"Computer plays: {label}")
                printBoard(board)
                if checkWinner(board) == "X":
                    print()
                    print("Computer wins! Game Over!")
                    break

        if all(board[r][c] != "-" for r in range(8) for c in range(8)):
            print()
            print("\nIt's a draw! Game Over!")
            break

        human_turn = not human_turn

if __name__ == "__main__":
    main()