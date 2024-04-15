import Piece
from draw_piece import is_piece_scan
import random


def place_piece(piece, position, graveyard, army):
    army.append(piece)
    graveyard.remove(piece)
    piece.setPosition(position[0], position[1])

def gen_layout(difficulty, graveyard, army):
    # enemy is always on top of board
    # their grid cells are: (0,9) -- (9, 6)

    if difficulty == 0:
        pass


    
    # Easy
    # Randomly place pieces
    elif difficulty == 1:
        random.shuffle(graveyard)
        copy = [i for i in graveyard]
        # top left coordinates of board
        pos_x = 0
        pos_y = 9
        i = 0
        for piece in copy:
            if piece.getType() != "Lke":
                # update position, left to right
                place_piece(piece, (pos_x, pos_y), graveyard, army)
                pos_x = pos_x + 1
                if pos_x == 10:
                    pos_x = pos_x % 10
                    pos_y = pos_y - 1
    else:
        print(f"ERROR: {difficulty} is not a valid difficulty.")