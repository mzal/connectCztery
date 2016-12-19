from static_values import *
from graphics import *


def draw_grid(win):
    win.setBackground(background_color)
    for i in range(1,COL):
        l = Line( Point(i*(WIN_X)/COL,0), Point(i*(WIN_X)/COL, WIN_Y))
        l.draw(win)
    for i in range(1,ROW+1):
        l = Line( Point(0, i*(WIN_Y-BASE)/ROW), Point(WIN_X, i*(WIN_Y-BASE)/ROW) )
        l.draw(win)
    for i in range(1,COL+1):
        u=Text(Point(i*WIN_X/COL - WIN_X/(2*COL), WIN_Y-BASE/2),str(i))
        u.setSize(11)
        u.setTextColor("blue")
        u.draw(win)


def draw_board(board,win):
    draw_grid(win)
    for i in range(COL):
        for j in range(ROW):
            if(board[i][j]==0):
                x="white"
            elif(board[i][j]==1):
                x="yellow"
            elif(board[i][j]==2):
                x="red"
            c=Circle( Point(WIN_X/(2*COL) + i*WIN_X/COL, (WIN_Y-BASE)/(2*ROW) + (ROW - j- 1)*(WIN_Y-BASE)/ROW), RADIUS)
            c.setFill(x)
            c.setOutline(x)
            c.draw(win)
