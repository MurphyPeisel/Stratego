import arcade

import draw_piece
from Piece import Piece
from constants import *
import gameboard
import random

def generateBot():
    print("generate")
    gameboard.Gameboard.changeAI(1)

class bot():

    selected = None

    def select_piece(self, bot_pieces):
        bot.selected = None
        movable_pieces = []
        for piece in bot_pieces:
            if piece.getType() != "Lke" and piece.getType() != "Flg" and piece.getType() != "Bom":
                movable_pieces.append(piece)
        selected_num = random.randint(0, len(movable_pieces) - 1)
        print("movable pieces", movable_pieces)
        x = 0
        print("selected_num", selected_num)
        while bot.selected == None:
            for piece in movable_pieces:
                print("x", x)
                if x == selected_num and piece.getType() != "Lke" and piece.getType() != "Flg" and piece.getType() != "Bom":
                    bot.selected = piece
                x = x + 1
            if bot.selected != None:
                print("testing", bot.selected.getType())
                if bot.are_moves_available(self, bot.selected, bot_pieces) == False:
                    bot.selected = None
        print(bot.selected.getType())
        bot.make_move(self, bot_pieces, gameboard.p1_pieces)
    def are_moves_available(self, selected_piece, bot_pieces):
        x = selected_piece.getPosition()[0]
        y = selected_piece.getPosition()[1]
        leftMovement = True
        rightMovement = True
        upMovement = True
        downMovement = True
        for piece in bot_pieces:
            if piece.getPosition()[0] == x + 1 and piece.getPosition()[1] == y or x + 1 > 9:
                rightMovement = False
            if piece.getPosition()[0] == x - 1 and piece.getPosition()[1] == y or x - 1 < 0:
                leftMovement = False
            if piece.getPosition()[0] == x and piece.getPosition()[1] == y + 1 or y + 1 > 9:
                upMovement = False
            if piece.getPosition()[0] == x and piece.getPosition()[1] == y - 1 or y - 1 < 0:
                downMovement = False
        if leftMovement == False and rightMovement == False and upMovement == False and downMovement == False:
            return False
        else:
            return True
    def make_move(self, bot_pieces, user_pieces):
        lakelessUserPieces = []
        for i in user_pieces:
            if i.getType() != "Lke":
                lakelessUserPieces.append(i)

        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        leftMovement = True
        rightMovement = True
        upMovement = True
        downMovement = True
        for piece in bot_pieces:
            if piece.getPosition()[0] == x + 1 and piece.getPosition()[1] == y or x + 1 > 9:
                rightMovement = False
            if piece.getPosition()[0] == x - 1 and piece.getPosition()[1] == y or x - 1 < 0:
                leftMovement = False
            if piece.getPosition()[0] == x and piece.getPosition()[1] == y + 1 or y + 1 > 9:
                upMovement = False
            if piece.getPosition()[0] == x and piece.getPosition()[1] == y - 1 or y - 1 < 0:
                downMovement = False
        movement = [leftMovement, rightMovement, upMovement, downMovement]

        possibleCaptureRight = False
        possibleCaptureLeft = False
        possibleCaptureUp = False
        possibleCaptureDown = False

        k = 0
        while possibleCaptureLeft == False and possibleCaptureUp == False and possibleCaptureDown == False and possibleCaptureRight == False and k < len(lakelessUserPieces) - 1:
            j = lakelessUserPieces[k]
            if j.getPosition()[0] == x + 1 and j.getPosition()[1] == y:
                print("possible capture right")
                possibleCaptureRight = True
            if j.getPosition()[0] == x - 1 and j.getPosition()[1] == y:
                print("possible capture left")
                possibleCaptureLeft = True
            if j.getPosition()[0] == x and j.getPosition()[1] == y + 1:
                print("possible capture up")
                possibleCaptureUp = True
            if j.getPosition()[0] == x and j.getPosition()[1] == y - 1:
                print("possible capture down")
                possibleCaptureDown = True
            if possibleCaptureLeft == False and possibleCaptureUp == False and possibleCaptureDown == False and possibleCaptureRight == False:
                k = k + 1


        if possibleCaptureRight:
            draw_piece.combat(bot.selected, j, [BOARD_RIGHT + 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * j.getPosition()[1]], gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
        elif possibleCaptureLeft:
            draw_piece.combat(bot.selected, j, [BOARD_LEFT - 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * j.getPosition()[1]], gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
        elif possibleCaptureDown:
            draw_piece.combat(bot.selected, j,
                              [BOARD_LEFT + 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_BOTTOM - 25 + BOARD_MARGIN * j.getPosition()[1]],
                              gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
        elif possibleCaptureUp:
            draw_piece.combat(bot.selected, j,
                              [BOARD_RIGHT - 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_TOP + 25 + BOARD_MARGIN * j.getPosition()[1]],
                              gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)


        else:
            bot_move = random.randint(0, len(movement) - 1)
            print(bot_move)
            while movement[bot_move] == False:
                bot_move = random.randint(0, len(movement) - 1)
                print(bot_move)
            if bot_move == 0:
                move = "left"
            if bot_move == 1:
                move = "right"
            if bot_move == 2:
                move = "up"
            if bot_move == 3:
                move = "down"
            print("moving to the", move)
            if move == "left":
                bot.selected.setPosition(x - 1, y)
                print("left")
            if move == "right":
                bot.selected.setPosition(x + 1, y)
                print("right")
            if move == "up":
                bot.selected.setPosition(x, y + 1)
                print("up")
            if move == "down":
                bot.selected.setPosition(x, y - 1)
                print("down")
