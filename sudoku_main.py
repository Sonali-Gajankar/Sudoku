board = [
    [0, 0, 6, 0, 5, 4, 9, 0, 0],
    [1, 0, 0, 0, 6, 0, 0, 4, 2],
    [7, 0, 0, 0, 8, 9, 0, 0, 0],
    [0, 7, 0, 0, 0, 5, 0, 8, 1],
    [0, 5, 0, 3, 4, 0, 6, 0, 0],
    [4, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 3, 4, 0, 0, 0, 1, 0, 0],
    [9, 0, 0, 8, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 0, 3, 0, 7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # Square
    sq_x = pos[1] // 3
    sq_y = pos[0] // 3

    for i in range(sq_y * 3, sq_y * 3 + 3):
        for j in range(sq_x * 3, sq_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(str(b[i][j]) + " ", end="")
            if j == 8:
                print("")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # return indexes as tuples
    return None


print("Sudoku board")
print_board(board)
solve(board)
print("\nSolved board: ")
print("----------------------------------------------------------")
print_board(board)
