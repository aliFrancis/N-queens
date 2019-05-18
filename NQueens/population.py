from NQueens.board import Board

class Population():

    def __init__(self, pop_limits=[100,100], boards = None, board_shape = [8,8]):
        self.pop_limits = pop_limits
        if isinstance(board_shape,int):
            self.board_shape = [board_shape,board_shape]
        elif isinstance(board_shape,list):
            if len(board_shape)==2:
                self.board_shape = board_shape
            else:
                raise "ValueError: board_shape must be an int or list of length 2"
        if boards is not None:
            assert all([board.shape==board_shape for board in boards]), 'Not all boards are correct side_length'
            assert len(boards)>=pop_limits[0] and len(boards)<=pop_limits[1], 'Number of boards not within pop_limits'
            self.boards = boards
        else: #Initialise a population of boards
            self.boards = [Board(board_shape) for i in range(pop_limits[0])]


    def __getitem__(self,index):
        return self.boards[index]

    def __len__(self):
        return len(self.boards)

    def add_board(self,board):
        assert len(self)<pop_limits[1], 'Cannot add board, at population cap!'
        assert board.shape == self.board_shape
        self.boards.append(board)
