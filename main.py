from graphics import *
from random import *
from evaluate1 import *
from evaluate2 import *
from static_values import *
from win_check import *
from board import *
from draw_board import *

game_history = []

def ev(i,board,player):
    if(i==1):
        if(player==0):
            return evaluate1(board,v1)
        if(player==1):
            return evaluate2(board,v2)
    if(i==2):
        if(player==0):
            return evaluate2(board,v1)
        if(player==1):
            return evaluate2(board,v2)

def a(x,y):
    return x<y
def b(x,y):
    return x>y

def move(player,board,win):
    player-=1
    if(player==0):
        ai=player1
        opp=player2
    if(player==1):
        ai=player2
        opp=player1
    if(debug):
        print("Player {} moves..".format(player+1))
    if(control[ai]["manual"]):
        m=int(win.getKey())-1
        while(not board.move(m)):
            m=int(win.getKey())-1
        if(m==-1):
            return False
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
                val=ev(control[ai]["ev"],newboard2,player)
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
        if(debug):
            print("Value of move {} is {}".format(best,ex))
    elif(control[ai]["AI"]=="debug"):
        newboard=Board(board)
        print("Before:")
        print(board)
        newboard.move(0)
        print("After:")
        print(board)
    if(debug):
        print(board)
    if(__name__=="__main__"):
        draw_board(board,win)
    return True

def main(*args):
    win=None
    if(__name__=="__main__"):
        win = GraphWin(WIN_TITLE, WIN_X, WIN_Y)
        draw_grid(win)
    else:
        global v1
        global v2
        v1 = args[0]
        v2 = args[1]
    board = Board()
    filled = []
    playermoves = []
    winner = 0
    game_history.append(Board(board))
    p=1
    for i in range(int(COL*ROW)):
        ai=player1
        opp=player2
        if(p==2):
            ai,opp=opp,ai
        if(not move(p,board,win)):
            if(control[opp]["manual"]):
                board=game_history[-2]
                game_history.pop(-1)
                game_history.pop(-1)
                i-=2
            else:
                board=game_history[-3]
                game_history.pop(-1)
                game_history.pop(-1)
                game_history.pop(-1)
                i-=3
                p=3-p
            draw_board(board,win)
        game_history.append(Board(board))
        winner=win_check(board)
        if(winner!=0):
            break
        p=3-p
    if(__name__=="__main__"):
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
        filename="games/game"
        it=0
        try:
            while(True):
                string=filename+str(it)+".txt"
                file=open(string,mode="r")
                file.close()
                it+=1
        except:
            pass
        finally:
            string=filename+str(it)+".txt"
            file=open(string,mode="w")
            for i in game_history:
                file.write(str(i))
                file.write("\n")
            file.close()
        win.getKey()
    else:
        return winner
if(__name__=="__main__"):
    main()