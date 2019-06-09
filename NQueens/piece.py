import numpy as np


class Piece():

    def __init__(self, colour, position, board):
        self.x = position[0]
        self.y = position[1]
        assert colour in ['black','white'], 'colour is not black or white'
        self.colour = colour
        self.board = board
        self.ID = self.board.add_piece(self)

    @property
    def position(self):
        return [self.x,self.y]

    @property
    def vision_grid(self):
        grid = np.zeros(self.board.shape,dtype='bool')
        x_0, y_0 = self.position
        grid[x_0,:] = True
        grid[:,y_0] = True
        upperleft,upperright,lowerleft,lowerright = self._diagonal_intersections()

        diag_start = upperleft[1]+grid.shape[1]*upperleft[0]
        diag_end = lowerright[1]+grid.shape[1]*lowerright[0]

        anti_diag_start = lowerleft[1]+grid.shape[1]*lowerleft[0]
        anti_diag_end = upperright[1]+grid.shape[1]*upperright[0]

        grid.ravel()[diag_start:diag_end+1:self.board.shape[1]+1] = True
        grid.ravel()[anti_diag_start:anti_diag_end+1:self.board.shape[1]-1] = True

        return grid

    def _diagonal_intersections(self):
        """
        Returns [x,y] grid coordinates of points of intersection between diagonal lines emanating
        from self.position and the edges of self.board.
        """
        x_0, y_0 = self.position
        upperleft  = [max(0,x_0-y_0),max(0,y_0-x_0)]
        upperright = [min(x_0+y_0,self.board.shape[0]-1), max(0,x_0 + y_0 + 1 - self.board.shape[0])]
        lowerleft  = [max(0,x_0+y_0+1-self.board.shape[1]), min(x_0 + y_0,self.board.shape[1]-1)]
        lowerright = [min(self.board.shape[0]-1,self.board.shape[1]+x_0-y_0-1), min(self.board.shape[1]-1,self.board.shape[0]+y_0-x_0-1)]
        return  upperleft,upperright,lowerleft,lowerright

    def is_valid(self):
        if self.colour=='black':
            other_pieces = self.board.white_pieces
        elif self.colour=='white':
            other_pieces = self.board.black_pieces
        for piece in other_pieces:
            vis_grid = piece.vision_grid
            if vis_grid[self.x,self.y]:
                return False
        return True

    def move_to(self,new_position):
        self.board.move_piece(self.ID,new_position)
