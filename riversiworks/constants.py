BOARDSIZE = 8
if BOARDSIZE < 5:
    BOARDSIZE = 5
peice_val = 1
edge_val = 2
corner_val = 3

EVALUATION_DEPTH = 2

SCREENSIZE = (500, 500)

minimum_evaluation = -1  # having less than 1 tile
middle_peices = ((BOARDSIZE - 2) ** 2) * peice_val
edge_peices = ((BOARDSIZE - 2) * 4) * edge_val
corner_peices = 4 * corner_val
maximum_evaluation = middle_peices + edge_peices + corner_peices + 1  # having 1 more tile than the maximum score
