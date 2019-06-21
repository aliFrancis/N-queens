from NQueens.piece import Piece
from NQueens.board import Board
import matplotlib.pyplot as plt
import pytest

def test_Piece_initialization():
    board = Board(20)
    w1 = Piece('white',[5,2],board)

    assert w1.x == 5
    assert w1.y == 2
    assert w1.position == [5,2]

    with pytest.raises(ValueError):
        Piece('black',[-1,-1],board)
    with pytest.raises(ValueError):
        Piece('not_white_or_black',[1,1],board)
    with pytest.raises(ValueError):
        Piece('black',[5,2],board)

def test_Piece_movement():
    board = Board(20)
    w1 = Piece('white',[5,2],board)
    w1.move_to([4,3])
    assert w1.x == 4
    assert w1.y == 3
    assert w1.position == [4,3]

def test_Piece_diagonal_intersections():
    board = Board([40,60])
    w1 = Piece('white',[0,0],board)
    UL,UR,LL,LR = w1._diagonal_intersections()
    assert UL==[0,0]
    assert UR==[0,0]
    assert LL==[0,0]
    assert LR==[39,39]
    w2 = Piece('white',[39,0],board)
    UL,UR,LL,LR = w2._diagonal_intersections()
    assert UL==[39,0]
    assert UR==[39,0]
    assert LL==[0,39]
    assert LR==[39,0]

    w3 = Piece('white',[0,59],board)
    UL,UR,LL,LR = w3._diagonal_intersections()
    assert UL==[0,59]
    assert UR==[39,20]
    assert LL==[0,59]
    assert LR==[0,59]

    w4 = Piece('white',[11,25],board)
    UL,UR,LL,LR = w4._diagonal_intersections()
    assert UL==[0,14]
    assert UR==[36,0]
    assert LL==[0,36]
    assert LR==[39,53]
