import curses

matrix = [
    [".", ".", ".", "X", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", "T", ".", ".", ".", "."],
    [".", ".", "F", ".", ".", "."],
]

def print_matrix(stdscr, x_pos, y_pos):
    stdscr.clear()
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if i == y_pos and j == x_pos:
                stdscr.addstr("X ")
            else:
                stdscr.addstr(char + " ")
        stdscr.addstr("\n")
    stdscr.refresh()

def move(stdscr, x_pos, y_pos):
    key = ""
    while key != ord("q"):
        key = stdscr.getch()
        if key == curses.KEY_UP and y_pos > 0:
            y_pos -= 1
        elif key == curses.KEY_DOWN and y_pos < len(matrix) - 1:
            y_pos += 1
        elif key == curses.KEY_LEFT and x_pos > 0:
            x_pos -= 1
        elif key == curses.KEY_RIGHT and x_pos < len(matrix[0]) - 1:
            x_pos += 1
        print_matrix(stdscr, x_pos, y_pos)

def main(stdscr):
    curses.curs_set(0)
    x_pos = 3
    y_pos = 0
    print_matrix(stdscr, x_pos, y_pos)
    move(stdscr, x_pos, y_pos)

curses.wrapper(main)
