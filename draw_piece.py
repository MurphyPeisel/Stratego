import arcade
from Piece import Piece
BOARD_LEFT = 200
BOARD_MARGIN = 50
BOARD_TOP = 150
BOARD_RIGHT = 250
BOARD_BOTTOM = 100
def draw(piece):
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    point_list = ((BOARD_LEFT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y),
                    (BOARD_LEFT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                    (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                    (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y))
    arcade.draw_polygon_filled(point_list, arcade.color.BLUE)

#if given a piece and the location of a cursor click it will return true stating that you can select that piece.
def is_piece(pieces, click):
    x = click[0]
    y = click[1]
    for piece in pieces:
        piecex = piece.getPosition()[0]
        piecey = piece.getPosition()[1]
        if x>=BOARD_LEFT + BOARD_MARGIN*piecex and x<=BOARD_RIGHT + BOARD_MARGIN*piecex and y<= BOARD_TOP + BOARD_MARGIN*piecey and y>= BOARD_BOTTOM + BOARD_MARGIN*piecey:
            return True
    return False


def select_piece(piece, click):
    x = click[0]
    y = click[1]
    piecex = piece.getPosition()[0]
    piecey = piece.getPosition()[1]
    if x >= BOARD_LEFT + BOARD_MARGIN * piecex and x <= BOARD_RIGHT + BOARD_MARGIN * piecex and y <= BOARD_TOP + BOARD_MARGIN * piecey and y >= BOARD_BOTTOM + BOARD_MARGIN * piecey:
        return True
    else:
        return False

def is_move_available(pieces, piece, click):
    if is_piece(pieces, click):
        return False
    else:
        return True

def select_move(piece, click):
    x = click[0]
    y = click[1]

    locx = None
    locy = None

    if y > 100 and y < 150 and x > 200 and x < 700:
        print("move the y coordinate to 0")
        locy = 0
    elif y > 150 and y < 200 and x > 200 and x < 700:
        print("move the y coordinate to 1")
        locy = 1
    elif y > 200 and y < 250 and x > 200 and x < 700:
        print("move the y coordinate to 2")
        locy = 2
    elif y > 250 and y < 300 and x > 200 and x < 700:
        print("move the y coordinate to 3")
        locy = 3
    elif y > 300 and y < 350 and x > 200 and x < 700:
        print("move the y coordinate to 4")
        locy = 4
    elif y > 350 and y < 400 and x > 200 and x < 700:
        print("move the y coordinate to 5")
        locy = 5
    elif y > 400 and y < 450 and x > 200 and x < 700:
        print("move the y coordinate to 6")
        locy = 6
    elif y > 450 and y < 500 and x > 200 and x < 700:
        print("move the y coordinate to 7")
        locy = 7
    elif y > 500 and y < 550 and x > 200 and x < 700:
        print("move the y coordinate to 8")
        locy = 8
    elif y > 550 and y < 600 and x > 200 and x < 700:
        print("move the y coordinate to 9")
        locy = 9
    else:
        locy = None

    if x > 200 and x < 250 and y > 100 and y < 600:
        print("move x coordinate to 0")
        locx = 0
    elif x > 250 and x < 300 and y > 100 and y < 600:
        print("move x coordinate to 1")
        locx = 1
    elif x > 300 and x < 350 and y > 100 and y < 600:
        print("move x coordinate to 2")
        locx = 2
    elif x > 350 and x < 400 and y > 100 and y < 600:
        print("move x coordinate to 3")
        locx = 3
    elif x > 400 and x < 450 and y > 100 and y < 600:
        print("move x coordinate to 4")
        locx = 4
    elif x > 450 and x < 500 and y > 100 and y < 600:
        print("move x coordinate to 5")
        locx = 5
    elif x > 500 and x < 550 and y > 100 and y < 600:
        print("move x coordinate to 6")
        locx = 6
    elif x > 550 and x < 600 and y > 100 and y < 600:
        print("move x coordinate to 7")
        locx = 7
    elif x > 600 and x < 650 and y > 100 and y < 600:
        print("move x coordinate to 8")
        locx = 8
    elif x > 650 and x < 700 and y > 100 and y < 600:
        print("move x coordinate to 9")
        locx = 9
    else:
        locx = None

    if locx != None and locy != None:
        return make_move(piece, locx, locy)
    else:
        return None

# right now erase just places a square over the top of the piec location. if this causes lag or other things we should look into how to remove drawings
def erase(piece):
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    point_list = ((BOARD_LEFT + BOARD_MARGIN * x, BOARD_TOP + BOARD_MARGIN * y),
                  (BOARD_LEFT + BOARD_MARGIN * x, BOARD_BOTTOM + BOARD_MARGIN * y),
                  (BOARD_RIGHT + BOARD_MARGIN * x, BOARD_BOTTOM + BOARD_MARGIN * y),
                  (BOARD_RIGHT + BOARD_MARGIN * x, BOARD_TOP + BOARD_MARGIN * y))
    arcade.draw_polygon_filled(point_list, arcade.color.GRANNY_SMITH_APPLE)
def make_move(piece, locx, locy):
    erase(piece)
    piece.setPosition(locx, locy)
    draw(piece)
