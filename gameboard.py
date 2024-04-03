import arcade
import esc_menu
import pass_turn
import Piece
import draw_piece
import win
from constants import *

p1_tester_piece1 = Piece.Piece("Min", 3, 0, 0, 1)
p1_tester_piece2 = Piece.Piece("Msh", 10, 2, 0, 1)
p1_tester_piece3 = Piece.Piece("Gen", 9, 4, 0, 1)
p1_tester_piece4 = Piece.Piece("Bom", 12, 6, 0, 1)
p1_tester_piece5 = Piece.Piece("Flg", 0, 8, 0, 1)

p2_tester_piece1 = Piece.Piece("Sct", 2, 0, 9, 2)
p2_tester_piece2 = Piece.Piece("Msh", 10, 2, 9, 2)
p2_tester_piece3 = Piece.Piece("Gen", 9, 4, 9, 3)
p2_tester_piece4 = Piece.Piece("Bom", 12, 6, 9, 2)
p2_tester_piece5 = Piece.Piece("Flg", 0, 8, 9, 2)

lake_piece_1 = Piece.Piece("Lke", 0, 2, 4, 3)
lake_piece_2 = Piece.Piece("Lke", 0, 3, 4, 3)
lake_piece_3 = Piece.Piece("Lke", 0, 2, 5, 3)
lake_piece_4 = Piece.Piece("Lke", 0, 3, 5, 3)

lake_piece_5 = Piece.Piece("Lke", 0, 6, 4, 3)
lake_piece_6 = Piece.Piece("Lke", 0, 7, 4, 3)
lake_piece_7 = Piece.Piece("Lke", 0, 6, 5, 3)
lake_piece_8 = Piece.Piece("Lke", 0, 7, 5, 3)

p1_pieces = [p1_tester_piece1, p1_tester_piece2, p1_tester_piece3, p1_tester_piece4, p1_tester_piece5, lake_piece_1, lake_piece_2, lake_piece_3, lake_piece_4, lake_piece_5, lake_piece_6, lake_piece_7, lake_piece_8]
p2_pieces = [p2_tester_piece1, p2_tester_piece2, p2_tester_piece3, p2_tester_piece4, p2_tester_piece5, lake_piece_1, lake_piece_2, lake_piece_3, lake_piece_4, lake_piece_5, lake_piece_6, lake_piece_7, lake_piece_8]
total_pieces = p1_pieces + p2_pieces


# graveyard1 = Piece.initPieces(1)
# graveyard2 = Piece.initPieces(2)

graveyard1 = []
graveyard2 = []

army1 = []
army2 = []

# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    last_screen = "game_board"

    player_turn = 1

    click_counter = 0
    selected = None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AVOCADO)
        #AVOCADO
        self.clear()

    # This method draws our assets including constructing a grid
    def on_draw(self):
        arcade.start_render()

        # initialize formatting details
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5

        # Shape for esc button
        arcade.draw_rectangle_filled(840,640,84,50,
                                     arcade.color.GRANNY_SMITH_APPLE)
        # Text for esc button
        arcade.draw_text("ESC",
                         start_x + (SCREEN_WIDTH *.9),
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         font_name="Kenney Future")
        
        #FILL IN BOARD WITH BACKGROUND COLOR
        Board = ((200, 100),
                 (700, 100),
                 (700, 600),
                 (200, 600),)
        arcade.draw_polygon_filled(Board, arcade.color.BUFF)
        
        #DRAW BOARD OUTLINE
        arcade.draw_polygon_outline(Board, arcade.color.BLACK,8)
        
        #DRAW OUTLINES OF SPACES ON BOARD 
        y = 0
        while (y < 10):
            x = 0
            while (x < 10):
                point_list = ((BOARD_LEFT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y),
                    (BOARD_LEFT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                    (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                    (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y))
                arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 4)
                x = x + 1
            y = y + 1


        #draw it
        if Gameboard.selected is not None:
            draw_piece.show_available_moves(Gameboard.selected, total_pieces)
        
        #DRAW LEFT LAKE
        Lake1 = ((LAKE1_LEFT, LAKE_BOTTOM),
                 (LAKE1_RIGHT, LAKE_BOTTOM),
                 (LAKE1_RIGHT, LAKE_TOP),
                 (LAKE1_LEFT, LAKE_TOP),)
        arcade.draw_polygon_filled(Lake1, arcade.color.BLUEBERRY)
        arcade.draw_polygon_outline(Lake1, arcade.color.BLACK,4)
        #DRAW RIGHT LAKE
        Lake2 = ((LAKE2_LEFT, LAKE_BOTTOM),
                 (LAKE2_RIGHT, LAKE_BOTTOM),
                 (LAKE2_RIGHT, LAKE_TOP),
                 (LAKE2_LEFT, LAKE_TOP),)
        arcade.draw_polygon_filled(Lake2, arcade.color.BLUEBERRY)
        arcade.draw_polygon_outline(Lake2, arcade.color.BLACK,4)
        
        yard1 = ((GRAVEYARD_1_LEFT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_1_RIGHT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_1_RIGHT, GRAVEYARD_TOP),
                 (GRAVEYARD_1_LEFT, GRAVEYARD_TOP),)
        arcade.draw_polygon_filled(yard1, arcade.color.DARK_TAUPE)
        arcade.draw_polygon_outline(yard1, arcade.color.BLACK,8)
        
        yard2 = ((GRAVEYARD_2_LEFT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_2_RIGHT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_2_RIGHT, GRAVEYARD_TOP),
                 (GRAVEYARD_2_LEFT, GRAVEYARD_TOP),)
        arcade.draw_polygon_filled(yard2, arcade.color.DARK_TAUPE)
        arcade.draw_polygon_outline(yard2, arcade.color.BLACK,8)

        # draw pieces
        for piece in total_pieces:
            if piece.defeated != True:
                draw_piece.draw(piece)
            #else:
                # piece is defeated --> draw it, but in the graveyary           

        #draw army 1
        i = 0
        for piece in graveyard1:
             draw_piece.draw_start(piece, 1, i)
             i = i+1
        #draw army 2
        i = 0
        for piece in graveyard2:
             draw_piece.draw_start(piece, 2, i)
             i = i+1
             
    def on_mouse_press(self, x, y, button, key_modifiers):
        # escape menu coordinates --> make constants
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        else:
            click = (x,y)
            for piece in total_pieces:
                # if the user has clicked any piece in the list of total pieces enter the if statement
                if draw_piece.select_piece(piece, click) == True:
                    # if there is no selected piece assign it to the one clicked by the user
                    if Gameboard.selected != None:
                        if Gameboard.selected.getPlayer() == piece.getPlayer():
                            # player re-selects one of their other pieces
                            Gameboard.selected = piece
                    else:
                        print(piece.getType() + " selected")
                        Gameboard.selected = piece

            if Gameboard.selected != None:
                is_valid_move, cell_occupant = draw_piece.is_move_available(total_pieces, Gameboard.selected, click)
                if is_valid_move and cell_occupant == None:
                    # move piece to open space
                    draw_piece.move_piece(Gameboard.selected, click)
                    Gameboard.selected = None
                    Gameboard.turn_screen(self)
                if is_valid_move and cell_occupant != None:
                    # player clicked opposing piece: check combat conditions
                    if cell_occupant.getType() != "Lke":
                        is_orthogonal = Piece.check_orthogonal(Gameboard.selected, cell_occupant)
                        if Gameboard.selected.getType() == "Sct":
                            draw_piece.combat(Gameboard.selected, cell_occupant, click, graveyard1, graveyard2, p1_pieces, p2_pieces) #p1_pieces/p2_pieces = Temp Variables
                            Gameboard.turn_screen(self)
                        elif is_orthogonal:
                            if cell_occupant.getType() == "Flg":
                                view = win.Win()
                                self.window.show_view(view)
                            else:
                                draw_piece.combat(Gameboard.selected, cell_occupant, click, graveyard1, graveyard2, p1_pieces, p2_pieces) #p1_pieces/p2_pieces = Temp Variables
                                Gameboard.turn_screen(self)
                    Gameboard.selected = None
            else:
                Gameboard.selected = None
    
    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

    def change_turn():
        if Gameboard.player_turn == 1:
            Gameboard.player_turn = 2
        else:
            Gameboard.player_turn = 1

    def turn_screen(self):
        Gameboard.change_turn()
        view = pass_turn.Pass_Turn()
        self.window.show_view(view)
    
    def get_turn():
        return Gameboard.player_turn

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen