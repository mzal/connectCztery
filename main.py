from graphics import *
from random import *
from evaluate1 import *
from evaluate2 import *
from static_values import *
from win_check import *
import copy

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

def draw_circle(win, board, filled, col_num, player,sim=False):
    if(sim):
        t_board=[]
        for i in range(COL):
            t_board.append(list(board[i]))
        t_filled=copy.copy(filled)
        row_num=filled[col_num]
        t_board[col_num][ROW-row_num-1]=player
        t_filled[col_num]+=1
        return (t_board,t_filled)
    row_num = filled[col_num]
    board[col_num][ROW - row_num - 1] = player
    filled[col_num] += 1
    c = Circle( Point(WIN_X/(2*COL) + col_num*WIN_X/COL, (WIN_Y-BASE)/(2*ROW) + (ROW - row_num - 1)*(WIN_Y-BASE)/ROW), RADIUS )
    if (player == 1):
        c.setFill("yellow")
        c.setOutline("yellow")
    else:
        c.setFill("red")
        c.setOutline("red")
    c.draw(win)
    return (board,filled)

def AImove1(win,board,filled,first,second):
    maks=-9000000001
    best=0
    for i in range(COL):
        if(filled[i]==ROW):
            continue
        ev=draw_circle(win,board,filled,i,second,sim=True)
        mini=1000000001
        if(win_check(ev[0])==0):
            for j in range(COL):
                if(ev[1][j]==ROW):
                    continue
                ev2=draw_circle(win,ev[0],ev[1],j,first,sim=True)
                mini=min((mini,evaluate1(ev2[0],first,second)))
        points=mini
        if(points>maks):
            best=i
            maks=points
    if(debug):
        print("Value of move "+str(best)+" is "+str(maks))
    return best

def AImove2(win,board,filled,first,second):
    maks=-9000000001
    best=0
    for i in range(COL):
        if(filled[i]==ROW):
            continue
        ev=draw_circle(win,board,filled,i,2,sim=True)
        mini=1000000001
        if(win_check(ev[0])==0):
            for j in range(COL):
                if(ev[1][j]==ROW):
                    continue
                ev2=draw_circle(win,ev[0],ev[1],j,1,sim=True)
                mini=min((mini,evaluate2(ev2[0],first,second)))
        points=mini
        if(points>maks):
            best=i
            maks=points
    if(debug):
        print("Value of move "+str(best)+" is "+str(maks))
    return best

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
    for i in range(int(COL*ROW/2)):
        #Player 1
        if(player1==1):
            move = int(win.getKey()) - 1
            if(move!=-1):
                while move < 0 or move >= COL or filled[move] == ROW:
                    move = int(win.getKey()) - 1
        if(player1==2):
            move = AImove1(win,board,filled,1,2)
        if(player1==3):
            move = AImove2(win,board,filled,1,2)
        draw_circle(win, board, filled, move, 1)
        winner = win_check(board)
        game_history.append(board)
        if(debug):
            print(board)
        if(winner!=0):
            break
        #Player 2
        if(player2==1):
            move = int(win.getKey()) - 1
            if(move!=-1):
                while move < 0 or move >= COL or filled[move] == ROW:
                    move = int(win.getKey()) - 1
        if(player2==2):
             move = AImove1(win,board,filled,2,1)
        if(player2==3):
             move = AImove2(win,board,filled,2,1)
        draw_circle(win, board, filled, move, 2)
        winner = win_check(board)
        game_history.append(board)
        if(debug):
            print(board)
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
