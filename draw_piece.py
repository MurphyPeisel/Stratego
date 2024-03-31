import arcade
from Piece import Piece
from constants import *

#Constants for Graveyards
GRAVEYARD_1_LEFT = 5
GRAVEYARD_1_RIGHT = 195
GRAVEYARD_2_LEFT = 705
GRAVEYARD_2_RIGHT = 895
GRAVEYARD_BOTTOM = 105
GRAVEYARD_TOP = 595
YARD_MARGIN = 50

#Function To Draw Pieces in Initial Graveyard Positions
def draw_start(piece, army, index):
    
    yard_left = 0
    
    #ARMY 1 on the Left, Army 2 on the right
    if army == 1:
        yard_left = GRAVEYARD_1_LEFT
    else:
        yard_left = GRAVEYARD_2_LEFT
    
    #4 Pieces per Row
    row = index // 4
    
    
    point_list = ((yard_left+YARD_MARGIN*(index - 4*row),GRAVEYARD_TOP - YARD_MARGIN*row), 
                  (yard_left+YARD_MARGIN*(index - 4*row), (GRAVEYARD_TOP- YARD_MARGIN*row) - 40),
                  (yard_left+(YARD_MARGIN * (index-4*row)) + 40, (GRAVEYARD_TOP - YARD_MARGIN*row)-40),
                  (yard_left+(YARD_MARGIN * (index-4*row)) + 40, GRAVEYARD_TOP - YARD_MARGIN*row))
    if piece.getType() == "Flg":
        arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
    elif piece.getType() == "Msh":
        arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
    elif piece.getType() == "Gen":
        arcade.draw_polygon_filled(point_list, arcade.color.VIOLET)
    if piece.getType() == "Col":
        arcade.draw_polygon_filled(point_list, arcade.color.PINK)
    if piece.getType() == "Maj":
        arcade.draw_polygon_filled(point_list, arcade.color.YELLOW)
    if piece.getType() == "Cap":
        arcade.draw_polygon_filled(point_list, arcade.color.MAGENTA)
    if piece.getType() == "Ltn":
        arcade.draw_polygon_filled(point_list, arcade.color.TANGERINE)
    if piece.getType() == "Sgt":
        arcade.draw_polygon_filled(point_list, arcade.color.BABY_BLUE)
    if piece.getType() == "Min":
        arcade.draw_polygon_filled(point_list, arcade.color.RASPBERRY)
    elif piece.getType() == "Sct":
        arcade.draw_polygon_filled(point_list, arcade.color.BLUE)
    elif piece.getType() == "Spy":
        arcade.draw_polygon_filled(point_list, arcade.color.BLACK)
    elif piece.getType() == "Bom":
        arcade.draw_polygon_filled(point_list, arcade.color.RED)

    if piece.getType() == "Lke":
        arcade.draw_polygon_filled(point_list, arcade.color.BLACK)



