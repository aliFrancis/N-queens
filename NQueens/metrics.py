import numpy as np

def is_valid(board):
    return int(board.is_valid())

def piece_count(board):
    return len(board.pieces)

def vision_grid_sparsity(board):
    vis_grid = board.full_vision_grid
    N_squares = vis_grid.size
    return (N_squares-np.sum(vis_grid.astype('int')))/N_squares
