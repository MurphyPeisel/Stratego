import Piece
from draw_piece import is_piece_scan
import random


def place_piece(piece, position, graveyard, army):
    print(f"{piece.getType()} placed at {position}")
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

    # # Medium
    # # Flag placed randomly in back two rows
    # # place bombs near flag
    # elif difficulty == 2:
    #    # sort array in the following order
    #     piece_order = {"Flg": 0, "Bom": 1, "Sct": 2, "Min": 3, 
    #                    "Msh": 4, "Gen": 5,  "Col": 6, "Maj": 7, 
    #                    "Cap": 8, "Ltn": 9, "Sgt": 10,  "Spy": 11,
    #                    "Lke": 12}
    #     graveyard.sort(key = lambda piece: piece_order[piece.getType()])
    #     copy = [i for i in graveyard]
    #     for piece in copy:
    #         match piece.getType():
    #             case "Flg":
    #                 # place flag on random column in back 2 rows
    #                 flag_x = random.randint(0, 9)
    #                 flag_y = random.randint(8, 9)
    #                 place_piece(piece, (flag_x, flag_y), graveyard, army)

    #             case "Bom":
    #                 # place bombs orthogonal to flag
    #                 if flag_x + 1 <= 9 and not is_piece_scan(graveyard, (flag_x + 1, flag_y)):
    #                     place_piece(piece, (flag_x + 1, flag_y), graveyard, army) # one cell right of the flag
    #                 elif flag_x - 1 >= 0 and not is_piece_scan(graveyard, (flag_x + 1, flag_y)):
    #                     place_piece(piece, (flag_x - 1, flag_y), graveyard, army) # one cell left of the flag
    #                 elif not is_piece_scan(graveyard, (flag_x, flag_y - 1)):
    #                     place_piece(piece, (flag_x, flag_y - 1), graveyard, army) # one cell below the flag
    #                 elif flag_y + 1 <= 9 and not is_piece_scan(graveyard, (flag_x, flag_y - 1)):
    #                     place_piece(piece, (flag_x, flag_y + 1), graveyard, army) # one cell above the flag
    #                 else:  
    #                 # randomly place other bombs
    #                     bomb_x = random.randint(0, 9)
    #                     bomb_y = random.randint(6, 9)
    #                     i = 0
    #                     while is_piece_scan(graveyard, (bomb_x, bomb_y)):
    #                         print(f"i: {i}")
    #                         i += 1
    #                         bomb_x = random.randint(0, 9)
    #                         bomb_y = random.randint(6, 9)
    #                     place_piece(piece, (bomb_x, bomb_y), graveyard, army)
    #             case "Lke":
    #                 pass
    #             case _:
    #                 # randomly place all other pieces
    #                 piece_x = random.randint(0, 9)
    #                 piece_y = random.randint(6, 9)
    #                 while is_piece_scan(graveyard, (piece_x, piece_y)):
    #                     piece_x = random.randint(0, 9)
    #                     piece_y = random.randint(6, 9)
    #                     print(f"({piece_x}, {piece_y})")
    #                 place_piece(piece, (piece_x, piece_y), graveyard, army)

    # # Hard
    # # Flag in bottom row surrounded by bombs
    # # Randomly place other pieces, scouts / miners towards front 
    # elif difficulty == 3:
    #     # sort array in the following order
    #     piece_order = {"Flg": 0, "Bom": 1, "Sct": 2, "Min": 3, 
    #                    "Msh": 4, "Gen": 5,  "Col": 6, "Maj": 7, 
    #                    "Cap": 8, "Ltn": 9, "Sgt": 10,  "Spy": 11,
    #                    "Lke": 12}
        
    #     graveyard.sort(key = lambda piece: piece_order[piece.getType()])
    #     copy = [i for i in graveyard]
    #     for piece in copy:
    #         match piece.getType():
    #             case "Flg":
    #                 # place flag on random column in back row
    #                 flag_x = random.randint(0, 9)
    #                 flag_y = 9
    #                 piece.setPosition(flag_x, flag_y)
    #             case "Bom":
    #                 # place bombs orthogonal to flag
    #                 if flag_x + 1 <= 9 and not is_piece_scan(graveyard, (flag_x + 1, flag_y)):
    #                     piece.setPosition(flag_x + 1, flag_y) # one cell right of the flag
    #                 elif flag_x - 1 >= 0 and not is_piece_scan(graveyard, (flag_x + 1, flag_y)):
    #                     piece.setPosition(flag_x - 1, flag_y) # one cell left of flag
    #                 elif not is_piece_scan(graveyard, (flag_x, flag_y - 1)):
    #                     piece.setPosition(flag_x, flag_y - 1) # one cell below flag
    #                 # randomly place other bombs
    #                 else: 
    #                     bomb_x = random.randint(0, 9)
    #                     bomb_y = random.randint(6, 9)
    #                     while not is_piece_scan(graveyard, (bomb_x, bomb_y)):
    #                         bomb_x = random.randint(0, 9)
    #                         bomb_y = random.randint(6, 9)
    #                     piece.setPosition(bomb_x, bomb_y)
    #             case "Sct":
    #                 # place scout in front 2 rows 
    #                 scout_x = random.randint(0, 9)
    #                 scout_y = random.randint(6, 7)
    #                 while not is_piece_scan(graveyard, (scout_x, scout_y)):
    #                     scout_x = random.randint(0, 9)
    #                     scout_y = random.randint(6, 7)
    #                 piece.setPosition(scout_x, scout_y)
    #             case "Min":
    #                 # place miner in front 3 rows
    #                 miner_x = random.randint(0, 9)
    #                 miner_y = random.randint(6, 8)
    #                 while not is_piece_scan(graveyard, (scout_x, scout_y)):
    #                     miner_x = random.randint(0, 9)
    #                     miner_y = random.randint(6, 8)
    #                 piece.setPosition(miner_x, miner_y)
    #             case "Lke":
    #                 pass
    #             case _:
    #                 # randomly place all other pieces
    #                 piece_x = random.randint(0, 9)
    #                 piece_y = random.randint(6, 9)
    #                 while not is_piece_scan(graveyard, (piece_x, piece_y)):
    #                     piece_x = random.randint(0, 9)
    #                     piece_y = random.randint(6, 9)
    #                 piece.setPosition(piece_x, piece_y)                        

    else:
        print(f"ERROR: {difficulty} is not a valid difficulty.")