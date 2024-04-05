import arcade

import draw_piece
from constants import *
import gameboard
import random

allAI = 0

def generateBot(ai):
    print("generate")
    allAI = ai
    gameboard.Gameboard.changeAI(ai)

class bot():

    selected = None
    ai = allAI

    def generateBot(ai):
        print("generate")
        bot.ai = ai
        gameboard.Gameboard.changeAI(ai)

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
        rightMovementList = []
        leftMovementList = []
        upMovementList = []
        downMovementList = []
        if bot.selected.getType() != "Sct":
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
            if bot.ai == 2:
                movement.append(leftMovement)
                movement.append(rightMovement)
                movement.append(downMovement)
            elif bot.ai == 3:
                movement.append(leftMovement)
                movement.append(rightMovement)
                movement.append(downMovement)
                movement.append(downMovement)
        elif bot.selected.getType() == "Sct":
            canAttackRight = []
            canAttackLeft = []
            canAttackUp = []
            canAttackDown = []
            i = 0
            while i < 9:
                i = i + 1
                total_pieces = bot_pieces + user_pieces
                for piece in total_pieces:
                    if piece.getPosition()[0] == x + i and piece.getPosition()[1] == y or x + i > 9:
                        i = 10
                if i <= 9:
                    rightMovementList.append("can move")
            print("right move list", rightMovementList)
            i = 0
            while i < 9:
                i = i + 1
                for piece in total_pieces:
                    if piece.getPosition()[0] == x - i and piece.getPosition()[1] == y or x - i < 0:
                        i = 10
                if i <= 9:
                    leftMovementList.append("can move")
                print(i)
            print("left move list", leftMovementList)
            i = 0
            while i < 9:
                i = i + 1
                for piece in total_pieces:
                    if piece.getPosition()[0] == x and piece.getPosition()[1] == y + i or y + i > 9:
                        i = 10
                if i <= 9:
                    upMovementList.append("can move")
            print("up move list", upMovementList)
            i = 0
            while i < 9:
                i = i + 1
                for piece in total_pieces:
                    if piece.getPosition()[0] == x and piece.getPosition()[1] == y - i or y - i < 0:
                        i = 10
                if i <= 9:
                    downMovementList.append("can move")
            print("down move list", downMovementList)


        possibleCaptureRight = False
        possibleCaptureLeft = False
        possibleCaptureUp = False
        possibleCaptureDown = False

        k = 0
        while possibleCaptureLeft == False and possibleCaptureUp == False and possibleCaptureDown == False and possibleCaptureRight == False and k < len(lakelessUserPieces) - 1:
            j = lakelessUserPieces[k]
            if j.getPosition()[0] == x + 1 and j.getPosition()[1] == y and bot.selected.getType() != "Sct":
                print("possible capture right")
                possibleCaptureRight = True
            if bot.selected.getType() == "Sct":
                i = 0
                while i < 9:
                    i = i + 1
                    if j.getPlayer() == 2 and j.getPosition()[0] == x + i and j.getPosition()[1] == y:
                        i = 10
                    elif j.getPlayer() == 1 and j.getPosition()[0] == x + i and j.getPosition()[1] == y:
                        print("found opponent right", piece.getType())
                        possibleCaptureRight = True
                        canAttackRight = [x + i, y]

            if j.getPosition()[0] == x - 1 and j.getPosition()[1] == y and bot.selected.getType() != "Sct":
                print("possible capture left")
                possibleCaptureLeft = True
            if bot.selected.getType() == "Sct":
                i = 0
                while i < 9:
                    i = i + 1
                    if j.getPlayer() == 2 and j.getPosition()[0] == x - i and j.getPosition()[1] == y:
                        i = 10
                    elif j.getPlayer() == 1 and j.getPosition()[0] == x - i and j.getPosition()[1] == y:
                        print("found opponent Left", piece.getType())
                        possibleCaptureLeft = True
                        canAttackLeft = [x - i, y]

            if j.getPosition()[0] == x and j.getPosition()[1] == y + 1 and bot.selected.getType() != "Sct":
                print("possible capture up")
                possibleCaptureUp = True
            if bot.selected.getType() == "Sct":
                i = 0
                while i < 9:
                    i = i + 1
                    if j.getPlayer() == 2 and j.getPosition()[0] == x and j.getPosition()[1] == y - i:
                        i = 10
                    elif j.getPlayer() == 1 and j.getPosition()[0] == x and j.getPosition()[1] == y - i:
                        print("found opponent up", piece.getType())
                        possibleCaptureUp = True
                        canAttackUp = [x, y - i]

            if j.getPosition()[0] == x and j.getPosition()[1] == y - 1 and bot.selected.getType() != "Sct":
                print("possible capture down")
                possibleCaptureDown = True
            if bot.selected.getType() == "Sct":
                i = 0
                while i < 9:
                    i = i + 1
                    if j.getPlayer() == 2 and j.getPosition()[0] == x and j.getPosition()[1] == y - i:
                        i = 10
                    elif j.getPlayer() == 1 and j.getPosition()[0] == x and j.getPosition()[1] == y - i:
                        print("found opponent up", piece.getType())
                        possibleCaptureDown = True
                        canAttackDown = [x, y + i]
            if possibleCaptureLeft == False and possibleCaptureUp == False and possibleCaptureDown == False and possibleCaptureRight == False:
                k = k + 1


        if possibleCaptureRight:
            draw_piece.combat(bot.selected, j, [BOARD_RIGHT - 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * j.getPosition()[1]], gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
        elif possibleCaptureLeft:
            draw_piece.combat(bot.selected, j, [BOARD_LEFT + 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * j.getPosition()[1]], gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
        elif possibleCaptureDown:
            draw_piece.combat(bot.selected, j,
                              [BOARD_LEFT + 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * j.getPosition()[1]],
                              gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
        elif possibleCaptureUp:
            draw_piece.combat(bot.selected, j,
                              [BOARD_RIGHT - 25 + BOARD_MARGIN * j.getPosition()[0], BOARD_TOP - 25 + BOARD_MARGIN * j.getPosition()[1]],
                              gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)

        else:
            if bot.selected.getType() != "Sct":
                bot_move = random.randint(0, len(movement) - 1)
                print(bot_move)
                while movement[bot_move] == False:
                    bot_move = random.randint(0, len(movement) - 1)
                    print(bot_move)
                move = "error"
                print("ai", bot.ai)
            if bot.ai == 1 and bot.selected.getType() != "Sct":
                if bot_move == 0:
                    move = "left"
                    bot.selected.setPosition(x - 1, y)
                if bot_move == 1:
                    move = "right"
                    bot.selected.setPosition(x + 1, y)
                if bot_move == 2:
                    move = "up"
                    bot.selected.setPosition(x, y + 1)
                if bot_move >= 3:
                    move = "down"
                    bot.selected.setPosition(x, y - 1)

            if bot.ai == 1 and bot.selected.getType() == "Sct":
                SctMovement = []
                if len(leftMovementList) != 0:
                    SctMovement.append("left")
                if len(rightMovementList) != 0:
                    SctMovement.append("right")
                if len(upMovementList) != 0:
                    SctMovement.append("up")
                if len(downMovementList) != 0:
                    SctMovement.append("down")
                print(SctMovement)

                bot_move = random.randint(0, len(SctMovement) - 1)

                if SctMovement[bot_move] == "left":
                    direction = "left"
                    movement_magnitude = random.randint(0, len(leftMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x - movement_magnitude, y)
                if SctMovement[bot_move] == "right":
                    direction = "right"
                    movement_magnitude = random.randint(0, len(rightMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x + movement_magnitude, y)
                if SctMovement[bot_move] == "up":
                    direction = "up"
                    movement_magnitude = random.randint(0, len(upMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x, y + movement_magnitude)
                if SctMovement[bot_move] == "down":
                    direction = "down"
                    movement_magnitude = random.randint(0, len(downMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x, y - movement_magnitude)

            if bot.ai == 2 and bot.selected.getType() != "Sct":
                if bot_move == 0:
                    move = "left"
                    bot.selected.setPosition(x - 1, y)
                if bot_move == 1:
                    move = "right"
                    bot.selected.setPosition(x + 1, y)
                if bot_move == 2:
                    move = "up"
                    bot.selected.setPosition(x, y + 1)
                if bot_move == 3:
                    move = "down"
                    bot.selected.setPosition(x, y - 1)
                if bot_move == 4:
                    move = "left"
                    bot.selected.setPosition(x - 1, y)
                if bot_move == 5:
                    move = "right"
                    bot.selected.setPosition(x + 1, y)
                if bot_move >= 6:
                    move = "down"
                    bot.selected.setPosition(x, y - 1)

            if bot.ai == 2 and bot.selected.getType() == "Sct":
                SctMovement = []
                if len(leftMovementList) != 0:
                    SctMovement.append("left")
                if len(rightMovementList) != 0:
                    SctMovement.append("right")
                if len(upMovementList) != 0:
                    SctMovement.append("up")
                if len(downMovementList) != 0:
                    SctMovement.append("down")
                print(SctMovement)

                bot_move = random.randint(0, len(SctMovement) - 1)

                if SctMovement[bot_move] == "left":
                    direction = "left"
                    movement_magnitude = random.randint(0, len(leftMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x - movement_magnitude, y)
                if SctMovement[bot_move] == "right":
                    direction = "right"
                    movement_magnitude = random.randint(0, len(rightMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x + movement_magnitude, y)
                if SctMovement[bot_move] == "up":
                    direction = "up"
                    movement_magnitude = random.randint(0, len(upMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x, y + movement_magnitude)
                if SctMovement[bot_move] == "down":
                    direction = "down"
                    movement_magnitude = random.randint(0, len(downMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x, y - movement_magnitude)

            if bot.ai == 3 and bot.selected.getType() != "Sct":
                if bot_move == 0:
                    move = "left"
                    bot.selected.setPosition(x - 1, y)
                if bot_move == 1:
                    move = "right"
                    bot.selected.setPosition(x + 1, y)
                if bot_move == 2:
                    move = "up"
                    bot.selected.setPosition(x, y + 1)
                if bot_move == 3:
                    move = "down"
                    bot.selected.setPosition(x, y - 1)
                if bot_move == 4:
                    move = "left"
                    bot.selected.setPosition(x - 1, y)
                if bot_move == 5:
                    move = "right"
                    bot.selected.setPosition(x + 1, y)
                if bot_move == 6:
                    move = "down"
                    bot.selected.setPosition(x, y - 1)
                if bot_move == 7:
                    move = "down"
                    bot.selected.setPosition(x, y - 1)

            if bot.ai == 3 and bot.selected.getType() == "Sct":
                SctMovement = []
                if len(leftMovementList) != 0:
                    SctMovement.append("left")
                if len(rightMovementList) != 0:
                    SctMovement.append("right")
                if len(upMovementList) != 0:
                    SctMovement.append("up")
                if len(downMovementList) != 0:
                    SctMovement.append("down")
                print(SctMovement)

                bot_move = random.randint(0, len(SctMovement) - 1)

                if SctMovement[bot_move] == "left":
                    direction = "left"
                    movement_magnitude = random.randint(0, len(leftMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x - movement_magnitude, y)
                if SctMovement[bot_move] == "right":
                    direction = "right"
                    movement_magnitude = random.randint(0, len(rightMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x + movement_magnitude, y)
                if SctMovement[bot_move] == "up":
                    direction = "up"
                    movement_magnitude = random.randint(0, len(upMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x, y + movement_magnitude)
                if SctMovement[bot_move] == "down":
                    direction = "down"
                    movement_magnitude = random.randint(0, len(downMovementList))
                    print(direction, movement_magnitude)
                    bot.selected.setPosition(x, y - movement_magnitude)

                print("moving", move)

