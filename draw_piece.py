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


def is_enemy(enemy_pieces, piece, click):
    x = click[0]
    y = click[1]
    hit_piece = None
    if is_piece(enemy_pieces, click):
        for enemy_piece in enemy_pieces:
            enemy_piecex = enemy_piece.getPosition()[0]
            enemy_piecey = enemy_piece.getPosition()[1]
            if x >= BOARD_LEFT + BOARD_MARGIN * enemy_piecex and x <= BOARD_RIGHT + BOARD_MARGIN * enemy_piecex and y <= BOARD_TOP + BOARD_MARGIN * enemy_piecey and y >= BOARD_BOTTOM + BOARD_MARGIN * enemy_piecey:
                hit_piece = enemy_piece
        if hit_piece != None and hit_piece.getPower() < piece.getPower():
            print("enemy piece captured")
            return True
        elif hit_piece != None and hit_piece.getPower() >= piece.getPower():
            print("not sure whats supposed to happen here so Im doing this temporarily")
            return False
        else:
            return False


def capture_enemy_piece(enemy_pieces, piece, click):
    x = click[0]
    y = click[1]
    hit_piece = None
    if is_piece(enemy_pieces, click):
        for enemy_piece in enemy_pieces:
            enemy_piecex = enemy_piece.getPosition()[0]
            enemy_piecey = enemy_piece.getPosition()[1]
            if x >= BOARD_LEFT + BOARD_MARGIN * enemy_piecex and x <= BOARD_RIGHT + BOARD_MARGIN * enemy_piecex and y <= BOARD_TOP + BOARD_MARGIN * enemy_piecey and y >= BOARD_BOTTOM + BOARD_MARGIN * enemy_piecey:
                hit_piece = enemy_piece
    print(hit_piece)
    enemy_pieces = enemy_pieces.remove(hit_piece)
    print(enemy_pieces)
    return enemy_pieces


# if given a piece and the location of a cursor click it will return true stating that you can select that piece.
def is_piece(pieces, click):
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
    x = click[0]
    y = click[1]
    piecex = piece.getPosition()[0]
    piecey = piece.getPosition()[1]
    if x >= BOARD_LEFT + BOARD_MARGIN * piecex and x <= BOARD_RIGHT + BOARD_MARGIN * piecex and y <= BOARD_TOP + BOARD_MARGIN * piecey and y >= BOARD_BOTTOM + BOARD_MARGIN * piecey:
        if piece.getType() == "Bom" or piece.getType() == "Flg":
            print("piece does not move please make another selection")
            return False
        else:
            # show_available_moves(piece)
            return True
    else:
        return False


