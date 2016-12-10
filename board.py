from static_values import *
import copy

class Board():

    def __getitem__(self,index):
        return self.tab[index]

    def __init__(self,*board):
        self.tab = [[0 for i in range(ROW)] for j in range(COL)]
        self.filled = [0 for i in range(COL)]
        self.turn = 1
        if(board):
            brd=board[0]
            for i in range(COL):
               for j in range(ROW):
                    self[i][j]=brd[i][j]
            for i in range(COL):
                self.filled[i]=brd.filled[i]
            self.turn = brd.turn

    def __str__(self):
        s = ""
        for i in range(ROW-1,-1,-1):
            for j in range(COL):
                s+=str(self[j][i])
            s+='\n'
        return s

    def __repr__(self):
        return self.__str__()

    def move(self,index):
        if(self.filled[index]==ROW):
            return False
        self[index][self.filled[index]]=self.turn
        self.filled[index]+=1
        self.turn=3-self.turn
        return True