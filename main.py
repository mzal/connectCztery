from graphics import *
from random import *
from evaluate1 import *
from evaluate2 import *
from static_values import *
from win_check import *
from board import *

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


def ev(i,board):
    if(i==1):
        return evaluate1(board)
    if(i==2):
        return evaluate2(board)

def a(x,y):
    return x<y
def b(x,y):
    return x>y

def move(player,board,win):
    player-=1
    if(player==0):
        ai=player1
    if(player==1):
        ai=player2
    if(debug):
        print("Player {} moves..".format(player+1))
    if(control[ai]["manual"]):
        m=int(win.getKey())-1
        while(not board.move(m)):
            pass
    elif(control[ai]["AI"]=="2dminimax"):
        best=0
        if(player==0):
            ex=-1000000000
        if(player==1):
            ex=1000000000
        newboard=Board(board)
        for i in range(COL):
            if(not newboard.move(i)):
                continue
            if(player==0):
                ex2=1000000000
            if(player==1):
                ex2=-1000000000
            newboard2=Board(newboard)
            for j in range(COL):
                if(not newboard2.move(j)):
                    continue
                val=ev(control[ai]["ev"],newboard2)
                #print("After {} and {} moves, the value is {}".format(i,j,val))
                if(player==0 and ex2>val):
                    ex2=val
                if(player==1 and ex2<val):
                    ex2=val
                newboard2=Board(newboard)
            if(player==0 and ex<ex2):
                best=i
                ex=ex2
            if(player==1 and ex>ex2):
                best=i
                ex=ex2
            newboard=Board(board)
        board.move(best)
        print("Value of move {} is {}".format(best,ex))
    elif(control[ai]["AI"]=="debug"):
        newboard=Board(board)
        print("Before:")
        print(board)
        newboard.move(0)
        print("After:")
        print(board)
    print(board)






def main():
    win = GraphWin(WIN_TITLE, WIN_X, WIN_Y)
    game_history = []
    board = Board()
    filled = []
    playermoves = []
    draw_grid(win)
    winner = 0
    game_history.append(Board(board))
    for i in range(int(COL*ROW/2)):
        move(1,board,win)
        game_history.append(Board(board))
        winner=win_check(board)
        if(winner!=0):
            break
        move(2,board,win)
        game_history.append(Board(board))
        winner=win_check(board)
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
    if(debug):
        print("game history:")
        for i in game_history:
            print(i)
    win.getKey()
main()