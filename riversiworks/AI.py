from riversi.classes import *
import copy


# Calculates Best Move
def bestMove(board: Board):
    maxPoints = minimum_evaluation
    mx = -1
    my = -1
    board = cp(board)
    for y in range(board.size):
        for x in range(board.size):
            flippable = board.flipTiles(x, y, checking=True)
            if flippable:
                boardTemp = cp(board)
                boardTemp.flipTiles(x, y)

                points = AlphaBeta(boardTemp, EVALUATION_DEPTH, minimum_evaluation, maximum_evaluation, True)

                if points > maxPoints:
                    maxPoints = points
                    mx = x
                    my = y
    return (mx, my)


# Alpha Beta pruning
def AlphaBeta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_game_over():
        return evalBoard(board.board, board.turnWhite)
    if maximizingPlayer:
        max_eval = minimum_evaluation
        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                flippable = board.flipTiles(x, y, checking=True)
                if flippable:
                    boardTemp = cp(board)
                    boardTemp.flipTiles(x, y)
                    max_eval = max(max_eval, AlphaBeta(boardTemp, depth - 1, alpha, beta, False))
                    alpha = max(alpha, max_eval)
                    if beta <= alpha:
                        break  # beta cut-off
        return max_eval
    else:  # minimizingPlayer
        min_eval = maximum_evaluation
        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                flippable = board.flipTiles(x, y, checking=True)
                if flippable:
                    boardTemp = cp(board)
                    boardTemp.flipTiles(x, y)

                    min_eval = min(min_eval, AlphaBeta(boardTemp, depth - 1, alpha, beta, True))
                    beta = min(beta, min_eval)
                    if beta <= alpha:
                        break  # alpha cut-off
        return min_eval


def evalBoard(board, player):
    score = 0
    for y in range(BOARDSIZE):
        for x in range(BOARDSIZE):
            if board[y][x].isWhite == player:
                if (x == 0 or x == BOARDSIZE - 1) and (y == 0 or y == BOARDSIZE - 1):
                    score += 3  # corner
                elif (x == 0 or x == BOARDSIZE - 1) or (y == 0 or y == BOARDSIZE - 1):
                    score += 2  # side
                else:
                    score += 1
    return score


def cp(board):
    nboard = simpleBoard(board.size)
    nboard.board = copy.deepcopy(board.board)
    nboard.turnWhite = board.turnWhite
    return nboard
