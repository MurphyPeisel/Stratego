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

def make_move(piece, click):
    x = click[0]
    y = click[1]

    if y > 100 and y < 150:
        print("move the y coordinate to 0")
    elif y > 150 and y < 200:
        print("move the y coordinate to 1")
    elif y > 200 and y < 250:
        print("move the y coordinate to 2")
    elif y > 250 and y < 300:
        print("move the y coordinate to 3")
    elif y > 300 and y < 350:
        print("move the y coordinate to 4")
    elif y > 350 and y < 400:
        print("move the y coordinate to 5")
    elif y > 400 and y < 450:
        print("move the y coordinate to 6")
    elif y > 450 and y < 500:
        print("move the y coordinate to 7")
    elif y > 500 and y < 550:
        print("move the y coordinate to 8")
    elif y > 550 and y < 600:
        print("move the y coordinate to 9")
    if x > 200 and x < 250:
        print("move x coordinate to 0")
    elif x > 250 and x < 300:
        print("move x coordinate to 2")

def select_move(piece, click):
    pass
