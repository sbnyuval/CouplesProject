import consts
import screen
board = []
def create():
    for row in range(consts.BOARD_ROWS):
        row = []
        for col in range(consts.BOARD_COLS):
            row.append("EMPTY")
        board.append(row)
    return board
for row in create():
    print(row)
    print()