def show_available_moves(piece, total_pieces):
    x = piece.getPosition()[0]
    y = piece.getPosition()[1]
    if piece.getType() != "Sct":
        if (is_piece(total_pieces, [BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_RIGHT + 25 + BOARD_MARGIN * x < 700):
            arcade.draw_arc_filled(BOARD_RIGHT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
        if (is_piece(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y]) == False and BOARD_TOP + 25 + BOARD_MARGIN * y < 600):
            arcade.draw_arc_filled(BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
        if (is_piece(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y]) == False and BOARD_BOTTOM - 25 + BOARD_MARGIN * y > 100):
            arcade.draw_arc_filled(BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
        if (is_piece(total_pieces, [BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_LEFT - 25 + BOARD_MARGIN * x > 200):
            arcade.draw_arc_filled(BOARD_LEFT - 25 + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
    if piece.getType() == "Sct":
        next_i = 1
        while (is_piece(total_pieces, [BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x < 700):
            arcade.draw_arc_filled(BOARD_RIGHT + 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_i = next_i + 2
        next_j = 1
        while (is_piece(total_pieces, [BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y]) == False and BOARD_TOP + 25 * next_j + BOARD_MARGIN * y < 600):
            arcade.draw_arc_filled(BOARD_RIGHT - 25 + BOARD_MARGIN * x, BOARD_TOP + 25 * next_j + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_j = next_j + 2
        next_j = 1
        while (is_piece(total_pieces, [BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y]) == False and BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y > 100):
            arcade.draw_arc_filled(BOARD_LEFT + 25 + BOARD_MARGIN * x, BOARD_BOTTOM - 25 * next_j + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_j = next_j + 2
        next_i = 1
        while (is_piece(total_pieces, [BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y]) == False and BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x > 200):
            arcade.draw_arc_filled(BOARD_LEFT - 25 * next_i + BOARD_MARGIN * x, BOARD_BOTTOM + 25 + BOARD_MARGIN * y, 10, 10,
                                   arcade.color.BLACK, 0, 360)
            next_i = next_i + 2


def is_move_available(pieces, piece, click):
    loc = select_coordinate(click)
    locx = loc[0]
    locy = loc[1]
    piece_loc = piece.getPosition()
    piece_loc_x = piece_loc[0]
    piece_loc_y = piece_loc[1]
    if is_piece(pieces, click):
        return False
    else:
        if piece.getType() == "Sct":
            if locx != piece_loc_x and locy != piece_loc_y:
                print("invalid please try again")
                return False
            else:
                x = (piece_loc_x * 50) + 225
                y = (piece_loc_y * 50) + 125
                # print("x " + str(x) + " y " + str(y))
                locx_tester = BOARD_LEFT + BOARD_MARGIN * locx
                # print(locx_tester)
                locy_tester = BOARD_BOTTOM + BOARD_MARGIN * locy
                # print("locx_tester " + str(locx_tester) + " locy_tester " + str(locy_tester))

                if x < locx_tester and locx != piece_loc_x:
                    # print("testing rightward movement")
                    x = (piece_loc_x * 50) + 225
                    y = (piece_loc_y * 50) + 125
                    while x < locx_tester:
                        x = x + 50
                        if is_piece(pieces, [x, y]) == False:
                            print("for right movement check x " + str(x) + " check y " + str(y))
                        else:
                            print("for right movement jump detected at " + str(x) + ", " + str(y))
                            return False
                elif x > locx_tester and locx != piece_loc_x:
                    # print("testing leftward movement")
                    locx_tester = BOARD_RIGHT + BOARD_MARGIN * locx
                    x = (piece_loc_x * 50) + 225
                    y = (piece_loc_y * 50) + 125
                    while x > locx_tester:
                        x = x - 50
                        if is_piece(pieces, [x, y]) == False:
                            print("for left movement check x " + str(x) + " check y " + str(y))
                        else:
                            print("for left movement jump detected at " + str(x) + ", " + str(y))
                            return False
                elif y < locy_tester and locy != piece_loc_y:
                    # print("testing upward movement")
                    x = (piece_loc_x * 50) + 225
                    y = (piece_loc_y * 50) + 125
                    while y < locy_tester:
                        y = y + 50
                        if is_piece(pieces, [x, y]) == False:
                            print("for up movement check x " + str(x) + " check y " + str(y))
                        else:
                            print("for up movement jump detected at " + str(x) + ", " + str(y))
                            return False

                elif y > locy_tester and locy != piece_loc_y:
                    # print("testing upward movement")
                    x = (piece_loc_x * 50) + 225
                    y = (piece_loc_y * 50) + 125
                    locy_tester = BOARD_TOP + BOARD_MARGIN * locy
                    while y > locy_tester:
                        y = y - 50
                        if is_piece(pieces, [x, y]) == False:
                            print("for up movement check x " + str(x) + " check y " + str(y))
                        else:
                            print("for up movement jump detected at " + str(x) + ", " + str(y))
                            return False

                return True
        else:
            if locx != piece_loc_x and locy != piece_loc_y:
                print("invalid please try again")
                return False
            if locx > piece_loc_x + 1:
                print("invalid please try again")
                return False
            if locx < piece_loc_x - 1:
                print("invalid please try again")
                return False
            if locy > piece_loc_y + 1:
                print("invalid please try again")
                return False
            if locy < piece_loc_y - 1:
                print("invalid please try again")
                return False
            else:
                return True

def select_coordinate(click):
    x = click[0]
    y = click[1]
    if y > 100 and y < 150 and x > 200 and x < 700:
        # print("move the y coordinate to 0")
        locy = 0
    elif y > 150 and y < 200 and x > 200 and x < 700:
        # print("move the y coordinate to 1")
        locy = 1
    elif y > 200 and y < 250 and x > 200 and x < 700:
        # print("move the y coordinate to 2")
        locy = 2
    elif y > 250 and y < 300 and x > 200 and x < 700:
        # print("move the y coordinate to 3")
        locy = 3
    elif y > 300 and y < 350 and x > 200 and x < 700:
        # print("move the y coordinate to 4")
        locy = 4
    elif y > 350 and y < 400 and x > 200 and x < 700:
        # print("move the y coordinate to 5")
        locy = 5
    elif y > 400 and y < 450 and x > 200 and x < 700:
        # print("move the y coordinate to 6")
        locy = 6
    elif y > 450 and y < 500 and x > 200 and x < 700:
        # print("move the y coordinate to 7")
        locy = 7
    elif y > 500 and y < 550 and x > 200 and x < 700:
        # print("move the y coordinate to 8")
        locy = 8
    elif y > 550 and y < 600 and x > 200 and x < 700:
        # print("move the y coordinate to 9")
        locy = 9
    else:
        locy = None

    if x > 200 and x < 250 and y > 100 and y < 600:
        # print("move x coordinate to 0")
        locx = 0
    elif x > 250 and x < 300 and y > 100 and y < 600:
        # print("move x coordinate to 1")
        locx = 1
    elif x > 300 and x < 350 and y > 100 and y < 600:
        # print("move x coordinate to 2")
        locx = 2
    elif x > 350 and x < 400 and y > 100 and y < 600:
        # print("move x coordinate to 3")
        locx = 3
    elif x > 400 and x < 450 and y > 100 and y < 600:
        # print("move x coordinate to 4")
        locx = 4
    elif x > 450 and x < 500 and y > 100 and y < 600:
        # print("move x coordinate to 5")
        locx = 5
    elif x > 500 and x < 550 and y > 100 and y < 600:
        # print("move x coordinate to 6")
        locx = 6
    elif x > 550 and x < 600 and y > 100 and y < 600:
        # print("move x coordinate to 7")
        locx = 7
    elif x > 600 and x < 650 and y > 100 and y < 600:
        # print("move x coordinate to 8")
        locx = 8
    elif x > 650 and x < 700 and y > 100 and y < 600:
        # print("move x coordinate to 9")
        locx = 9
    else:
        locx = None

    coordinate = [locx, locy]
    return coordinate
def select_move(piece, click):
    x = click[0]
    y = click[1]

    loc = select_coordinate(click)
    locx = loc[0]
    locy = loc[1]

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
