class Population():

    def __init__(self, pop_limits=[100,100], boards = None, side_length = 10):
        self.pop_limits = pop_limits
        self.side_length = side_length
        if boards is not None:
            assert all([board.shape[0]==side_length for board in boards]), 'Not all boards are correct side_length'
            assert len(boards)>=pop_limits[0] and len(boards)<=pop_limits[1], 'Number of boards not within pop_limits'

            self.boards = boards
        else: #Initialise a population of boards
            self.boards = [board.Board(side_length) for i in range(pop_limits[0])]


    def __getitem__(self,index):
        return self.boards[index]
