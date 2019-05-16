class Population():

    def __init__(self, pop_limits=[100,100], boards = None, board_shape = [10,10]):
        self.pop_limits = pop_limits
        self.board_shape = board_shape
        if boards is not None:
            assert all([board.shape==board_shape for board in boards]), 'Not all boards are correct side_length'
            assert len(boards)>=pop_limits[0] and len(boards)<=pop_limits[1], 'Number of boards not within pop_limits'

            self.boards = boards
        else: #Initialise a population of boards
            self.boards = [board.Board(board_shape) for i in range(pop_limits[0])]


    def __getitem__(self,index):
        return self.boards[index]
