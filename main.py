from graphics import *
from random import *

FLAT_UI_COLORS = [[color_rgb(26, 188, 156), color_rgb(46, 204, 113), color_rgb(52, 152, 219), color_rgb(155, 89, 182)],
                    [color_rgb(241, 196, 15), color_rgb(230, 126, 34), color_rgb(231, 76, 60), color_rgb(189, 195, 199)]]
WIN_TITLE = "ConnectCztery"
COL = 10
ROW = 6
WIN_X = 700
WIN_Y = 700 * ROW/COL
RADIUS = 3/4 * WIN_X / (2*COL)
COLOR_1 = FLAT_UI_COLORS[0][randint(0,3)]
COLOR_2 = FLAT_UI_COLORS[1][randint(0,3)]
BG_COLOR = "white"

def draw_grid(win):
    for i in range(COL):
        l = Line( Point(i*WIN_X/COL, 0), Point(i*WIN_X/COL, WIN_Y) )
        l.draw(win)
    for i in range(ROW):
        l = Line( Point(0, i*WIN_Y/ROW), Point(WIN_X, i*WIN_Y/ROW) )
        l.draw(win)

def draw_circle(win, board, filled, col_num, player):
    row_num = filled[col_num]
    board[col_num][ROW - row_num - 1] = player
    filled[col_num] += 1
    c = Circle( Point(WIN_X/(2*COL) + col_num*WIN_X/COL, WIN_Y/(2*ROW) + (ROW - row_num - 1)*WIN_Y/ROW), RADIUS )
    if (player == 1):
        c.setFill(COLOR_1)
        c.setOutline(COLOR_1)
    else:
        c.setFill(COLOR_2)
        c.setOutline(COLOR_2)
    c.draw(win)

def main():
    win = GraphWin(WIN_TITLE, WIN_X, WIN_Y)
    win.setBackground(BG_COLOR)
    board = []
    filled = []
    for i in range(COL):
        filled.append(0)

    for i in range(COL):
        board.append([])
        for j in range(ROW):
            board[i].append(0)

    draw_grid(win)
    while True:
        move = int(win.getKey()) - 1
        while filled[move] == ROW:
            move = int(win.getKey()) - 1
        draw_circle(win, board, filled, move, 1)
        move = randint(0,COL-1)
        while filled[move] == ROW:
            move = randint(0,COL-1)
        draw_circle(win, board, filled, move, 2)

main()
