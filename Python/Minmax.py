import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner(player):
    win_pos = [(0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_pos)

def is_draw():
    return " " not in board



def minimax(alpha, beta, is_max):

    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(alpha, beta, False)
                board[i] = " "

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break   

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(alpha, beta, True)
                board[i] = " "

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break   

        return best


def best_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(-math.inf, math.inf, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"



while True:
    print_board()

    pos = int(input("Enter position (0-8): "))
    board[pos] = "X"

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    best_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break