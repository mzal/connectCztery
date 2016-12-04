from win_check import *

v = [0,1,5,20]

def evaluate(board):
    points = 0
    if(win_check(board)==2):
        points=1000000000
        return points
    if(win_check(board)==1):
        points=-1000000000
        return points
    for i in range(COL):
        for j in range(ROW-TL+1):
            a = 0
            b = 0
            for k in range(TL):
                if(board[i][j+k]==1):
                    a+=1
                if(board[i][j+k]==2):
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
                if(board[i+k][j]==1):
                    a+=1
                if(board[i+k][j]==2):
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
                if(board[i+k][j+k]==1):
                    a+=1
                if(board[i+k][j+k]==2):
                    b+=1
            if(a==0):
                points+=v[b]
            if(b==0):
                points-=v[a]
            a = 0
            b = 0
            for k in range(TL):
                if(board[i+TL-k-1][j+k]==1):
                    a+=1
                if(board[i+TL-k-1][j+k]==2):
                    b+=1
            if(a==0):
                points+=v[b]
            if(b==0):
                points-=v[a]
    return points