from static_values import *

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

