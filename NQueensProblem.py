""" This file contains the solution code to the N-Queens Problem using recursion, propogation, and backtracking. """

global N
N = 4

# Below is a helper function to check if a queen can be placed on the board in the location board[row][col]. It checks that there are no queens to the left, upper diagonally to the left, and lower diagonally to the left


def is_safe(board, row, col):
    # Check on the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, column):
    # Base case: if all queens are placed, return True
    if column >= N:
        return True

    # Consider the column and try to place queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, column):
            board[i][column] = 1

            # Recur to place queens in rest of columns
            if solve_n_queens(board, column + 1) == True:
                return True

            # If queen placement in position board[i][column] does not lead to a solution, then remove queen from board[i][column]
            board[i][column] = 0

    # If the queen cannot be placed in any rown in the column, then return False
    return False


def print_solution(board):
    for i in range(N):
        print(board[i])


def main():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

    if solve_n_queens(board, 0) == False:
        print("Solution does not exist.")

    else:
        print_solution(board)


main()
