import Piece
from draw_piece import is_piece_scan
import random

# def quicksort(arr):


# def test_sort():


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
                pos_y = pos_y + 1

    # Medium
    # Well-rounded, more defensive than offensive
    # Bombs placed randomly
    elif difficulty == 2:
        pass
    # Hard
    # Flag in bottom row surrounded by bombs
    # Decoy flag post (bombs in corner)
    # Aggressive set-up
    elif difficulty == 3:
        # sort array in the following order
        piece_order = {"Flg": 0, "Bom": 1, "Msh": 2, "Gen": 3, 
                       "Col": 4, "Maj": 5, "Cap": 6, "Ltn": 7, 
                       "Sgt": 8, "Min": 9, "Sct": 10, "Spy": 11}
        
        pieces.sort(key=piece_order)

        for piece in pieces:
            match piece.getType():
                case "Flg":
                    # place flag on random column in back row
                    flag_x = random.randint(0,9)
                    flag_y = 9
                    piece.setPosition(flag_x, flag_y)
                case "Bom":
                    # place bombs orthogonal to flag
                    bomb_x = flag_x
                    bomb_y = flag_y
                    # while cell is empty
                    while not is_piece_scan(pieces, (bomb_x, bomb_y)):
                        
                        

                    # if flag is already surrounded, place bombs randomly in columns that already have a bomb
                    # cases: (+1, +1), (-1, -1), (+1, -1), (-1, +1)
                    pass
                case "Msh":
                    pass
                case "Gen":
                    pass
                case "Col":
                    pass
                case "Maj":
                    pass
                case "Cap":
                    pass
                case "Ltn":
                    pass
                case "Sgt":
                    pass
                case "Min":
                    pass
                case "Sct":
                    pass
                case "Spy":
                    pass
                case _:
                    raise Exception("Invalid piece ")
                    

            
    else:
        print(f"ERROR: {difficulty} is not a valid difficulty.")