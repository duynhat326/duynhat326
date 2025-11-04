import copy
from typing import List, Tuple

Board = List[List[int]]


def print_board(board: Board) -> None:
    """Display the Sudoku board in a user-friendly layout."""
    horizontal_sep = "+-------+-------+-------+"
    for i, row in enumerate(board):
        if i % 3 == 0:
            print(horizontal_sep)
        row_display = []
        for j, value in enumerate(row):
            if j % 3 == 0:
                row_display.append("|")
            row_display.append(str(value) if value != 0 else ".")
        row_display.append("|")
        print(" ".join(row_display))
    print(horizontal_sep)


def find_empty(board: Board) -> Tuple[int, int] | None:
    """Return the coordinates of the first empty cell or None if solved."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board: Board, row: int, col: int, value: int) -> bool:
    """Check whether placing value at board[row][col] is valid."""
    if any(board[row][c] == value for c in range(9)):
        return False
    if any(board[r][col] == value for r in range(9)):
        return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == value:
                return False
    return True


def solve(board: Board) -> bool:
    """Backtracking solver that modifies the board in place."""
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for value in range(1, 10):
        if is_valid(board, row, col, value):
            board[row][col] = value
            if solve(board):
                return True
            board[row][col] = 0
    return False


def play_game(initial_board: Board) -> None:
    """Run a simple command-line Sudoku game."""
    board = copy.deepcopy(initial_board)
    solution = copy.deepcopy(initial_board)
    solve(solution)

    print("Chào mừng bạn đến với Sudoku! Nhập 'solve' để xem lời giải hoặc 'quit' để thoát.")
    while True:
        print_board(board)
        user_input = input("Nhập vị trí và giá trị (ví dụ 1 3 9): ").strip().lower()

        if user_input in {"quit", "exit"}:
            print("Tạm biệt!")
            break
        if user_input == "solve":
            print("Lời giải:")
            print_board(solution)
            continue

        try:
            row_str, col_str, value_str = user_input.split()
            row = int(row_str) - 1
            col = int(col_str) - 1
            value = int(value_str)
        except ValueError:
            print("Vui lòng nhập 3 số: hàng, cột và giá trị (1-9).")
            continue

        if not (0 <= row < 9 and 0 <= col < 9):
            print("Hàng và cột phải nằm trong khoảng 1-9.")
            continue
        if initial_board[row][col] != 0:
            print("Ô này là cố định, không thể thay đổi.")
            continue
        if not (1 <= value <= 9):
            print("Giá trị phải nằm trong khoảng 1-9.")
            continue
        if not is_valid(board, row, col, value):
            print("Nước đi không hợp lệ, hãy thử lại.")
            continue

        board[row][col] = value
        if board == solution:
            print_board(board)
            print("Chúc mừng! Bạn đã hoàn thành Sudoku!")
            break


if __name__ == "__main__":
    PUZZLE: Board = [
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
    play_game(PUZZLE)
