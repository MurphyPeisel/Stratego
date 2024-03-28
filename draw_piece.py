import arcade
from Piece import Piece
from constants import *

def draw(piece):
    x, y = piece.getPosition()
    point_list = ((BOARD_LEFT + BOARD_MARGIN * x, BOARD_TOP + BOARD_MARGIN * y),
                    (BOARD_LEFT + BOARD_MARGIN * x, BOARD_BOTTOM + BOARD_MARGIN * y),
                    (BOARD_RIGHT + BOARD_MARGIN * x, BOARD_BOTTOM + BOARD_MARGIN * y),
                    (BOARD_RIGHT + BOARD_MARGIN * x, BOARD_TOP + BOARD_MARGIN * y))
    if piece.getType() == "Sct":
        arcade.draw_polygon_filled(point_list, arcade.color.BLUE)
    elif piece.getType() == "Gen":
        arcade.draw_polygon_filled(point_list, arcade.color.VIOLET)
    elif piece.getType() == "Bom":
        arcade.draw_polygon_filled(point_list, arcade.color.RED)
    elif piece.getType() == "Msh":
        arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
    elif piece.getType() == "Flg":
        arcade.draw_polygon_filled(point_list, arcade.color.WHITE)

#if given a piece and the location of a cursor click it will return true stating that you can select that piece.
def is_piece(pieces, click):
    """ 
    Checks if there is a piece at the location of a cursor click.
    :param pieces: List of all pieces
    :param click: Cursor click location (x, y)
    :return: Tuple containing bool of if there is a piece at the location and the piece there if so
    :rtype: (bool, Piece)
    """
    x, y = click
    for piece in pieces:
        piece_x, piece_y = piece.getPosition()
        if (x >= BOARD_LEFT + BOARD_MARGIN * piece_x and 
            x <= BOARD_RIGHT + BOARD_MARGIN * piece_x and 
            y <= BOARD_TOP + BOARD_MARGIN * piece_y and 
            y>= BOARD_BOTTOM + BOARD_MARGIN * piece_y):
            return (True, piece)
    return (False, None)

def select_piece(piece, click):
    x, y = click
    piece_x, piece_y = piece.getPosition()
    if (x >= BOARD_LEFT + BOARD_MARGIN * piece_x and 
        x <= BOARD_RIGHT + BOARD_MARGIN * piece_x and
        y <= BOARD_TOP + BOARD_MARGIN * piece_y and 
        y >= BOARD_BOTTOM + BOARD_MARGIN * piece_y):
        if piece.getType() == "Bom" or piece.getType() == "Flg":
            print(f"{piece.getType()} is not selectable. Select another piece.")
            return False
        else:
            # show_available_moves(piece)
            return True
    else:
        return False

# TO IMPLEMENT IN SPRINT 3 
# def show_available_moves(piece):
#     x = piece.getPosition()[0]
#     y = piece.getPosition()[1]
#     points_list = ((BOARD_LEFT + BOARD_MARGIN, BOARD_TOP + BOARD_MARGIN),
#                    (BOARD_LEFT + BOARD_MARGIN, BOARD_BOTTOM + BOARD_MARGIN),
#                    (BOARD_RIGHT + BOARD_MARGIN, BOARD_BOTTOM + BOARD_MARGIN),
#                    (BOARD_RIGHT + BOARD_MARGIN, BOARD_TOP + BOARD_MARGIN))
#     arcade.draw_polygon_filled(points_list, arcade.color.BLACK)

def is_move_available(pieces, piece, click):
    """ 
    Checks if a piece's move is valid.
    :param pieces: List of all pieces
    :param piece: Selected piece
    :param click: Cursor click location (x, y)
    :return: Tuple containing bool of if the move is available and the piece at that location if so 
    :rtype: (bool, Piece)
    """
    try:
        loc_x, loc_y = get_coordinates(click)
    except TypeError:
        print("Invalid move. Cannot convert out-of-bound click to x,y coordinates.")
        return (False, None)
    else:
        piece_loc_x, piece_loc_y = piece.getPosition()
        piece_exists, selected_piece = is_piece(pieces, click)
        if piece_exists:
            if selected_piece.getPlayer() != piece.getPlayer():
                return (True, selected_piece)
            else:
                return (False, None)
        else:
            if piece.getType() == "Sct":
                if loc_x != piece_loc_x and loc_y != piece_loc_y:
                    print("invalid please try again")
                    return (False, None)
                else:
                    is_jump = False
                    x = piece_loc_x
                    y = piece_loc_y
                    while x < loc_x:
                        if is_piece(pieces, [x, y])[0] == False:
                            x = x + 1
                        else:
                            print("jump detected")
                            is_jump = True
                            return (False, None)
                    return (True, None)
            else:
                if loc_x != piece_loc_x and loc_y != piece_loc_y:
                    print("invalid please try again")
                    return (False, None)
                if loc_x > piece_loc_x + 1:
                    print("invalid please try again")
                    return (False, None)
                if loc_x < piece_loc_x - 1:
                    print("invalid please try again")
                    return (False, None)
                if loc_y > piece_loc_y + 1:
                    print("invalid please try again")
                    return (False, None)
                if loc_y < piece_loc_y - 1:
                    print("invalid please try again")
                    return (False, None)
                else:
                    return (True, None)
                
def get_coordinates(click):
    """ 
    Converts cursor click to coordinates on grid
    :param click: Cursor click location (x, y)
    :return: Tuple of x,y coordinates on grid
    :rtype: (int, int)
    """
    x, y = click
    # click in grid
    if x >= GRID_LEFT and x <= GRID_RIGHT and y >= GRID_BOTTOM and y <= GRID_TOP:   
        loc_y = ROW_COUNT - 1 - abs(GRID_TOP - y) // CELL_WIDTH # ROW_COUNT - 1 to flip y-coordinate (bottom left cell is 0,0)
        loc_x = abs(x - GRID_LEFT) // CELL_WIDTH
        coordinates = (loc_x, loc_y)
        print(f"(x,y): {coordinates}")
        return coordinates
    # click in left graveyard
    # elif:
    #     pass
    # click in right graveyard
    # elif:
    #     pass
    else:
        return None

def move_piece(piece, click):
    """ 
    Updates a piece's x, y location on grid
    :param piece: Piece to be moved
    :param click: Cursor click location (x, y)
    """
    try:
        loc_x, loc_y = get_coordinates(click)
    except TypeError:
        print("Invalid move. Cannot convert out-of-bound click to x,y coordinates.")
    else:
        piece.setPosition(loc_x, loc_y)

def combat(attacker, defender, click):
    """ 
    Combat between two pieces. If the attacking piece 
    :param attacker: Attacking piece
    :param defender: Defending piece
    :param click: Cursor click location (x, y)
    """
    print("COMBAT")
    print(f"attacker located at {attacker.getPosition()}, type: {attacker.getType()}, power: {attacker.getPower()}")
    print(f"defender located at {defender.getPosition()}, type: {defender.getType()}, power: {defender.getPower()}")
    if attacker.getPower() > defender.getPower():
        print("attacker wins")
        defender.defeated = True
        move_piece(attacker, click)
    elif attacker.getPower() < defender.getPower():
        print("defender wins")
        attacker.defeated = True
        move_piece(defender, click)
    else:
        print("attacker and defender defeated")
        attacker.defeated = True
        defender.defeated = True

