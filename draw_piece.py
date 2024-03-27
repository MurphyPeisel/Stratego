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

def select_piece(piece, click):
    x = click[0]
    y = click[1]
    piecex = piece.getPosition()[0]
    piecey = piece.getPosition()[1]
    if x>=BOARD_LEFT + BOARD_MARGIN*piecex and x<=BOARD_RIGHT + BOARD_MARGIN*piecex and y<= BOARD_TOP + BOARD_MARGIN*piecey and y>= BOARD_BOTTOM + BOARD_MARGIN*piecey:
        return True
    else:
        return False

def select_move(piece, click):
    pass
