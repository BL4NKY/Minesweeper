from tile import Tile
from random import randint

class Board(object):
    def __init__(self, row, column, number_mines):
        self.row = row
        self.column = column
        self.number_mines = number_mines
        self.board = []
        for i in range (self.row):
            self.board.append([])
            for j in range (self.column):
                self.board[i].append(Tile())
        self.place_mines()
        self.check_adj_mines()
                
    def get_row(self):
        return self.row
        
    def set_row(self, row):
        self.row = row
    
    def get_column(self):
        return self.column
        
    def set_column(self, column):
        self.column = column
        
    def get_number_mines(self):
        return self.number_mines
        
    def set_number_mines(self, number_mines):
        self.number_mines = number_mines
    
    def __str__(self):
        row_num = "  |"
        line = "-+"
        matrix = ""
        for k in range (self.column):
            if k < 10:
                row_num += " " + str(k) + "|"
            else:
                row_num += str(k) + "|"
            line +=  "--+"
        line += "-"
        for l in range(self.row):
            for m in range (self.column+1):
                if m == 0:
                    if l < 10:
                        matrix += " " + str(l) + "|"
                    else:
                        matrix += str(l) + "|"
                else:
                    matrix += str(self.board[l][m-1])
            matrix += "\n"                    
        final_board = row_num + "\n" + line + "\n" +  matrix + line
        return final_board

    def place_mines(self):
        i = 0
        while i != self.number_mines:
            x_rand = randint(0, self.row-1)
            y_rand = randint(0, self.column-1)
            if self.check_if_mine(x_rand, y_rand) == False:
                self.board[x_rand][y_rand].set_mine(True)
#                self.board[x_rand][y_rand].set_uncovered(True)
                i = i + 1
        
    def check_if_mine(self, x, y):
        if self.board[x][y].get_mine() == True:
            return True
        else:
            return False
    
    def put_flag(self, x, y):      
        if self.check_if_flag(x, y) == True:
            return False
        else:
            self.board[x][y].set_flag(True)
        
    def check_if_flag(self, x, y):
        if self.board[x][y].get_flag() == True:
            return True
        else:
            return False
    
    def put_interrogant(self, x, y): 
        if self.check_if_interrogant(x, y) == True:
            return False
        else:
            self.board[x][y].set_interrogant(True)
            
        
    def check_if_interrogant(self, x, y):
        if self.board[x][y].get_interrogant() == True:
            return True
        else:
            return False
        
    def uncover_tile(self, x, y):
        if self.check_if_uncover(x, y) == True:
            return False
        else:
            self.board[x][y].set_uncover(True)
        
    def chek_if_uncover(self, x, y):
        if self.board[x][y].get_uncover() == True:
            return True
        else:
            return False
    def check_adj_mines(self): 
        surrounding = ((-1, -1), (-1,  0), (-1,  1), (0, -1), (0,  1), (1, -1), (1,  0), (1,  1))
        for i in range (self.row):
            for j in range (self.column):
                if self.check_if_mine(i, j) == True:
                    for (sur_x, sur_y) in surrounding:
                        if i + sur_x >= 0 and j + sur_y >= 0 and i + sur_x < self.row and j + sur_y < self.column:
                            self.board[i + sur_x][j + sur_y].add_adj_mine()
        for k in range (self.row):
            for l in range (self.column):
                if self.board[k][l].get_adj_mine() == 0:
                    self.board[k][l].set_adj_mine(" ")
                elif self.board[k][l].get_adj_mine() == 1:
                    self.board[k][l].set_adj_mine("\033[34m1\033[0m")
                elif self.board[k][l].get_adj_mine() == 2:
                    self.board[k][l].set_adj_mine("\033[32m2\033[0m")
                elif self.board[k][l].get_adj_mine() == 3:
                    self.board[k][l].set_adj_mine("\033[31m3\033[0m")
                elif self.board[k][l].get_adj_mine() == 4:
                    self.board[k][l].set_adj_mine("\033[35m4\033[0m")
                elif self.board[k][l].get_adj_mine() == 5:
                    self.board[k][l].set_adj_mine("\033[33m5\033[0m")
                elif self.board[k][l].get_adj_mine() == 6:
                    self.board[k][l].set_adj_mine("\033[30m6\033[0m")
                elif self.board[k][l].get_adj_mine() == 7:
                    self.board[k][l].set_adj_mine("\033[93m7\033[0m")
                else:
                    self.board[k][l].set_adj_mine("\033[36m8\033[0m")
                    
    def uncover_adj(self,x,y):
        self.board[x][y].set_uncovered(True)
        surrounding = ((-1, -1), (-1,  0), (-1,  1), (0 , -1), (0 ,  1), (1 , -1), (1 ,  0), (1 ,  1))
        for (sur_x, sur_y) in surrounding:   
            if 0 <= x + sur_x and x + sur_x < self.row and 0 <= y + sur_y and y + sur_y < self.column and self.board[x + sur_x][y + sur_y].get_uncovered() != True and self.board[x][y].get_adj_mine() == " ":
                    if self.board[x + sur_x][y + sur_y].get_flag() != True and self.board[x + sur_x][y + sur_y].get_question() != True:
                        if self.board[x + sur_x][y + sur_y].get_adj_mine() == " ":            
                            self.board[x + sur_x][y + sur_y].set_uncovered(True)
                            self.uncover_adj(x + sur_x, y + sur_y)
                        elif self.board[x + sur_x][y + sur_y].get_adj_mine() != " ":
                            self.board[x + sur_x][y + sur_y].set_uncovered(True)