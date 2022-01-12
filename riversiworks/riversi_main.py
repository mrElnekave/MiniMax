import pygame
import sys
import os
import copy
from riversi.constants import *
from riversi.objects import *
from riversi.classes import Board
import riversi.AI as AI
pygame.init()


def gameover():
    player_score = AI.evalBoard(board, 'O')
    AI_score = AI.evalBoard(board, 'X')
    # sleep for 10 seconds
    sys.exit()


board = Board(BOARDSIZE)
while True:
    wait = 0
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                board.toggle_available_spots()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # mouse 1
                board.makeMove(mouse_pos[0], mouse_pos[1])
                wait = 500

    board.draw()

    wait -= 1
    if not board.turnWhite and wait < 0:
        x, y = AI.bestMove(board)
        board.flipTiles(x, y)
        board.turnWhite = not board.turnWhite

    # if board.playerTurn:  # Player
    #     move = getPlayerMove(board, playerTile)
    #     makeMove(board, playerTile, move[0], move[1])
    #     drawBoard(board)
    #     board.playerTurn = False
    # else:  # AI
    #     (x, y) = bestMove(board, currentTile)
    #     board = makeMove(board, enemyTile, x, y)
    #     drawBoard(board)
    #     print('AI played (X Y): ' + str(x + 1) + '' + str(y + 1))
    #     board.playerTurn = True
    #
    # if isTerminalNode(board, currentTile):
    #     gameover()

    pygame.display.update()
    mainClock.tick(10)
