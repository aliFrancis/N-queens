def is_valid(board):
    return int(board.is_valid())

def piece_count(board):
    return len(board.pieces['black'])+len(board.pieces['white'])

def vision_grid_sparsity(board):
    vis_grid = board.get_full_vision_grid()
    return (vis_grid.size - np.sum(vis_grid.astype('int')))/vis_grid.size
