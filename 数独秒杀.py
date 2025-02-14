import random

def get_sudoku(sudoku):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

    if not empty_cells:
        return sudoku

    # 按顺序选择第一个空格
    cell = empty_cells[0]

    for num in range(1, 10):
        if is_valid(sudoku, cell, num):
            sudoku[cell[0]][cell[1]] = num
            if get_sudoku(sudoku):
                return sudoku
            sudoku[cell[0]][cell[1]] = 0

    return None

def is_valid(sudoku, cell, num):
    row, col = cell

    # 检查行和列
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # 检查 3x3 方格
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[row_start + i][col_start + j] == num:
                return False

    return True

def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # 打印分隔线
        print(" ".join(str(x) if x != 0 else '.' for x in row[:3]) + " | " +
              " ".join(str(x) if x != 0 else '.' for x in row[3:6]) + " | " +
              " ".join(str(x) if x != 0 else '.' for x in row[6:]))

# 初始数独
sudoku = [
    [0, 0, 0, 6, 0, 0, 0, 5, 0],
    [8, 0, 4, 0, 0, 0, 6, 0, 0],
    [0, 2, 0, 0, 8, 0, 0, 3, 0],
    [0, 0, 0, 7, 0, 3, 0, 0, 4],
    [0, 0, 6, 0, 5, 0, 1, 0, 0],
    [3, 0, 0, 1, 0, 8, 0, 0, 0],
    [0, 7, 0, 0, 1, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 3, 0, 1],
    [0, 9, 0, 0, 0, 7, 0, 0, 0],
]

# 解决数独
sudoku = get_sudoku(sudoku)


# 打印数独
print_sudoku(sudoku)