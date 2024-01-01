def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(grid, row, col, num):
    return (
        not used_in_row(grid, row, num)
        and not used_in_col(grid, col, num)
        and not used_in_box(grid, row - row % 3, col - col % 3, num)
    )

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    return num in [grid[row][col] for row in range(9)]

def used_in_box(grid, start_row, start_col, num):
    for row in range(3):
        for col in range(3):
            if grid[row + start_row][col + start_col] == num:
                return True
    return False

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    if solve_sudoku(sudoku_grid):
        print("Solved Sudoku:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")
