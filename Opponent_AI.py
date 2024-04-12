import arcade

import draw_piece
from constants import *
import gameboard
import random

# sets the default AI to 0 level difficultly
allAI = 0


def generateBot(ai):
    """
    sets the AI difficultly to what the user selected
    :param ai: integer representing the difficulty of the AI
    :return: none
    """
    print("generate")
    allAI = ai
    gameboard.Gameboard.changeAI(ai)


class bot():
    """
    bot class that controls the moves and pieces of the computers moves if the user selects to play against the computer
    """
    selected = None
    ai = allAI

    def generateBot(ai):
        """
        sets the AI difficultly to what the user selected
        :param ai: integer representing the difficulty of the AI
        :return: none
        """
        print("generate")
        bot.ai = ai
        gameboard.Gameboard.changeAI(ai)

    def select_piece(self, bot_pieces):
        """
        this function scans all the pieces on its side and randomly selects from those that are movable
        :param self / bot: the bot itself
        :param bot_pieces: a list of all the pieces on the bots side
        """
        bot.selected = None
        # this filters for pieces that inherently cannot be moved as a part of the rules
        movable_pieces = []
        for piece in bot_pieces:
            if piece.getType() != "Lke" and piece.getType() != "Flg" and piece.getType() != "Bom":
                movable_pieces.append(piece)
        # generates a random number to be used to pick the piece to move
        selected_num = random.randint(0, len(movable_pieces) - 1)
        print("movable pieces", movable_pieces)
        x = 0
        print("selected_num", selected_num)
        # I THINK THIS WORKS BUT IT COULD CAUSE AN ERROR WHEN MORE PIECES ARE ON THE BOARD. NEEDS FURTHER TESTING
        # IF RANDOM NUMBER SELECTED HAS NO AVAILABLE MOVES IT DOESN'T LOOK LIKE THE SELECTED NUMBER IS BEING RESET. THIS
        # NEEDS MORE TESTING WHEN THE FULL BOARD IS INITIALIZED
        while bot.selected == None:
            for piece in movable_pieces:
                # uses the selected number to find the piece at that point in the list. if the piece is movable it
                # becomes selected and calls make move
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
        """
        this function scans the surrounding areas of the piece to determine if a move can be made
        :param self / bot: the bot itself
        :param selected_piece: the piece selected by the selected piece function
        :param bot_pieces: the list of the bots total pieces
        :returns boolean: true or false depending on if the piece can move in one or more of directions left, right, up,
                          or down
        """
        x = selected_piece.getPosition()[0]
        y = selected_piece.getPosition()[1]
        leftMovement = True
        rightMovement = True
        upMovement = True
        downMovement = True
        # This scans through each piece in the bots pieces to see if any of them are directly above, below, to the right
        # or to the left of the selected piece. if they are it restricts movement in that respective direction. This
        # also accounts for the size of the board so that moves don't move pieces off the board itself
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
        """
        This function takes makes the selected piece move to a randomized location depending on if the move is
        available/legal and the difficulty selected by the user
        :param bot / self: the bot itself
        :param bot_pieces: a list of all the bots pieces
        :param user_pieces: a list of all the users pieces
        """
        # This creates a list of pieces excluding the lakes, this way the bot doesn't get confused and attempt to attack
        # a lake
        lakelessUserPieces = []
        for i in user_pieces:
            if i.getType() != "Lke":
                lakelessUserPieces.append(i)
        for i in lakelessUserPieces:
            print(i.getType())
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
        # for selected pieces that are not scouts  this generates a list of boolean values stating if movement is
        # possible in the respective direction. The order of this list is important as each value and its position
        # relate to the direction in question. The Order of this list is left, right, up, down
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
            # If the bot AI has a higher difficulty it has more preference to moving down, left and right. this way the
            # movements are more aggressive than if they were truly random. now the bot moves towards the opponent more
            # than it goes away from the opponent
            if bot.ai == 2:
                movement.append(leftMovement)
                movement.append(rightMovement)
                movement.append(downMovement)
            # if the bot AI has the highest difficulty it has the highest preference to downward movement, then the
            # second-highest preference towards left and right movement, followed by the lowest preference of upward
            # movement
            elif bot.ai == 3:
                movement.append(leftMovement)
                movement.append(rightMovement)
                movement.append(downMovement)
                movement.append(downMovement)
        # if the selected piece is a scout it has to be handled differently since scouts can move more than one space
        elif bot.selected.getType() == "Sct":
            canAttackRight = []
            canAttackLeft = []
            canAttackUp = []
            canAttackDown = []
            # these while loops check if there are any pieces at any distance to the immediate right, left, above or
            # below of the selected piece and creates a list with the length of how many moves can be made in that
            # direction without landing on top of another piece
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

        # this checks to see if there are any enemy pieces within range of the selected piece and sets a
        # boolean value to true if there is a possible capture and it also sets the piece available to capture to a
        # value to be accessed later
        possibleCaptureRight = False
        possibleCaptureLeft = False
        possibleCaptureUp = False
        possibleCaptureDown = False
        for j in user_pieces:
            print("not capture position left", j.getPosition())
            print("test left loc", x - (len(leftMovementList) + 1))
            print("test right loc", x + (len(rightMovementList) + 1))
            print("test up loc", y + (len(upMovementList) + 1))
            print("test down loc", y - (len(downMovementList) + 1))
            if bot.selected.getType() == "Sct":
                if x - (len(leftMovementList) + 1) == j.getPosition()[0] and y == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureLeft = True
                    leftCapturePiece = j
                if x + (len(rightMovementList) + 1) == j.getPosition()[0] and y == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureRight = True
                    rightCapturePiece = j
                if x == j.getPosition()[0] and y + (len(upMovementList) + 1) == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureUp = True
                    upCapturePiece = j
                if x == j.getPosition()[0] and y - (len(downMovementList) + 1) == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureDown = True
                    downCapturePiece = j
            else:
                if x - 1 == j.getPosition()[0] and y == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureLeft = True
                    leftCapturePiece = j
                if x + 1 == j.getPosition()[0] and y == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureRight = True
                    rightCapturePiece = j
                if x == j.getPosition()[0] and y + 1 == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureUp = True
                    upCapturePiece = j
                if x == j.getPosition()[0] and y - 1 == j.getPosition()[1] and j.getPlayer() == 1:
                    print("capture")
                    possibleCaptureDown = True
                    downCapturePiece = j

        isCaptureAvailable = False
        # The following if statement check for a possible capture and set weather or not the computer attempts to
        # capture the piece to a random value if the AI difficulty is more than 1 otherwise it immediately attempts to
        # capture any piece the moment it is in range
        if bot.ai != 1:
            if possibleCaptureRight or possibleCaptureUp or possibleCaptureDown or possibleCaptureLeft:
                isCaptureAvailable = True
                captureOrFlee = random.randint(0, 1)
            else:
                captureOrFlee = 0
        if bot.ai == 1:
            if possibleCaptureRight or possibleCaptureUp or possibleCaptureDown or possibleCaptureLeft:
                isCaptureAvailable = True
                captureOrFlee = 1
            else:
                captureOrFlee = 0
        if captureOrFlee == 1:
            if possibleCaptureRight:
                draw_piece.combat(bot.selected, rightCapturePiece, [BOARD_RIGHT - 25 + BOARD_MARGIN * rightCapturePiece.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * rightCapturePiece.getPosition()[1]], gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
            elif possibleCaptureLeft:
                draw_piece.combat(bot.selected, leftCapturePiece, [BOARD_LEFT + 25 + BOARD_MARGIN * leftCapturePiece.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * leftCapturePiece.getPosition()[1]], gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
            elif possibleCaptureDown:
                draw_piece.combat(bot.selected, downCapturePiece,
                                  [BOARD_LEFT + 25 + BOARD_MARGIN * downCapturePiece.getPosition()[0], BOARD_BOTTOM + 25 + BOARD_MARGIN * downCapturePiece.getPosition()[1]],
                                  gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)
            elif possibleCaptureUp:
                draw_piece.combat(bot.selected, upCapturePiece,
                                  [BOARD_RIGHT - 25 + BOARD_MARGIN * upCapturePiece.getPosition()[0], BOARD_TOP - 25 + BOARD_MARGIN * upCapturePiece.getPosition()[1]],
                                  gameboard.graveyard1, gameboard.graveyard2, gameboard.p1_pieces, gameboard.p2_pieces)

        # All non attack based movement is executed here
        else:
            # if the selected piece is not a scout then a random integer is generated that is used to determine the
            # direction of movement
            bot_move = 0
            if bot.selected.getType() != "Sct":
                bot_move = random.randint(0, len(movement) - 1)
                print(bot_move)
                while movement[bot_move] == False:
                    bot_move = random.randint(0, len(movement) - 1)
                    print(bot_move)
                move = "error"
                print("ai", bot.ai)
            if bot.ai == 1 and bot.selected.getType() != "Sct":
                bot.moves_for_ai_1_no_sct(self, bot_move)
            if bot.ai == 1 and bot.selected.getType() == "Sct":
                bot.moves_for_ai_1_sct(self, leftMovementList, rightMovementList, upMovementList, downMovementList)
            if bot.ai == 2 and bot.selected.getType() != "Sct":
                bot.moves_for_ai_2_no_sct(self, bot_move, possibleCaptureLeft, possibleCaptureRight, possibleCaptureUp,
                                          possibleCaptureDown, movement)
            if bot.ai == 2 and bot.selected.getType() == "Sct":
                bot.moves_for_ai_2_sct(self, leftMovementList, rightMovementList, upMovementList, downMovementList)
            if bot.ai == 3 and bot.selected.getType() != "Sct":
                bot.moves_for_ai_3_no_sct(self, bot_move, possibleCaptureLeft, possibleCaptureRight, possibleCaptureUp,
                                          possibleCaptureDown, movement)
            if bot.ai == 3 and bot.selected.getType() == "Sct":
                bot.moves_for_ai_3_sct(self, leftMovementList, rightMovementList, upMovementList, downMovementList)

    def moves_for_ai_1_no_sct(self, bot_move):
        """
        this function makes the piece move if the selected piece is not a scout and the AI is at a difficulty of 1
        :param self / bot: the bot itself
        :param bot_move: the random number representing the direction of movement
        """
        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        # this makes the moves for all non scout pieces with bot difficulties of 1
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

    def moves_for_ai_1_sct(self, leftMovementList, rightMovementList, upMovementList,
                                   downMovementList):
        """
        this function executes the moves for selected scout pieces with AI difficulties of 1
        :param leftMovementList: a list that has a size equal to that of how many moves to the left the selected piece
                                 can make
        :param rightMovementList: a list that has a size equal to that of how many moves to the right the selected piece
                                  can make
        :param upMovementList: a list that has a size equal to that of how many moves up the selected piece
                               can make
        :param downMovementList: a list that has a size equal to that of how many moves down the selected piece
                                 can make
        """
        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        # if the selected piece is a scout then the movement needs to have a randomized magnitude generated as well
        # this generates that so that the scout can move any distance it wants under the difficulty 1
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
                movement_magnitude = random.randint(1, len(leftMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x - movement_magnitude, y)
            if SctMovement[bot_move] == "right":
                direction = "right"
                movement_magnitude = random.randint(1, len(rightMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x + movement_magnitude, y)
            if SctMovement[bot_move] == "up":
                direction = "up"
                movement_magnitude = random.randint(1, len(upMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x, y + movement_magnitude)
            if SctMovement[bot_move] == "down":
                direction = "down"
                movement_magnitude = random.randint(1, len(downMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x, y - movement_magnitude)

    def moves_for_ai_2_no_sct(self, bot_move, possibleCaptureLeft, possibleCaptureRight, possibleCaptureUp, possibleCaptureDown, movement):
        """
        this function makes the piece move if the selected piece is not a scout and the AI is at a difficulty of 2
        :param self / bot: the bot itself
        :param bot_move: the random number representing the direction of movement
        """
        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        # this makes the movements for all non scout pieces that have a bot difficulty of 2
        if bot.ai == 2 and bot.selected.getType() != "Sct":
            # this checks to make sure that the selected moves aren't going to be captures, if they are it
            # re-randomizes the move
            if possibleCaptureLeft:
                # cannot move, re select movement
                while bot_move == 0 or bot_move == 4:
                    bot_move = random.randint(0, len(movement) - 1)
            if possibleCaptureRight:
                # cannot move, re select movement
                while bot_move == 1 or bot_move == 5:
                    bot_move = random.randint(0, len(movement) - 1)
            if possibleCaptureUp:
                while bot_move == 2:
                    bot_move = random.randint(0, len(movement) - 1)
            if possibleCaptureDown:
                while bot_move == 3 or bot_move == 6:
                    bot_move = random.randint(0, len(movement) - 1)
            # the following if statements make the moves for the piece
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

    def moves_for_ai_2_sct(self, leftMovementList, rightMovementList, upMovementList, downMovementList):
        """
        this function executes the moves for selected scout pieces with AI difficulties of 2
        :param leftMovementList: a list that has a size equal to that of how many moves to the left the selected piece
                                 can make
        :param rightMovementList: a list that has a size equal to that of how many moves to the right the selected piece
                                  can make
        :param upMovementList: a list that has a size equal to that of how many moves up the selected piece
                               can make
        :param downMovementList: a list that has a size equal to that of how many moves down the selected piece
                                 can make
        """
        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        # For selected pieces that are scouts and have an AI difficulty of 2, this generates random direction and
        # magnitude for the scouts movement
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
                movement_magnitude = random.randint(1, len(leftMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x - movement_magnitude, y)
            if SctMovement[bot_move] == "right":
                direction = "right"
                movement_magnitude = random.randint(1, len(rightMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x + movement_magnitude, y)
            if SctMovement[bot_move] == "up":
                direction = "up"
                movement_magnitude = random.randint(1, len(upMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x, y + movement_magnitude)
            if SctMovement[bot_move] == "down":
                direction = "down"
                movement_magnitude = random.randint(1, len(downMovementList))
                print(direction, movement_magnitude)
                bot.selected.setPosition(x, y - movement_magnitude)

    def moves_for_ai_3_no_sct(self, bot_move, possibleCaptureLeft, possibleCaptureRight, possibleCaptureUp, possibleCaptureDown, movement):
        """
        this function makes the piece move if the selected piece is not a scout and the AI is at a difficulty of 3
        :param self / bot: the bot itself
        :param bot_move: the random number representing the direction of movement
        """
        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        # this if statement handles all selected non scout pieces with AI difficulties of 3, it has to make sure
        # that any movements do not overlap with opponent pieces and if so it re-generates a random move.
        if bot.ai == 3 and bot.selected.getType() != "Sct":
            if possibleCaptureLeft:
                # cannot move, re select movement
                while bot_move == 0 or bot_move == 4:
                    bot_move = random.randint(0, len(movement) - 1)
            if possibleCaptureRight:
                # cannot move, re select movement
                while bot_move == 1 or bot_move == 5:
                    bot_move = random.randint(0, len(movement) - 1)
            if possibleCaptureUp:
                while bot_move == 2:
                    bot_move = random.randint(0, len(movement) - 1)
            if possibleCaptureDown:
                while bot_move == 3 or bot_move == 6 or bot_move == 7:
                    bot_move = random.randint(0, len(movement) - 1)
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

    def moves_for_ai_3_sct(self, leftMovementList, rightMovementList, upMovementList, downMovementList):
        """
        this function executes the moves for selected scout pieces with AI difficulties of 3
        :param leftMovementList: a list that has a size equal to that of how many moves to the left the selected piece
                                 can make
        :param rightMovementList: a list that has a size equal to that of how many moves to the right the selected piece
                                  can make
        :param upMovementList: a list that has a size equal to that of how many moves up the selected piece
                               can make
        :param downMovementList: a list that has a size equal to that of how many moves down the selected piece
                                 can make
        """
        x = bot.selected.getPosition()[0]
        y = bot.selected.getPosition()[1]
        # this if statement handles all scout movement with AI difficulties of 3, randomized movement directions and
        # magnitude must be generated
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
                movement_magnitude = 1
                print(direction, movement_magnitude)
                bot.selected.setPosition(x - movement_magnitude, y)
            if SctMovement[bot_move] == "right":
                direction = "right"
                movement_magnitude = 1
                print(direction, movement_magnitude)
                bot.selected.setPosition(x + movement_magnitude, y)
            if SctMovement[bot_move] == "up":
                direction = "up"
                movement_magnitude = 1
                print(direction, movement_magnitude)
                bot.selected.setPosition(x, y + movement_magnitude)
            if SctMovement[bot_move] == "down":
                direction = "down"
                movement_magnitude = 1
                print(direction, movement_magnitude)
                bot.selected.setPosition(x, y - movement_magnitude)
