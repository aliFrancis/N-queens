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
        upperleft,upperright,lowerleft,lowerright = self._diagonal_intersections()

        diag_start = upperleft[1]+grid.shape[0]*upperleft[0]
        diag_end = lowerright[1]+grid.shape[0]*lowerright[0]

        anti_diag_start = lowerleft[1]+grid.shape[0]*lowerleft[0]
        anti_diag_end = upperright[1]+grid.shape[0]*upperright[0]

        grid.ravel()[diag_start:diag_end+1:self.board.shape[0]+1] = True
        grid.ravel()[anti_diag_start:anti_diag_end+1:self.board.shape[0]-1] = True

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
        lowerright = [min(self.board.shape[0]-1,self.board.shape[1]+x_0-y_0), min(self.board.shape[1]-1,self.board.shape[0]+y_0-x_0)]
        return  upperleft,upperright,lowerleft,lowerright


    def is_valid(self):
        other_colour = [col for col in ['black','white'] if col!=self.colour][0]
        for piece in self.board.pieces[other_colour]:
            vis_grid = piece.get_vision_grid()
            if vis_grid[self.x,self.y]:
                return False
        return True


    def move_to(self,position):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.board.move_piece(self.ID,position)


if __name__=='__main__':
    import board
    board = board.Board(20)
    piece_w1 = Piece('white',[16,10],board)
    piece_b1 = Piece('black',[15,12],board)
    piece_b2 = Piece('black',[ 2, 2],board)
    print(board)
    print(piece_w1.is_valid())
    print(piece_b1.is_valid())
    print(piece_b2.is_valid())
    print(board.is_valid())
