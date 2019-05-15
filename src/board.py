import numpy as np


class Board():
    def __init__(self, side_length,pieces = None):
        self.shape = [side_length,side_length]
        self.grid = np.zeros(self.shape+[2],dtype=bool)
        if pieces is None:
            self.pieces = {'black':[],'white':[]}
        else:
            self.pieces = pieces

    def is_valid(self):
        condition = True
        for piece in self.pieces['black']:
            condition = piece.is_valid()
            if not condition:
                return False
        return True

    def add_piece(self,piece):
        self.pieces[piece.colour].append(piece)
        if piece.colour=='black':
            self.grid[piece.x,piece.y,0] = True
        elif piece.colour=='white':
            self.grid[piece.x,piece.y,1] = True

    def is_filled_at(self,position):
        if any(self.grid[position[0],position[1]]):
            return True
        else:
            return False

    def get_new_ID(self):
        return 1

    def get_full_vision_grid(self):
        black_vision_grid = np.zeros(self.shape)
        white_vision_grid = np.zeros(self.shape)

        for piece in self.pieces['black']:
            black_vision_grid+=piece.get_vision_grid()
        for piece in self.pieces['white']:
            white_vision_grid+=piece.get_vision_grid()

        self.vision_grid = np.concatenate(black_vision_grid,white_vision_grid,axis=2)

    def __str__(self):
        disp = np.empty(self.shape,dtype='str')
        disp[self.grid[...,0]==1] = 'B'
        disp[self.grid[...,1]==1] = 'W'
        disp[disp==''] = '+'
        string = '-'*2*disp.shape[0]+'\n'
        for i in range(disp.shape[1]):
            string
            for j in range(disp.shape[0]):
                string+=disp[j,i]+' '
            string+='\n'
        return string
