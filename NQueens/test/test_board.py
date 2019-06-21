from NQueens.board import Board
from NQueens.piece import Piece
import numpy as np


def test_board():

    board0 = Board([8,15])
    assert board0.shape==[8,15]
    assert board0.grid.shape==(8,15,2)
    assert np.sum(board0.grid)==0

    board1= Board(10)
    assert board1.shape==[10,10]
    assert board1.black_pieces==[]
    assert board1.white_pieces==[]
    assert board1.pieces==[]
    assert board1.is_peaceable()
    assert not board1.is_filled_at([1,1])
    assert np.sum(board1.black_vision_grid) == 0
    assert np.sum(board1.white_vision_grid) == 0
    assert np.sum(board1.full_vision_grid) == 0

    w0 = Piece('white',[2,4],board1)
    assert len(board1.black_pieces)==0
    assert len(board1.white_pieces)==1
    assert len(board1.pieces)==1
    assert board1.is_peaceable()
    assert not board1.is_filled_at([1,1])
    assert board1.is_filled_at([2,4])
    assert np.sum(board1.black_vision_grid) == 0
    assert np.sum(board1.white_vision_grid) != 0
    assert np.sum(board1.full_vision_grid) != 0
    assert board1.ID_list == [0]

    w1 = Piece('white',[4,7],board1)
    assert len(board1.black_pieces)==0
    assert len(board1.white_pieces)==2
    assert len(board1.pieces)==2
    assert board1.is_peaceable()
    assert board1.ID_list == [0,1]

    b1 = Piece('black',[7,7],board1)
    assert len(board1.black_pieces)==1
    assert len(board1.white_pieces)==2
    assert len(board1.pieces)==3
    assert not board1.is_peaceable()
    assert np.sum(board1.black_vision_grid) != 0
    assert np.sum(board1.grid[...,0]) == 1 #black pieces on grid
    assert np.sum(board1.grid[...,1]) == 2 #white pieces on grid
    assert np.sum(board1.black_grid) == 1 #black pieces on grid
    assert np.sum(board1.white_grid) == 2 #white pieces on grid
    assert board1.ID_list == [0,1,2]

    board1.remove_piece(w1.ID)
    assert board1.ID_list == [0,2]
    board1.reassign_IDs()
    assert board1.ID_list == [0,1]
    assert board1.is_peaceable()
    assert len(board1.pieces)==2
    assert len(board1.white_pieces)==1
    assert np.sum(board1.white_grid) == 1 #white pieces on grid

    board1.move_piece(w0.ID,[5,7])
    assert not board1.is_peaceable()
