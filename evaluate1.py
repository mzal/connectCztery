from win_check import *

v = [0,1,5,20,1000000000]

def evaluate1(board,first,second):
    win=win_check(board)
    if(win==second):
        return 9000000000
    if(win==first):
        return -9000000000
    points = 0
    for i in range(COL):
        for j in range(ROW):
            if(board[i][j]!=0):
                continue
            maks=0
            mini=0
            xdf=min((TL-1,i))
            xdl=max((0,i-COL+TL))
            ydf=min((TL-1,j))
            ydl=max((0,j-ROW+TL))
            for k in range(xdf,xdl-1,-1):
                a=0
                b=0
                for l in range(TL):
                    if(board[i-k+l][j]==first):
                        a+=1
                    if(board[i-k+l][j]==second):
                        b+=1
                if(a==0):
                    maks=max((maks,v[b]))
                if(b==0):
                    mini=max((mini,v[a]))
            for k in range(ydf,ydl-1,-1):
                a=0
                b=0
                for l in range(TL):
                    if(board[i][j-k+l]==first):
                        a+=1
                    if(board[i][j-k+l]==second):
                        b+=1
                if(a==0):
                    maks=max((maks,v[b]))
                if(b==0):
                    mini=max((mini,v[a]))
            for k in range(min((xdf,ydf)),max((xdl,ydl))-1,-1):
                a=0
                b=0
                for l in range(TL):
                    if(board[i-k+l][j-k+l]==first):
                        a+=1
                    if(board[i-k+l][j-k+l]==second):
                        b+=1
                if(a==0):
                    maks=max((maks,v[b]))
                if(b==0):
                    mini=max((mini,v[a]))
            for k in range(min((xdf,TL-ydl-1)),max((xdl,TL-ydf-1)),-1):
                a=0
                b=0
                for l in range(TL):
                    if(board[i-k+l][j+k-l]==first):
                        a+=1
                    if(board[i-k+l][j+k-l]==second):
                        b+=1
                if(a==0):
                    maks=max((maks,v[b]))
                if(b==0):
                    mini=max((mini,v[a]))
            points+=maks
            points-=mini
    return points
