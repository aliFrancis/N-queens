import numpy as np

class Piece():


    def __init__(self, colour, position, board):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        assert colour in ['black','white'], 'colour is not black or white'
        self.colour = colour
        self.board = board
        self.ID = self.board.add_piece(self)
        self.vision_grid = self.get_vision_grid()

    def get_vision_grid(self):
        grid = np.zeros(self.board.shape,dtype='bool')
        x_0, y_0 = self.position
        grid[x_0,:] = True
        grid[:,y_0] = True
        intersect_upperleft  = [max(0,x_0-y_0),max(0,y_0-x_0)]
        intersect_upperright = [min(x_0+y_0,self.board.shape[0]-1), max(0,x_0 + y_0 + 1 - self.board.shape[0])]
        intersect_lowerleft  = [max(0,x_0+y_0+1-self.board.shape[1]), min(x_0 + y_0,self.board.shape[1]-1)]
        intersect_lowerright = [min(self.board.shape[0]-1,self.board.shape[1]+x_0-y_0), min(self.board.shape[1]-1,self.board.shape[0]+y_0-x_0)]

        diag_start = intersect_upperleft[1]+grid.shape[0]*intersect_upperleft[0]
        diag_end = intersect_lowerright[1]+grid.shape[0]*intersect_lowerright[0]

        anti_diag_start = intersect_lowerleft[1]+grid.shape[0]*intersect_lowerleft[0]
        anti_diag_end = intersect_upperright[1]+grid.shape[0]*intersect_upperright[0]
        
        grid.ravel()[diag_start:diag_end+1:self.board.shape[0]+1] = True
        grid.ravel()[anti_diag_start:anti_diag_end+1:self.board.shape[0]-1] = True

        return grid

    def is_valid(self):
        condition = True
        for piece in self.pieces['black']:
            condition = self.is_valid_piece_against(piece,self.pieces['white'])
            if not condition:
                return False


    def move_to(self,position):
        self.board.move_piece(self.ID,position)


if __name__=='__main__':
    import board
    board = board.Board(30)
    piece = Piece('white',[16,24],board)
    print(piece.vision_grid.astype('int'))
