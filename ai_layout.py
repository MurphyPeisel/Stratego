import Piece
from draw_piece import is_piece_scan
import random

def gen_layout(pieces, difficulty):
    # enemy is always on top of board
    # their grid cells are: (0,9) -- (9, 6)

    # Easy
    # Randomly place pieces
    if difficulty == 1:
        random.shuffle(pieces)
        # top left coordinates of board
        pos_x = 0
        pos_y = 9
        for piece in pieces:
            # update position, left to right
            piece.setPosition(pos_x, pos_y)
            pos_x = pos_x + 1
            if pos_x == 10:
                pos_x = pos_x % 10
                pos_y = pos_y - 1

    # Medium
    # Flag placed randomly in back two rows
    # place bombs near flag
    elif difficulty == 2:
       # sort array in the following order
        piece_order = {"Flg": 0, "Bom": 1, "Sct": 2, "Min": 3, 
                       "Msh": 4, "Gen": 5,  "Col": 6, "Maj": 7, 
                       "Cap": 8, "Ltn": 9, "Sgt": 10,  "Spy": 11}
        
        pieces.sort(key = lambda piece: piece_order[piece.getType()])
        for piece in pieces:
            match piece.getType():
                case "Flg":
                    # place flag on random column in back 2 rows
                    flag_x = random.randint(0, 9)
                    flag_y = random.randint(8, 9)
                    piece.setPosition(flag_x, flag_y)
                case "Bom":
                    # place bombs orthogonal to flag
                    if flag_x + 1 <= 9 and not is_piece_scan(pieces, (flag_x + 1, flag_y)):
                        piece.setPosition(flag_x + 1, flag_y) # one cell right of the flag
                    elif flag_x - 1 >= 0 and not is_piece_scan(pieces, (flag_x + 1, flag_y)):
                        piece.setPosition(flag_x - 1, flag_y) # one cell left of flag
                    elif not is_piece_scan(pieces, (flag_x, flag_y - 1)):
                        piece.setPosition(flag_x, flag_y - 1) # one cell below flag
                    elif flag_y + 1 <= 9 and not is_piece_scan(pieces, (flag_x, flag_y - 1)):
                        piece.setPosition(flag_x, flag_y + 1) # one cell above flag
                    else:  
                    # randomly place other bombs
                        bomb_x = random.randint(0, 9)
                        bomb_y = random.randint(6, 9)
                        while not is_piece_scan(pieces, (bomb_x, bomb_y)):
                            bomb_x = random.randint(0, 9)
                            bomb_y = random.randint(6, 9)
                        piece.setPosition(bomb_x, bomb_y)
                case _:
                    # randomly place all other pieces
                    piece_x = random.randint(0, 9)
                    piece_y = random.randint(6, 9)
                    while not is_piece_scan(pieces, (piece_x, piece_y)):
                        piece_x = random.randint(0, 9)
                        piece_y = random.randint(6, 9)
                    piece.setPosition(piece_x, piece_y)                        
    
    # Hard
    # Flag in bottom row surrounded by bombs
    # Randomly place other pieces, scouts / miners towards front 
    elif difficulty == 3:
        # sort array in the following order
        piece_order = {"Flg": 0, "Bom": 1, "Sct": 2, "Min": 3, 
                       "Msh": 4, "Gen": 5,  "Col": 6, "Maj": 7, 
                       "Cap": 8, "Ltn": 9, "Sgt": 10,  "Spy": 11}
        
        pieces.sort(key = lambda piece: piece_order[piece.getType()])
        for piece in pieces:
            match piece.getType():
                case "Flg":
                    # place flag on random column in back row
                    flag_x = random.randint(0, 9)
                    flag_y = 9
                    piece.setPosition(flag_x, flag_y)
                case "Bom":
                    # place bombs orthogonal to flag
                    if flag_x + 1 <= 9 and not is_piece_scan(pieces, (flag_x + 1, flag_y)):
                        piece.setPosition(flag_x + 1, flag_y) # one cell right of the flag
                    elif flag_x - 1 >= 0 and not is_piece_scan(pieces, (flag_x + 1, flag_y)):
                        piece.setPosition(flag_x - 1, flag_y) # one cell left of flag
                    elif not is_piece_scan(pieces, (flag_x, flag_y - 1)):
                        piece.setPosition(flag_x, flag_y - 1) # one cell below flag
                    # randomly place other bombs
                    else: 
                        bomb_x = random.randint(0, 9)
                        bomb_y = random.randint(6, 9)
                        while not is_piece_scan(pieces, (bomb_x, bomb_y)):
                            bomb_x = random.randint(0, 9)
                            bomb_y = random.randint(6, 9)
                        piece.setPosition(bomb_x, bomb_y)
                case "Sct":
                    # place scout in front 2 rows 
                    scout_x = random.randint(0, 9)
                    scout_y = random.randint(6, 7)
                    while not is_piece_scan(pieces, (scout_x, scout_y)):
                        scout_x = random.randint(0, 9)
                        scout_y = random.randint(6, 7)
                    piece.setPosition(scout_x, scout_y)
                case "Min":
                    # place miner in front 3 rows
                    miner_x = random.randint(0, 9)
                    miner_y = random.randint(6, 8)
                    while not is_piece_scan(pieces, (scout_x, scout_y)):
                        miner_x = random.randint(0, 9)
                        miner_y = random.randint(6, 8)
                    piece.setPosition(miner_x, miner_y)
                case _:
                    # randomly place all other pieces
                    piece_x = random.randint(0, 9)
                    piece_y = random.randint(6, 9)
                    while not is_piece_scan(pieces, (piece_x, piece_y)):
                        piece_x = random.randint(0, 9)
                        piece_y = random.randint(6, 9)
                    piece.setPosition(piece_x, piece_y)                        

    else:
        print(f"ERROR: {difficulty} is not a valid difficulty.")