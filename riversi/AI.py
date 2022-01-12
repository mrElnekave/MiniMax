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
            flippable = flipTiles(board,x, y, checking=True)
            if flippable:
                boardTemp = cp(board)
                flipTiles(boardTemp, x, y)

                points = AlphaBeta(boardTemp, EVALUATION_DEPTH, minimum_evaluation, maximum_evaluation, True)

                if points > maxPoints:
                    maxPoints = points
                    mx = x
                    my = y
    return (mx, my)


# Alpha Beta pruning
def AlphaBeta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_game_over(board):
        return evalBoard(board.board, board.turnWhite)
    if maximizingPlayer:
        max_eval = minimum_evaluation
        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                flippable = flipTiles(board, x, y, checking=True)
                if flippable:
                    boardTemp = cp(board)
                    flipTiles(boardTemp, x, y)
                    max_eval = max(max_eval, AlphaBeta(boardTemp, depth - 1, alpha, beta, False))
                    alpha = max(alpha, max_eval)
                    if beta <= alpha:
                        break  # beta cut-off
        return max_eval
    else:  # minimizingPlayer
        min_eval = maximum_evaluation
        for y in range(BOARDSIZE):
            for x in range(BOARDSIZE):
                flippable = flipTiles(board, x, y, checking=True)
                if flippable:
                    boardTemp = cp(board)
                    flipTiles(boardTemp, x, y)

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


def cellOnBoard(self, x, y):
    return 0 <= x < self.size and 0 <= y < self.size

def flipTiles(self, x, y, checking=False):
    if self.board[x][y].vacant:
        orig_Xval = self.turnWhite

        tiles_to_flip = []
        directions = [[1, 0], [1, -1], [0, 1], [1, 1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for xdir, ydir in directions:
            new_x = x + xdir
            new_y = y + ydir
            dir_flip = []
            other_color_at_end = False
            flipping = True
            while flipping:
                # see if new cord is on the board and is a enemy peice or your peice
                if cellOnBoard(self, new_x, new_y) and not self.board[new_x][new_y].vacant:
                    if self.board[new_x][new_y].isWhite != orig_Xval:
                        dir_flip.append((new_x, new_y))
                        new_x += xdir
                        new_y += ydir
                    else:
                        other_color_at_end = True
                        flipping = False
                else:
                    flipping = False
            if len(dir_flip) > 0 and other_color_at_end:
                for cell in dir_flip:
                    tiles_to_flip.append(cell)

        if len(tiles_to_flip) == 0:
            if not checking:
                self.turnWhite = not self.turnWhite
            return False
        if not checking:
            if self.turnWhite:
                self.board[x][y].isWhite = True
            self.board[x][y].vacant = False
            for x, y in tiles_to_flip:
                self.board[x][y].isWhite = not self.board[x][y].isWhite
        return True
    if not checking:
        self.turnWhite = not self.turnWhite

def is_game_over(self):

    for i in range(self.size):
        for j in range(self.size):
            if self.board[i][j].vacant:
                return False
    return True


