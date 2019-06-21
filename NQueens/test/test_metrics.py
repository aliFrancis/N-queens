from NQueens import metrics
from NQueens.piece import Piece
from NQueens.board import Board

import numpy as np


def test_is_peaceable():
    board = Board(10)
    w1 = Piece('white',[5,2],board)
    b1 = Piece('black',[9,3],board)
    assert metrics.is_peaceable(board)
    b2 = Piece('black',[7,4],board)
    assert not metrics.is_peaceable(board)

def test_piece_count():
    board = Board(8)
    w1 = Piece('white',[5,2],board)
    assert metrics.piece_count(board) == 1
    b1 = Piece('black',[7,3],board)
    assert metrics.piece_count(board) == 2
    b2 = Piece('black',[7,4],board)
    assert metrics.piece_count(board) == 3
    board.remove_piece(b1.ID)
    assert metrics.piece_count(board) == 2


def test_vision_grid_sparsity():
    board1 = Board(3)
    w1 = Piece('white',[1,1],board1)
    assert metrics.vision_grid_sparsity(board1)==9/18
    b1 = Piece('black',[0,1],board1)
    assert metrics.vision_grid_sparsity(board1)==2/18

    board2 = Board(5)
    w2 = Piece('white',[2,2],board2)
    assert metrics.vision_grid_sparsity(board2)==33/50

    board3 = Board(8)
    w3 = Piece('white',[0,0],board3)
    assert metrics.vision_grid_sparsity(board3)==106/128

    board4 = Board(3)
    w4 = Piece('white',[0,0],board4)
    b2 = Piece('black',[2,2],board4)
    assert metrics.vision_grid_sparsity(board4)==4/18

    board5 = Board([13,18])
    w5 = Piece('white',[10,10],board5)
    assert metrics.vision_grid_sparsity(board5)==(13*18*2-51)/(13*18*2)
