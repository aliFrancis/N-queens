import numpy as np




class Board():


    def __init__(self, side_length,pieces = None):
        self.shape = [side_length,side_length]
        self.grid = np.empty(self.shape+[2],dtype=bool)
        if pieces is None:
            self.pieces = {'black':[],'white':[]}
        else:
            self.pieces = pieces


    def is_valid(self):
        condition = True
        for piece in self.pieces['black']:
            condition = self.is_valid_piece_against(piece,self.pieces['white'])
            if not condition:
                return False


    def add_piece(self,piece):
        self.pieces[piece.colour].append({'ID':self.get_new_ID,'x':piece.x,'y':piece.y,'position':piece.position})

    def is_filled_at(self,position):
        if any(self.grid[position[0],position[1]]):
            return True
        else:
            return False

    def get_new_ID(self):
        return 1
