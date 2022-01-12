from riversi.constants import *
import os
from riversi.objects import *


class Cell:
    def __init__(self):
        self.isWhite = False
        self.vacant = True


class simpleBoard:
    def __init__(self, size):
        self.board = []
        self.size = size
        # self.playerTurn = True
        self.turnWhite = True


class Board:
    def __init__(self, size):
        self.board = []
        self.resetBoard()
        self.size = size
        self.playerTurn = True
        self.available_spots = []
        self.highlight_available_spots = True
        self.tile_size = SCREENSIZE[0] // size
        self.turnWhite = True

        # image stuff
        current_path = os.path.dirname(__file__)  # Where your .py file is located
        self.image_path = os.path.join(current_path, 'imgs')  # The image folder path
        tileImage = pygame.image.load(os.path.join(self.image_path, "dark_green_tile" + ".png"))
        self.tileImage = pygame.transform.scale(tileImage, (self.tile_size, self.tile_size))
        white = pygame.image.load(os.path.join(self.image_path, "white_circle" + ".png"))
        black = pygame.image.load(os.path.join(self.image_path, "black_circle" + ".png"))
        self.white = pygame.transform.scale(white, (self.tile_size, self.tile_size))
        self.black = pygame.transform.scale(black, (self.tile_size, self.tile_size))

        pass

    def draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                cell = self.board[i][j]
                # if self.highlight_available_spots:
                #     image = self.tileImage.set_alpha(60)
                #     screen.blit(image, (i * self.tile_size, j * self.tile_size))
                screen.blit(self.tileImage, (i * self.tile_size, j * self.tile_size))
                if not cell.vacant:
                    if cell.isWhite:
                        Image = self.white
                    else:
                        Image = self.black
                    screen.blit(Image, (i * self.tile_size, j * self.tile_size))

    def resetBoard(self):
        self.board = [[Cell() for j in range(BOARDSIZE)] for i in range(BOARDSIZE)]

        # Pieces starting on the board
        self.board[3][3].isWhite = True
        self.board[3][4].isWhite = False
        self.board[4][3].isWhite = False
        self.board[4][4].isWhite = True

        self.board[3][3].vacant = False
        self.board[3][4].vacant = False
        self.board[4][3].vacant = False
        self.board[4][4].vacant = False

    def makeMove(self, x, y):
        x = x//self.tile_size
        y = y//self.tile_size
        self.flipTiles(x, y)
        self.turnWhite = not self.turnWhite
        pass

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
                    if self.cellOnBoard(new_x, new_y) and not self.board[new_x][new_y].vacant:
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
                self.turnWhite = not self.turnWhite
                return False
            if not checking:
                if self.turnWhite:
                    self.board[x][y].isWhite = True
                self.board[x][y].vacant = False
                for x, y in tiles_to_flip:
                    self.board[x][y].isWhite = not self.board[x][y].isWhite
            return True
        self.turnWhite = not self.turnWhite

    def toggle_available_spots(self):
        if len(self.available_spots) == 0:
            for i in range(self.size):
                for j in range(self.size):
                    if self.flipTiles(i, j, checking=True):
                        self.available_spots.append((i, j))
        self.highlight_available_spots = not self.highlight_available_spots
        pass

    def is_game_over(self):

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].vacant:
                    return False
        return True
