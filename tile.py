class Tile(object):
    def __init__(self):
        self.uncovered = False
        self.mine = False
        self.flag = False
        self.question = False
        self.adj_mine = 0
        
    def get_uncovered(self):
        return self.uncovered
        
    def set_uncovered(self, uncovered):
        self.uncovered = uncovered
        
    def get_mine(self):
        return self.mine
        
    def set_mine(self, mine):
        self.mine = mine
            
    def get_flag(self):
        return self.flag
                
    def set_flag(self, flag):
        self.flag = flag
        
    def get_question(self):
        return self.question
                
    def set_question(self, question):
        self.question = question
        
    def get_adj_mine(self):
        return self.adj_mine
    
    def set_adj_mine(self, value):
        self.adj_mine = value
                
    def add_adj_mine(self):
        self.adj_mine += 1
        
    def __str__(self):
        if self.flag == True:
                return " !|"
        elif self.question == True:
                return " ?|"
        else:
            if self.uncovered == False:
                return " x|"
            else:
                if self.mine == True:
                    return " *|"
                else:
                    return " " + str(self.adj_mine) + "|"