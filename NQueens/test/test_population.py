from NQueens.population import Population
from NQueens.board import Board
from NQueens.piece import Piece


def test_Population():
    pop1 = Population()
    assert len(pop1)==100
    assert isinstance(pop1[4],Board)

    pop2 = Population(board_shape=4)
    assert pop2[4].shape == [4,4]

    pop3 = Population(pop_limits=[10,80],board_shape=4)
    assert len(pop3) == 10
    