def draw(piece):
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    point_list = ((BOARD_LEFT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y),
                    (BOARD_LEFT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                    (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                    (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y))
    if piece.getType() == "Flg":
        arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
    elif piece.getType() == "Msh":
        arcade.draw_polygon_filled(point_list, arcade.color.BROWN)
    elif piece.getType() == "Gen":
        arcade.draw_polygon_filled(point_list, arcade.color.VIOLET)
    if piece.getType() == "Col":
        arcade.draw_polygon_filled(point_list, arcade.color.PINK)
    if piece.getType() == "Maj":
        arcade.draw_polygon_filled(point_list, arcade.color.YELLOW)
    if piece.getType() == "Cap":
        arcade.draw_polygon_filled(point_list, arcade.color.MAGENTA)
    if piece.getType() == "Ltn":
        arcade.draw_polygon_filled(point_list, arcade.color.TANGERINE)
    if piece.getType() == "Sgt":
        arcade.draw_polygon_filled(point_list, arcade.color.BABY_BLUE)
    if piece.getType() == "Min":
        arcade.draw_polygon_filled(point_list, arcade.color.RASPBERRY)
    elif piece.getType() == "Sct":
        arcade.draw_polygon_filled(point_list, arcade.color.BLUE)
    elif piece.getType() == "Spy":
        arcade.draw_polygon_filled(point_list, arcade.color.BLACK)
    elif piece.getType() == "Bom":
        arcade.draw_polygon_filled(point_list, arcade.color.RED)


# def is_enemy(enemy_pieces, piece, click):
#     x = click[0]
#     y = click[1]
#     hit_piece = None
#     if is_piece(enemy_pieces, click):
#         for enemy_piece in enemy_pieces:
#             enemy_piecex = enemy_piece.getPosition()[0]
#             enemy_piecey = enemy_piece.getPosition()[1]
#             if x >= BOARD_LEFT + BOARD_MARGIN * enemy_piecex and x <= BOARD_RIGHT + BOARD_MARGIN * enemy_piecex and y <= BOARD_TOP + BOARD_MARGIN * enemy_piecey and y >= BOARD_BOTTOM + BOARD_MARGIN * enemy_piecey:
#                 hit_piece = enemy_piece
#         if hit_piece != None and hit_piece.getPower() < piece.getPower():
#             print("enemy piece captured")
#             return True
#         elif hit_piece != None and hit_piece.getPower() >= piece.getPower():
#             print("not sure whats supposed to happen here so Im doing this temporarily")
#             return False
#         else:
#             return False


# def capture_enemy_piece(enemy_pieces, piece, click):
#     x = click[0]
#     y = click[1]
#     hit_piece = None
#     if is_piece(enemy_pieces, click):
#         for enemy_piece in enemy_pieces:
#             enemy_piecex = enemy_piece.getPosition()[0]
#             enemy_piecey = enemy_piece.getPosition()[1]
#             if x >= BOARD_LEFT + BOARD_MARGIN * enemy_piecex and x <= BOARD_RIGHT + BOARD_MARGIN * enemy_piecex and y <= BOARD_TOP + BOARD_MARGIN * enemy_piecey and y >= BOARD_BOTTOM + BOARD_MARGIN * enemy_piecey:
#                 hit_piece = enemy_piece
#     print(hit_piece)
#     enemy_pieces = enemy_pieces.remove(hit_piece)
#     print(enemy_pieces)
#     return enemy_pieces


# if given a piece and the location of a cursor click it will return true stating that you can select that piece.
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
def is_piece_scan(pieces, click):
    x = click[0]
    y = click[1]
    # print("checking for piece at " + str(x) + str(y))
    for piece in pieces:
        piecex = piece.getPosition()[0]
        piecey = piece.getPosition()[1]
        if x>=BOARD_LEFT + BOARD_MARGIN*piecex and x<=BOARD_RIGHT + BOARD_MARGIN*piecex and y<= BOARD_TOP + BOARD_MARGIN*piecey and y>= BOARD_BOTTOM + BOARD_MARGIN*piecey:
            return True
    return False

def select_piece(piece, click):
    x, y = click
    piece_x, piece_y = piece.getPosition()
    if (x >= BOARD_LEFT + BOARD_MARGIN * piece_x and 
        x <= BOARD_RIGHT + BOARD_MARGIN * piece_x and
        y <= BOARD_TOP + BOARD_MARGIN * piece_y and 
        y >= BOARD_BOTTOM + BOARD_MARGIN * piece_y):
        if piece.getType() == "Bom" or piece.getType() == "Flg" or piece.getType() == "Lke":
            print(f"{piece.getType()} is not selectable. Select another piece.")
            return False
        else:
            #show_available_moves(piece, total_pieces)
            return True
    else:
        return False


def show_available_moves(piece, total_pieces):
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    if piece.getType() != "Sct":
        if (is_piece_scan(total_pieces, [BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_RIGHT + 25 + BOARD_MARGIN * x < 700):
            arcade.draw_arc_filled(BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
        if (is_piece_scan(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y]) == False and BOARD_TOP + 25 + BOARD_MARGIN * y < 600):
            arcade.draw_arc_filled(BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
        if (is_piece_scan(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y]) == False and BOARD_BOTTOM - 25 + BOARD_MARGIN * y > 100):
            arcade.draw_arc_filled(BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
        if (is_piece_scan(total_pieces, [BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_LEFT - 25 + BOARD_MARGIN * x > 200):
            arcade.draw_arc_filled(BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
    if piece.getType() == "Sct":
        next_i = 1
        while (is_piece_scan(total_pieces, [BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x < 700):
            arcade.draw_arc_filled(BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_i = next_i + 2
        next_j = 1
        while (is_piece_scan(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y]) == False and BOARD_TOP + 25 * next_j + BOARD_MARGIN * y < 600):
            arcade.draw_arc_filled(BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_j = next_j + 2
        next_j = 1
        while (is_piece_scan(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y]) == False and BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y > 100):
            arcade.draw_arc_filled(BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_j = next_j + 2
        next_i = 1
        while (is_piece_scan(total_pieces, [BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x > 200):
            arcade.draw_arc_filled(BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_i = next_i + 2

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
                    x = (piece_loc_x * 50) + 225
                    y = (piece_loc_y * 50) + 125
                    # print("x " + str(x) + " y " + str(y))
                    locx_tester = BOARD_LEFT + BOARD_MARGIN * loc_x
                    # print(locx_tester)
                    locy_tester = BOARD_BOTTOM + BOARD_MARGIN * loc_y
                    # print("locx_tester " + str(locx_tester) + " locy_tester " + str(locy_tester))

                    if x < locx_tester and loc_x != piece_loc_x:
                        # print("testing rightward movement")
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        while x < locx_tester:
                            x = x + 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                print("for right movement check x " + str(x) + " check y " + str(y))
                            else:
                                print("for right movement jump detected at " + str(x) + ", " + str(y))
                                return (False, None)
                    elif x > locx_tester and loc_x != piece_loc_x:
                        # print("testing leftward movement")
                        locx_tester = BOARD_RIGHT + BOARD_MARGIN * loc_x
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        while x > locx_tester:
                            x = x - 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                print("for left movement check x " + str(x) + " check y " + str(y))
                            else:
                                print("for left movement jump detected at " + str(x) + ", " + str(y))
                                return (False, None)
                    elif y < locy_tester and loc_y != piece_loc_y:
                        # print("testing upward movement")
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        while y < locy_tester:
                            y = y + 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                print("for up movement check x " + str(x) + " check y " + str(y))
                            else:
                                print("for up movement jump detected at " + str(x) + ", " + str(y))
                                return (False, None)

                    elif y > locy_tester and loc_y != piece_loc_y:
                        # print("testing upward movement")
                        x = (piece_loc_x * 50) + 225
                        y = (piece_loc_y * 50) + 125
                        locy_tester = BOARD_TOP + BOARD_MARGIN * loc_y
                        while y > locy_tester:
                            y = y - 50
                            if is_piece_scan(pieces, [x, y]) == False:
                                print("for up movement check x " + str(x) + " check y " + str(y))
                            else:
                                print("for up movement jump detected at " + str(x) + ", " + str(y))
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
# def is_move_available(pieces, piece, click):
#     """ 
#     Checks if a piece's move is valid.
#     :param pieces: List of all pieces
#     :param piece: Selected piece
#     :param click: Cursor click location (x, y)
#     :return: Tuple containing bool of if the move is available and the piece at that location if so 
#     :rtype: (bool, Piece)
#     """
#     try:
#         locx, locy = get_coordinates(click)
#     except TypeError:
#         print("Invalid move. Cannot convert out-of-bound click to x,y coordinates.")
#         return (False, None)
#     else:
#         piece_loc_x, piece_loc_y = piece.getPosition()
#         if piece.getType() == "Sct":
#             if locx != piece_loc_x and locy != piece_loc_y:
#                 print("invalid please try again")
#                 return False
#             else:
#                 x = (piece_loc_x * 50) + 225
#                 y = (piece_loc_y * 50) + 125
#                 # print("x " + str(x) + " y " + str(y))
#                 locx_tester = BOARD_LEFT + BOARD_MARGIN * locx
#                 # print(locx_tester)
#                 locy_tester = BOARD_BOTTOM + BOARD_MARGIN * locy
#                 # print("locx_tester " + str(locx_tester) + " locy_tester " + str(locy_tester))

#                 if x < locx_tester and locx != piece_loc_x:
#                     # print("testing rightward movement")
#                     x = (piece_loc_x * 50) + 225
#                     y = (piece_loc_y * 50) + 125
#                     while x < locx_tester:
#                         x = x + 50
#                         if is_piece(pieces, [x, y]) == False:
#                             print("for right movement check x " + str(x) + " check y " + str(y))
#                         else:
#                             print("for right movement jump detected at " + str(x) + ", " + str(y))
#                             return False
#                 elif x > locx_tester and locx != piece_loc_x:
#                     # print("testing leftward movement")
#                     locx_tester = BOARD_RIGHT + BOARD_MARGIN * locx
#                     x = (piece_loc_x * 50) + 225
#                     y = (piece_loc_y * 50) + 125
#                     while x > locx_tester:
#                         x = x - 50
#                         if is_piece(pieces, [x, y]) == False:
#                             print("for left movement check x " + str(x) + " check y " + str(y))
#                         else:
#                             print("for left movement jump detected at " + str(x) + ", " + str(y))
#                             return False
#                 elif y < locy_tester and locy != piece_loc_y:
#                     # print("testing upward movement")
#                     x = (piece_loc_x * 50) + 225
#                     y = (piece_loc_y * 50) + 125
#                     while y < locy_tester:
#                         y = y + 50
#                         if is_piece(pieces, [x, y]) == False:
#                             print("for up movement check x " + str(x) + " check y " + str(y))
#                         else:
#                             print("for up movement jump detected at " + str(x) + ", " + str(y))
#                             return False

#                 elif y > locy_tester and locy != piece_loc_y:
#                     # print("testing upward movement")
#                     x = (piece_loc_x * 50) + 225
#                     y = (piece_loc_y * 50) + 125
#                     locy_tester = BOARD_TOP + BOARD_MARGIN * locy
#                     while y > locy_tester:
#                         y = y - 50
#                         if is_piece(pieces, [x, y]) == False:
#                             print("for up movement check x " + str(x) + " check y " + str(y))
#                         else:
#                             print("for up movement jump detected at " + str(x) + ", " + str(y))
#                             return False

#                 return True
#         else:
#             if locx != piece_loc_x and locy != piece_loc_y:
#                 print("invalid please try again")
#                 return False
#             if locx > piece_loc_x + 1:
#                 print("invalid please try again")
#                 return False
#             if locx < piece_loc_x - 1:
#                 print("invalid please try again")
#                 return False
#             if locy > piece_loc_y + 1:
#                 print("invalid please try again")
#                 return False
#             if locy < piece_loc_y - 1:
#                 print("invalid please try again")
#                 return False
#             else:
#                 return True

# def select_coordinate(click):
#     x = click[0]
#     y = click[1]
#     if y > 100 and y < 150 and x > 200 and x < 700:
#         # print("move the y coordinate to 0")
#         locy = 0
#     elif y > 150 and y < 200 and x > 200 and x < 700:
#         # print("move the y coordinate to 1")
#         locy = 1
#     elif y > 200 and y < 250 and x > 200 and x < 700:
#         # print("move the y coordinate to 2")
#         locy = 2
#     elif y > 250 and y < 300 and x > 200 and x < 700:
#         # print("move the y coordinate to 3")
#         locy = 3
#     elif y > 300 and y < 350 and x > 200 and x < 700:
#         # print("move the y coordinate to 4")
#         locy = 4
#     elif y > 350 and y < 400 and x > 200 and x < 700:
#         # print("move the y coordinate to 5")
#         locy = 5
#     elif y > 400 and y < 450 and x > 200 and x < 700:
#         # print("move the y coordinate to 6")
#         locy = 6
#     elif y > 450 and y < 500 and x > 200 and x < 700:
#         # print("move the y coordinate to 7")
#         locy = 7
#     elif y > 500 and y < 550 and x > 200 and x < 700:
#         # print("move the y coordinate to 8")
#         locy = 8
#     elif y > 550 and y < 600 and x > 200 and x < 700:
#         # print("move the y coordinate to 9")
#         locy = 9
#     else:
#         locy = None

#     if x > 200 and x < 250 and y > 100 and y < 600:
#         # print("move x coordinate to 0")
#         locx = 0
#     elif x > 250 and x < 300 and y > 100 and y < 600:
#         # print("move x coordinate to 1")
#         locx = 1
#     elif x > 300 and x < 350 and y > 100 and y < 600:
#         # print("move x coordinate to 2")
#         locx = 2
#     elif x > 350 and x < 400 and y > 100 and y < 600:
#         # print("move x coordinate to 3")
#         locx = 3
#     elif x > 400 and x < 450 and y > 100 and y < 600:
#         # print("move x coordinate to 4")
#         locx = 4
#     elif x > 450 and x < 500 and y > 100 and y < 600:
#         # print("move x coordinate to 5")
#         locx = 5
#     elif x > 500 and x < 550 and y > 100 and y < 600:
#         # print("move x coordinate to 6")
#         locx = 6
#     elif x > 550 and x < 600 and y > 100 and y < 600:
#         # print("move x coordinate to 7")
#         locx = 7
#     elif x > 600 and x < 650 and y > 100 and y < 600:
#         # print("move x coordinate to 8")
#         locx = 8
#     elif x > 650 and x < 700 and y > 100 and y < 600:
#         # print("move x coordinate to 9")
#         locx = 9
#     else:
#         locx = None

#     coordinate = [locx, locy]
#     return coordinate

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
def select_move(piece, click):
    x = click[0]
    y = click[1]

    loc = get_coordinates(click)
    locx = loc[0]
    locy = loc[1]

    if locx != None and locy != None:
        return move_piece(piece, locx, locy)
    else:
        return None
def move_to_graveyard(army,piece, graveyard):
    piece.setPosition(-1,-1)
    army.remove(piece)
    graveyard.append(piece)
    print(graveyard[0])
    

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

def combat(attacker, defender, click, graveyard1, graveyard2, army1, army2):
    """ 
    Combat between two pieces. If the attacking piece 
    :param attacker: Attacking piece
    :param defender: Defending piece
    :param click: Cursor click location (x, y)
    """
    if attacker.getType() == "Lke" or defender.getType() == "Lke":
        return "lake!"
    print("COMBAT")
    print(f"attacker located at {attacker.getPosition()}, type: {attacker.getType()}, power: {attacker.getPower()}")
    print(f"defender located at {defender.getPosition()}, type: {defender.getType()}, power: {defender.getPower()}")
    if attacker.getPower() > defender.getPower():
        print("attacker wins")
        defender.defeated = True
        defender.setPosition(-1,-1)
        if defender.getPlayer() == 1:
            move_to_graveyard(army1, defender, graveyard1)
        else:
            move_to_graveyard(army2, defender, graveyard2)


        move_piece(attacker, click)
    elif attacker.getPower() < defender.getPower():
        print("defender wins")
        attacker.defeated = True
        move_piece(defender, click)
        if attacker.getPlayer() == 1:
            move_to_graveyard(army1, attacker, graveyard1)
        else:
            move_to_graveyard(army2, attacker, graveyard2)
    else:
        print("attacker and defender defeated")
        attacker.defeated = True
        defender.defeated = True
        if attacker.getPlayer() == 1:
            move_to_graveyard(army1, attacker, graveyard1)
        else:
            move_to_graveyard(army2, attacker, graveyard2)
        if defender.getPlayer() == 1:
            move_to_graveyard(army1, defender, graveyard1)
        else:
            move_to_graveyard(army2, defender, graveyard2)

