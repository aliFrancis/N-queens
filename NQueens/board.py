import numpy as np


class Board():
    def __init__(self,shape,pieces = None):
        if isinstance(shape,int):
            self.shape = [shape,shape]
        elif isinstance(shape,list):
            if len(shape)==2:
                self.shape = shape
            else:
                raise "ValueError: shape must be an int or list of length 2"
        self.grid = np.zeros(self.shape+[2],dtype=bool)
        if pieces is None:
            self.pieces = []
        else:
            self.pieces = pieces
            self.reassign_IDs()

    @property
    def ID_list(self):
        IDs = []
        for piece in self.pieces:
            IDs+=[piece.ID]
        return IDs

    @property
    def black_pieces(self):
        return [piece for piece in self.pieces if piece.colour=='black']

    @property
    def white_pieces(self):
        return [piece for piece in self.pieces if piece.colour=='white']

    def is_peaceable(self):
        condition = True
        for piece in self.black_pieces:
            condition = piece.is_peaceable()
            if not condition:
                return False
        return True

    def has_piece(self,ID):
        if ID in self.ID_list:
            return True
        else:
            return False

    def add_piece(self,piece):
        ID = self.next_free_ID()
        self.pieces.append(piece)
        if self.is_filled_at(piece.position):
            position_ID = self.piece_at(piece.position).ID
            raise ValueError('Piece {} placed in already occupied position occupied by {}'.format(ID,position_ID))
        if piece.colour=='black':
            self.grid[piece.x,piece.y,0] = True
        elif piece.colour=='white':
            self.grid[piece.x,piece.y,1] = True
        return ID

    def move_piece(self,ID,new_position):
        piece = self.pieces[self.ID_list.index(ID)]
        self.grid[new_position[0],new_position[1]] = self.grid[piece.x,piece.y]
        self.grid[piece.x,piece.y] = 0
        piece.x = new_position[0]
        piece.y = new_position[1]

    def remove_piece(self,ID,reassign_IDs=False):
        piece_index = self.ID_list.index(ID)
        self.grid[self.pieces[piece_index].x,self.pieces[piece_index].y] = 0
        del self.pieces[piece_index]
        if reassign_IDs:
            self.reassign_IDs()

    def piece_at(self,position):
        if not self.is_filled_at(position):
            return None
        else:
            for piece in self.pieces:
                if piece.position==position:
                    return piece

    def is_filled_at(self,position):
        if any(self.grid[position[0],position[1]]):
            return True
        else:
            return False

    def next_free_ID(self):
        found = False
        ID = 0
        while not found:
            if not self.has_piece(ID):
                found = True
            else:
                ID+=1
        return ID

    def reassign_IDs(self):
        for i,piece in enumerate(self.pieces):
            piece.ID = i

    @property
    def black_grid(self):
        return self.grid[...,0]

    @property
    def white_grid(self):
        return self.grid[...,1]

    @property
    def black_vision_grid(self):
        black_vision_grid=np.zeros(self.shape,dtype='bool')
        for piece in self.black_pieces:
            black_vision_grid+=piece.vision_grid
        return black_vision_grid

    @property
    def white_vision_grid(self):
        white_vision_grid=np.zeros(self.shape,dtype='bool')
        for piece in self.white_pieces:
            white_vision_grid+=piece.vision_grid
        return white_vision_grid

    @property
    def full_vision_grid(self):
        black_vision_grid = self.black_vision_grid[...,np.newaxis]
        white_vision_grid = self.white_vision_grid[...,np.newaxis]
        return np.concatenate((black_vision_grid,white_vision_grid),axis=2)

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
