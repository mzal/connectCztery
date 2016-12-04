from graphics import *
from random import *


WIN_TITLE = "ConnectCztery"
COL = 7
ROW = 6
WIN_X = 700
WIN_Y = 700 * ROW/COL
RADIUS = 3/4 * WIN_X / (2*COL)
background_color = "white"
TL = 4
#TL = Target Length

def win_check(board):
    for i in range(COL):
        for j in range(ROW-TL+1):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i][j+k]==1):
                    a+=1
                if(board[i][j+k]==2):
                    b+=1
            if(a==TL):
                return 1
            if(b==TL):
                return 2
    for i in range(COL-TL+1):
        for j in range(ROW):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+k][j]==1):
                    a+=1
                if(board[i+k][j]==2):
                    b+=1
            if(a==TL):
                return 1
            if(b==TL):
                return 2
    for i in range(COL-TL+1):
        for j in range(ROW-TL+1):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+k][j+k]==1):
                    a+=1
                if(board[i+k][j+k]==2):
                    b+=1
            if(a==TL):
                return 1
            if(b==TL):
                return 2
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+TL-k-1][j+k]==1):
                    a+=1
                if(board[i+TL-k-1][j+k]==2):
                    b+=1
            if(a==TL):
                return 1
            if(b==TL):
                return 2
    return 0

def draw_grid(win):
    win.setBackground(background_color)
    for i in range(1,COL):
        l = Line( Point(i*WIN_X/COL, 0), Point(i*WIN_X/COL, WIN_Y) )
        l.draw(win)
    for i in range(1,ROW):
        l = Line( Point(0, i*WIN_Y/ROW), Point(WIN_X, i*WIN_Y/ROW) )
        l.draw(win)

def draw_circle(win, board, filled, col_num, player):
    row_num = filled[col_num]
    board[col_num][ROW - row_num - 1] = player
    filled[col_num] += 1
    c = Circle( Point(WIN_X/(2*COL) + col_num*WIN_X/COL, WIN_Y/(2*ROW) + (ROW - row_num - 1)*WIN_Y/ROW), RADIUS )
    if (player == 1):
        c.setFill("yellow")
        c.setOutline("yellow")
    else:
        c.setFill("red")
        c.setOutline("red")
    c.draw(win)

def main():
    win = GraphWin(WIN_TITLE, WIN_X, WIN_Y)
    game_history = []
    board = []
    filled = []
    for i in range(COL):
        filled.append(0)

    for i in range(COL):
        board.append([])
        for j in range(ROW):
            board[i].append(0)

    draw_grid(win)
    winner = 0
    game_history.append(board)
    for i in range(COL*ROW):
        #Player 1
        move = int(win.getKey()) - 1
        while filled[move] == ROW:
            move = int(win.getKey()) - 1
        draw_circle(win, board, filled, move, 1)
        winner = win_check(board)
        game_history.append(board)
        if(winner!=0):
            break
        #Player 2
        move = randint(0,COL-1)
        while filled[move] == ROW:
            move = randint(0,COL-1)
        draw_circle(win, board, filled, move, 2)
        winner = win_check(board)
        game_history.append(board)
        if(winner!=0):
            break
    if(winner==1):
        t=Text(Point(WIN_X/2,WIN_Y/2),"Yellow wins ;)")
    if(winner==2):
        t=Text(Point(WIN_X/2,WIN_Y/2),"Red wins :C")
    if(winner==0):
        t=Text(Point(WIN_X/2,WIN_Y/2),"That's a draw! :O")
    t.setSize(30)
    t.setTextColor("blue")
    t.draw(win)
    win.getKey()
main()
