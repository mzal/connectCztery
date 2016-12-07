from win_check import *

v = [0,1,5,20]

def evaluate2(board,first,second):
    points = 0
    if(win_check(board)==second):
        points=1000000000
        return points
    if(win_check(board)==first):
        points=-1000000000
        return points
    for i in range(COL):
        for j in range(ROW-TL+1):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i][j+k]==first):
                    a+=1
                if(board[i][j+k]==second):
                    b+=1
            if(a==0):
                points+=v[b]
            if(b==0):
                points-=v[a]
    for i in range(COL-TL+1):
        for j in range(ROW):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+k][j]==first):
                    a+=1
                if(board[i+k][j]==second):
                    b+=1
            if(a==0):
                points+=v[b]
            if(b==0):
                points-=v[a]
    for i in range(COL-TL+1):
        for j in range(ROW-TL+1):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+k][j+k]==first):
                    a+=1
                if(board[i+k][j+k]==second):
                    b+=1
            if(a==0):
                points+=v[b]
            if(b==0):
                points-=v[a]
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+TL-k-1][j+k]==first):
                    a+=1
                if(board[i+TL-k-1][j+k]==second):
                    b+=1
            if(a==0):
                points+=v[b]
            if(b==0):

                points-=v[a]
    return points
