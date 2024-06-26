import arcade
from Piece import *
from constants import *
import game_settings
import pass_turn
import time
import gameboard as Gameboard
import sound_settings



def draw_start(piece, army, index):
    yard_left = 0
    if army == PLAYER_ONE:
        yard_left = GRAVEYARD_1_LEFT
        color = arcade.color.BLUE
    else:
        yard_left = GRAVEYARD_2_LEFT
        color = arcade.color.RED
   
    row = index // GRAVEYARD_CELLS_WIDE
    point_list = ((yard_left+YARD_MARGIN*(index - GRAVEYARD_CELLS_WIDE*row),GRAVEYARD_TOP - YARD_MARGIN*row), 
                  (yard_left+YARD_MARGIN*(index - GRAVEYARD_CELLS_WIDE*row), (GRAVEYARD_TOP - YARD_MARGIN*row) - 40),
                  (yard_left+(YARD_MARGIN * (index-GRAVEYARD_CELLS_WIDE*row)) + 40, (GRAVEYARD_TOP - YARD_MARGIN*row)-40),
                  (yard_left+(YARD_MARGIN * (index-GRAVEYARD_CELLS_WIDE*row)) + 40, GRAVEYARD_TOP - YARD_MARGIN*row))
    arcade.draw_polygon_filled(point_list, color)

    if piece.getType() == "Flg":
        arcade.draw_text("F", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+13, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    elif piece.getType() == "Msh":
        arcade.draw_text("10", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+5, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    elif piece.getType() == "Gen":
        arcade.draw_text("9", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    if piece.getType() == "Col":
        arcade.draw_text("8", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    if piece.getType() == "Maj":
        arcade.draw_text("7", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    if piece.getType() == "Cap":
        arcade.draw_text("6", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    if piece.getType() == "Ltn":
        arcade.draw_text("5", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    if piece.getType() == "Sgt":
        arcade.draw_text("4", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    if piece.getType() == "Min":
        arcade.draw_text("3", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    elif piece.getType() == "Sct":
        arcade.draw_text("2", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+12, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    elif piece.getType() == "Spy":
        arcade.draw_text("S", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+13, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)
    elif piece.getType() == "Bom":
        arcade.draw_text("B", yard_left+YARD_MARGIN*(index-GRAVEYARD_CELLS_WIDE*row)+13, GRID_TOP-YARD_MARGIN*row-33, arcade.color.WHITE, 20, 1, "center", "Kenney Pixel Square Font", bold=True)

    if piece.getType() == "Lke":
        arcade.draw_polygon_filled(point_list, arcade.color.BLACK)


def is_enemy(piece, player_turn):
    if piece.getPlayer() != player_turn:
        return True
    else:
        return False
        
def add_highlight(army, index):
    if army == 1:
        yard_left = GRAVEYARD_1_LEFT
    else:
        yard_left = GRAVEYARD_2_LEFT
    
    row = index // GRAVEYARD_CELLS_WIDE
    
    point_list = ((yard_left+YARD_MARGIN*(index - GRAVEYARD_CELLS_WIDE*row),GRAVEYARD_TOP - YARD_MARGIN*row), 
                  (yard_left+YARD_MARGIN*(index - GRAVEYARD_CELLS_WIDE*row), (GRAVEYARD_TOP- YARD_MARGIN*row) - 40),
                  (yard_left+(YARD_MARGIN * (index-GRAVEYARD_CELLS_WIDE*row)) + 40, (GRAVEYARD_TOP - YARD_MARGIN*row)-40),
                  (yard_left+(YARD_MARGIN * (index-GRAVEYARD_CELLS_WIDE*row)) + 40, GRAVEYARD_TOP - YARD_MARGIN*row))
    arcade.draw_polygon_outline(point_list, arcade.color.GREEN, 4)


def draw(piece, army):
    if army == 1:
        color = arcade.color.BLUE
    else:
        color = arcade.color.RED
    
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    point_list = (((BOARD_LEFT+10) + YARD_MARGIN*x, (BOARD_TOP-10) + YARD_MARGIN*y),
                    ((BOARD_LEFT+10) + YARD_MARGIN*x, (BOARD_BOTTOM+10) + YARD_MARGIN*y),
                    ((BOARD_RIGHT-10) + YARD_MARGIN*x, (BOARD_BOTTOM+10) + YARD_MARGIN*y),
                    ((BOARD_RIGHT-10) + YARD_MARGIN*x, (BOARD_TOP-10) + YARD_MARGIN*y))
    
    if piece.getType() == "Lke":
        color = arcade.color.BLUEBERRY
    arcade.draw_polygon_filled(point_list, color)


    down = 10-y
    if game_settings.Computer.sight:
        if piece.getType() == "Flg":
            arcade.draw_text("F", BOARD_LEFT+YARD_MARGIN*x +16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Blocks Font", bold=True)
        elif piece.getType() == "Msh":
            arcade.draw_text("10", BOARD_LEFT+YARD_MARGIN*x + 12, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Rocket Square Font", bold=True)
        elif piece.getType() == "Gen":
            arcade.draw_text("9", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        if piece.getType() == "Col":
            arcade.draw_text("8", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        if piece.getType() == "Maj":
            arcade.draw_text("7", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        if piece.getType() == "Cap":
            arcade.draw_text("6", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        if piece.getType() == "Ltn":
            arcade.draw_text("5", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        if piece.getType() == "Sgt":
            arcade.draw_text("4", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        if piece.getType() == "Min":
            arcade.draw_text("3", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        elif piece.getType() == "Sct":
            arcade.draw_text("2", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        elif piece.getType() == "Spy":
            arcade.draw_text("S", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
        elif piece.getType() == "Bom":
            arcade.draw_text("B", BOARD_LEFT+YARD_MARGIN*x +16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
    else:
        if army == pass_turn.Pass_Turn.player_turn and piece.getHidden() == True:
            if piece.getType() == "Flg":
                    arcade.draw_text("F", BOARD_LEFT+YARD_MARGIN*x +16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Blocks Font", bold=True)
            elif piece.getType() == "Msh":
                arcade.draw_text("10", BOARD_LEFT+YARD_MARGIN*x + 12, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Rocket Square Font", bold=True)
            elif piece.getType() == "Gen":
                arcade.draw_text("9", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            if piece.getType() == "Col":
                arcade.draw_text("8", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            if piece.getType() == "Maj":
                arcade.draw_text("7", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            if piece.getType() == "Cap":
                arcade.draw_text("6", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            if piece.getType() == "Ltn":
                arcade.draw_text("5", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            if piece.getType() == "Sgt":
                arcade.draw_text("4", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            if piece.getType() == "Min":
                arcade.draw_text("3", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            elif piece.getType() == "Sct":
                arcade.draw_text("2", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            elif piece.getType() == "Spy":
                arcade.draw_text("S", BOARD_LEFT+YARD_MARGIN*x + 16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)
            elif piece.getType() == "Bom":
                arcade.draw_text("B", BOARD_LEFT+YARD_MARGIN*x +16, GRID_TOP-YARD_MARGIN*down + 16, arcade.color.WHITE, 18, 1, "center", "Kenney Pixel Square Font", bold=True)

        
    if piece.getType() == "Flg":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    elif piece.getType() == "Msh":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    elif piece.getType() == "Gen":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    if piece.getType() == "Col":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    if piece.getType() == "Maj":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    if piece.getType() == "Cap":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    if piece.getType() == "Ltn":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    if piece.getType() == "Sgt":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    if piece.getType() == "Min":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    elif piece.getType() == "Sct":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    elif piece.getType() == "Spy":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)
    elif piece.getType() == "Bom":
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 2)


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


def is_piece_scan(pieces, loc):
    """
    Checks if there is a piece at the location of a provided coordinate set, this is to be used inside the show
    available moves function so that it only returns the necessary values.
    :param pieces: List of all pieces
    :param loc: location to check for a piece (x, y)
    :return boolean value: This value represents whether there is a piece at the given location
    """
    x = loc[0]
    y = loc[1]
    for piece in pieces:
        piecex = piece.getPosition()[0]
        piecey = piece.getPosition()[1]
        if (x>=BOARD_LEFT + BOARD_MARGIN*piecex and 
            x<=BOARD_RIGHT + BOARD_MARGIN*piecex and 
            y<= BOARD_TOP + BOARD_MARGIN*piecey and 
            y>= BOARD_BOTTOM + BOARD_MARGIN*piecey):
            return True
    return False

def select_yard_piece(piece, army, click, index):
    yard_left = 0
    if army == 1:
        yard_left = GRAVEYARD_1_LEFT
    else:
        yard_left = GRAVEYARD_2_LEFT    
    
    row = index // GRAVEYARD_CELLS_WIDE

    x, y = click
    
    

def select_piece(piece, click, player_turn):
    """
    This function checks if a piece is at the given click coordinates and is one selectable / can be moved. Pieces like
    bombs, flags or lakes cannot be moved or "played with"
    :param piece: the piece clicked on and the location of the click
    :param click: location of the users click
    :return boolean value: This value represents whether the piece selected is one that can be moved by the user
    """
    hold = piece.getPosition()
    coords = get_coordinates(click)
    
    if (coords[0] == hold[0] and coords[1] == hold[1]):
        if piece.getType() == "Bom" or piece.getType() == "Flg" or piece.getType() == "Lke" or piece.getPlayer() != player_turn:
            return False
        else:
            return True
    else:
        return False

def show_available_placements(total_pieces, player):
    loc = [0,0]
    
    next_i = 5
    if player == 1:
        y=0
        while (y < 4):
                x = 0
                while (x < 10):
                    arcade.draw_arc_filled(center_x= BOARD_LEFT+25+50*x, center_y=BOARD_BOTTOM+25 + y*50, width=10, height=10, color=arcade.color.WHITE, start_angle=0, end_angle=360)
                    arcade.draw_arc_outline(center_x= BOARD_LEFT+25+50*x, center_y=BOARD_BOTTOM+25 + y*50, width=10, height=10, color=arcade.color.BLACK, start_angle=0, end_angle=360, border_width=3)
                    x = x + 1
                y = y + 1
    else:
        y= 6
        while (y < 10):
                x = 0
                while (x < 10):
                    arcade.draw_arc_filled(center_x= BOARD_LEFT+25+50*x, center_y=BOARD_TOP*4-(25 + (y-6)*50), width=10, height=10, color=arcade.color.WHITE, start_angle=0, end_angle=360)
                    arcade.draw_arc_outline(center_x= BOARD_LEFT+25+50*x, center_y=BOARD_TOP*4-(25 + (y-6)*50), width=10, height=10, color=arcade.color.BLACK, start_angle=0, end_angle=360, border_width=3)
                    x = x + 1
                y = y + 1
        
# Board Setup: Determines if pieces are placed on the board or into the graveyard. Toggle Function  
def place_piece(piece, click, graveyard, army):
    coords = get_coordinates(click)
    if is_piece_scan(army, click) == False:
        try:
            piece.setPosition(coords[0], coords[1])
        except Exception:
            pass
        army.append(piece)
        graveyard.remove(piece)
    else:
        for piece in army:
            if piece.getPosition()[0] == coords[0] and piece.getPosition()[1] == coords[1]:
                graveyard.append(piece)
                army.remove(piece)
        

def show_available_moves(piece, total_pieces):
    """
    This function takes in the selected piece and a list of all the total pieces in play. The function identifies if
    the piece has a unique movement type (scout) or is standard. It then draws a circle on every part of the game-board
    where the piece can move to. It will not draw a circle if there is a piece occupying that space or if the move in
    question moves the piece outside the game-board
    :param piece: the piece selected to be moved. this provides the location for all available moves to be drawn from
    :param total_pieces: location of all the pieces in the game
    :return: This function returns no values
    """
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    # This portion of the function draws circles to the left, right, above, and below a selected piece if the piece is
    # not a scout and there is no piece occupying the space in question and the piece itself is not at the edge of the
    # board
    if piece.getType() != "Sct":

        # Right scan
        if (is_piece_scan(total_pieces, [BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_RIGHT + 25 + BOARD_MARGIN * x < 700):
            arcade.draw_arc_filled(BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)

        if (is_piece_scan(total_pieces, [BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == True and BOARD_RIGHT + 25 + BOARD_MARGIN * x < 700):
            if is_enemy(is_piece(total_pieces, [BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1].getType() != "Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "right", BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 5, arcade.color.GREEN)


        # up scan
        if (is_piece_scan(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y]) == False and BOARD_TOP + 25 + BOARD_MARGIN * y < 600):
            arcade.draw_arc_filled(BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)

        if (is_piece_scan(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y]) == True and BOARD_TOP + 25 + BOARD_MARGIN * y < 600):
            if is_enemy(is_piece(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y])[1].getType() != "Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "up", BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y, 5, arcade.color.GREEN)


        # down scan
        if (is_piece_scan(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y]) == False and BOARD_BOTTOM - 25 + BOARD_MARGIN * y > 100):
            arcade.draw_arc_filled(BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)

        if (is_piece_scan(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x,
                                         BOARD_BOTTOM - 25 + BOARD_MARGIN * y]) == True and BOARD_BOTTOM - 25 + BOARD_MARGIN * y > 100):
            if is_enemy(is_piece(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y])[1].getType() != "Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "down", BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y, 5, arcade.color.GREEN)

        # left scan
        if (is_piece_scan(total_pieces, [BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_LEFT - 25 + BOARD_MARGIN * x > 200):
            arcade.draw_arc_filled(BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)

        if (is_piece_scan(total_pieces, [BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == True and BOARD_LEFT - 25 + BOARD_MARGIN * x > 200):
            if is_enemy(is_piece(total_pieces, [BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1].getType() != "Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "left", BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 5, arcade.color.GREEN)


    # if the piece is a scout then this portion of the function scans through all the spaces directly to the left,
    # right, above, and below. This portion of the function draws a circle at every space so long as it is not beyond
    # the board space and there is no other piece in the way. The scan will halt any time it detects the edge of the
    # board or another piece, this way the available moves do not imply the ability to jump over other pieces
    if piece.getType() == "Sct":
        next_i = 1
        # Right
        while (is_piece_scan(total_pieces, [BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x < 700):
            arcade.draw_arc_filled(BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_i = next_i + 2
        if is_piece_scan(total_pieces, [BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == True and BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x < 700:
            if is_enemy(is_piece(total_pieces, [BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1].getType() != "Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "right", BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 5, arcade.color.GREEN)

        next_j = 1
        # up
        while (is_piece_scan(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y]) == False and BOARD_TOP + 25 * next_j + BOARD_MARGIN * y < 600):
            arcade.draw_arc_filled(BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_j = next_j + 2
        if (is_piece_scan(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y]) == True and BOARD_TOP + 25 * next_j + BOARD_MARGIN * y < 600):
            if is_enemy(is_piece(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y])[1].getType() !="Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "up", BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y, 5, arcade.color.GREEN)
        next_j = 1
        # down
        while (is_piece_scan(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y]) == False and BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y > 100):
            arcade.draw_arc_filled(BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_j = next_j + 2
        if (is_piece_scan(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y]) == True and BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y > 100):
            if is_enemy(is_piece(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y])[1].getType() !="Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "down", BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y, 5, arcade.color.GREEN)
        next_i = 1
        while (is_piece_scan(total_pieces, [BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x > 200):
            arcade.draw_arc_filled(BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_i = next_i + 2
        if (is_piece_scan(total_pieces, [BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == True and BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x > 200):
            if is_enemy(is_piece(total_pieces, [BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1], piece.getPlayer()) and is_piece(total_pieces, [BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y])[1].getType() !="Lke":
                Gameboard.Gameboard.setAttack(Gameboard, "left", BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 5, arcade.color.GREEN)


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
                # player has selected an opposing piece
                return (True, selected_piece)
            else:
                return (False, None)
        else:
            if piece.getType() == "Sct":
                # This checks to make sure that the user isn't attempting to move the piece diagonally
                if loc_x != piece_loc_x and loc_y != piece_loc_y:
                    return (False, None)
                else:
                    # this converts the location of the piece from the game-board coordinates to the coordinates of the
                    # window
                    x = (piece_loc_x * 50) + 225
                    y = (piece_loc_y * 50) + 125
                    # This converts the coordinates of the users click to coordinates of the game-board
                    locx_tester = BOARD_LEFT + BOARD_MARGIN * loc_x
                    locy_tester = BOARD_BOTTOM + BOARD_MARGIN * loc_y

                    # This tests for if the user attempts rightward movement of the piece
                    if x < locx_tester and loc_x != piece_loc_x:
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        while x < locx_tester:
                            # Moves the x coordinate over to the next piece over to scan
                            x = x + 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                pass
                            else:
                                return (False, None)
                    # This tests for if the user attempts leftward movement of the piece
                    elif x > locx_tester and loc_x != piece_loc_x:
                        # This re-assigns the location of the tester value so that scanning attempts from this point
                        # can work without overlapping between two possible piece coordinates
                        locx_tester = BOARD_RIGHT + BOARD_MARGIN * loc_x
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        while x > locx_tester:
                            # This moves the location of the point in which the scanner scans for a piece to the left
                            # for each loop through
                            x = x - 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                pass
                            else:
                                return (False, None)
                    # This section of the function tests for upward movement of the piece selected
                    elif y < locy_tester and loc_y != piece_loc_y:
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        while y < locy_tester:
                            # This moves the location in which the scanner scans the piece to the next location above
                            # the selected piece
                            y = y + 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                pass
                            else:
                                return (False, None)
                    # This section of the function tests for downward movement of the selected piece
                    elif y > locy_tester and loc_y != piece_loc_y:
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        # This re-assigns the location of th y value tester so that the distance moved for the scanner
                        # is accommodated and doesn't overlap across different piece spaces
                        locy_tester = BOARD_TOP + BOARD_MARGIN * loc_y
                        while y > locy_tester:
                            y = y - 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                pass
                            else:
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
        return coordinates
    else:
        return click

    
def move_to_graveyard(army, piece, graveyard):
    """ 
    Sends a piece to its graveyard
    :param army: List of active pieces
    :param piece: Piece 
    :param graveyard: List of inactive pieces
    """
    piece.defeated = True
    piece.setPosition(-1, -1)
    army.remove(piece)
    graveyard.append(piece)
    Gameboard.selected = None
    

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
        Gameboard.Gameboard.resetAttack(Gameboard)

def convert_piece_type(piece):
    """ 
    Converts piece short name to long name
    :param piece: Piece 
    :return: Piece long name
    :rtype: String
    """
    if piece.getType() == "Flg":
        return "FLAG"
    elif piece.getType() == "Msh":
        return "MARSHALL"
    elif piece.getType() == "Gen":
        return "GENERAL"
    if piece.getType() == "Col":
        return "COLONEL"
    if piece.getType() == "Maj":
        return "MAJOR"
    if piece.getType() == "Cap":
        return "CAPTAIN"
    if piece.getType() == "Ltn":
        return "LIEUTENANT"
    if piece.getType() == "Sgt":
        return "SERGEANT"
    if piece.getType() == "Min":
        return "MINER"
    elif piece.getType() == "Sct":
        return "SCOUT"
    elif piece.getType() == "Spy":
        return "SPY"
    elif piece.getType() == "Bom":
        return "BOMB"

def combat(attacker, defender, click, graveyard1, graveyard2, army1, army2):
    """ 
    Combat between two pieces. 
    :param attacker: Attacking piece
    :param defender: Defending piece
    :param click: Cursor click location (x, y)
    """

    if Gameboard.Gameboard.AI == AI_OFF:
        opponent = "PLAYER 2"
    else:
        opponent = "COMPUTER"
    sound = arcade.load_sound("Death.wav",False)
    defuse = arcade.load_sound("Defuse.wav", False)
    level = sound_settings.Sound.level
    
    output = ""
    
    # SPECIAL CASE: Miner vs. Bomb
    if attacker.getType() == "Min" and defender.getType() == "Bom": #HISS SFX
        if defender.getPlayer() == PLAYER_ONE:
            move_to_graveyard(army1, defender, graveyard1)
            arcade.play_sound(defuse, level+1, 0)
            output = f"{opponent}'S MINER DEFUSES PLAYER 1'S BOMB"
        else:
            move_to_graveyard(army2, defender, graveyard2)
            arcade.play_sound(defuse, level+1, 0)
            output = f"{opponent}'S MINER DEFUSES PLAYER 2'S BOMB"
        move_piece(attacker, click)

    # SPECIAL CASE: Non-miner attacks bomb
    elif defender.getType() == "Bom":
        if attacker.getPlayer() == PLAYER_ONE:
            move_to_graveyard(army1, attacker, graveyard1)
            arcade.play_sound(sound, level+1, 0)
            output = f"BOMB EXPLODES, PLAYER 1'S {convert_piece_type(attacker)} DEFEATED"
        else:
            move_to_graveyard(army2, attacker, graveyard2)
            arcade.play_sound(sound, level+1, 0)
            output = f"BOMB EXPLODES, {opponent}'S {convert_piece_type(attacker)} DEFEATED"

    # SPECIAL CASE: Spy is attacking Marshall
    elif attacker.getType() == "Spy" and defender.getType() == "Msh":
        # spy attacks msh, msh defeated
        if defender.getPlayer() == PLAYER_ONE:
            move_to_graveyard(army1, defender, graveyard1)
            arcade.play_sound(sound, level+1, 0)
            output = f"{opponent}'S SPY DEFEATS PLAYER 1'S MARSHALL"
        else:
            move_to_graveyard(army2, defender, graveyard2)
            arcade.play_sound(sound, level+1, 0)
            output =  f"PLAYER 1'S SPY DEFEATS {opponent}'S MARSHALL"
        move_piece(attacker, click) 

    elif attacker.getPower() > defender.getPower():
        # attacking piece wins and takes defending piece's place
        if defender.getPlayer() == PLAYER_ONE:
            move_to_graveyard(army1, defender, graveyard1)
            arcade.play_sound(sound, level+1, 0)
            output = f"{opponent}'S {convert_piece_type(attacker)} DEFEATS PLAYER 1'S {convert_piece_type(defender)}"
        else:
            move_to_graveyard(army2, defender, graveyard2)
            arcade.play_sound(sound, level+1, 0)
            output = f"PLAYER 1'S {convert_piece_type(attacker)} DEFEATS {opponent}'S {convert_piece_type(defender)}"
        move_piece(attacker, click)

    elif attacker.getPower() < defender.getPower():
        # defending piece wins
        if attacker.getPlayer() == PLAYER_ONE:
            move_to_graveyard(army1, attacker, graveyard1)
            arcade.play_sound(sound, level+1, 0)
            output = f"{opponent}'S {convert_piece_type(defender)} DEFEATS PLAYERS 1'S {convert_piece_type(attacker)}"
        else:
            move_to_graveyard(army2, attacker, graveyard2)
            arcade.play_sound(sound, level+1, 0)
            output = f"PLAYER 1'S {convert_piece_type(defender)} DEFEATS {opponent}'S {convert_piece_type(attacker)}"
    else:
        # attacker and defender have same power, both sent to graveyards
        if attacker.getPlayer() == PLAYER_ONE:
            move_to_graveyard(army1, attacker, graveyard1)
            move_to_graveyard(army2, defender, graveyard2)
            arcade.play_sound(sound, level+1, 0)
            time.sleep(.2)
            arcade.play_sound(sound, level+1, 0)
            output = f"{opponent}'S {convert_piece_type(defender)} DEFEATED. PLAYER 1'S {convert_piece_type(attacker)} DEFEATED"
        else:
            move_to_graveyard(army1, defender, graveyard1)
            move_to_graveyard(army2, attacker, graveyard2)
            arcade.play_sound(sound, level+1, 0)
            time.sleep(.2)
            arcade.play_sound(sound, level+1, 0)
            output = f"PLAYER 1'S {convert_piece_type(defender)} DEFEATED. {opponent}'S {convert_piece_type(attacker)} DEFEATED"
            
    return output