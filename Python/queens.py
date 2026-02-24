N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1

    return False

def print_board(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i] == j else ".", end=" ")
        print()

board = [-1] * N

if solve_queens(board, 0):
    print("8-Queens Solution:")
    print_board(board)
else:
    print("No solution found")
