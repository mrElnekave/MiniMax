import pygame
import sys
import os
from riversi.constants import *
from riversi.objects import *
from riversi.classes import Board
import riversi.AI as AI
pygame.init()

# Player Input with validation on the board
def getPlayerMove(board, playerTile):
    pass


# if no valid move(s) possible then True
def isTerminalNode(board, player):  # game end
    pass


# Allows the player to pick the tile he wants
def chooseTile():
    pass


def gameover():
    player_score = AI.evalBoard(board, 'O')
    AI_score = AI.evalBoard(board, 'X')
    # sleep for 10 seconds
    sys.exit()


board = Board(BOARDSIZE)
while True:
    space_hit = False
    x = 0
    y = 0
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                board.toggle_available_spots()
            if event.key == pygame.K_SPACE:
                space_hit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # mouse 1
                board.makeMove(mouse_pos[0], mouse_pos[1])

    board.draw()

    if not board.turnWhite:
        x, y = AI.bestMove(board)
        if space_hit:
            board.flipTiles(x, y)
            board.turnWhite = not board.turnWhite
            space_hit = False

    pygame.display.update()
    mainClock.tick(10)
