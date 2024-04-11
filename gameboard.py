import arcade
import esc_menu
import pass_turn
import Piece
import draw_piece
import win
from constants import *

game_state = "setup"


graveyard1 = Piece.initPieces(1)
graveyard2 = Piece.initPieces(2)
army1 = []
army2 = []








# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    highlight_index = 0
    last_screen = "game_board"
    total_pieces = army1 + army2
    last_placement = []

    
    hover = []

    player_turn = 2

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
            draw_piece.show_available_moves(Gameboard.selected, Gameboard.total_pieces)
        
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
        for piece in Gameboard.total_pieces:
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
        for piece in army1:
                    draw_piece.draw(piece)
        for piece in army2:
                    draw_piece.draw(piece)
                    
        Gameboard.total_pieces = army1 + army2

        
        global game_state  
        if game_state == "setup":
            if Gameboard.player_turn == 1 and len(graveyard1) !=0:
                Gameboard.player_turn = 1
                draw_piece.show_available_placements(Gameboard.total_pieces, 1)
                draw_piece.add_highlight(1, Gameboard.highlight_index)
                if Gameboard.highlight_index >= len(graveyard1):
                    Gameboard.highlight_index = Gameboard.highlight_index-1 

                


            else:
                Gameboard.player_turn = 2
            if Gameboard.player_turn == 2 and len(graveyard2) !=0:
                Gameboard.player_turn = 2
                draw_piece.show_available_placements(Gameboard.total_pieces, 2)
                draw_piece.add_highlight(2, Gameboard.highlight_index)
                if Gameboard.highlight_index >= len(graveyard2):
                    Gameboard.highlight_index = Gameboard.highlight_index-1 

                

            else:
                Gameboard.player_turn = 1
            if len(graveyard1) == 0 and len(graveyard2) == 0:
                game_state = "play"
                print(game_state)
                
    
   
             
    def on_mouse_press(self, x, y, button, key_modifiers):
        # escape menu coordinates --> make constants
        click = (x,y)
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

        if game_state == "setup":
            click = (x,y)
            if Gameboard.player_turn == 1:
                if x >= 200 and x <= 700 and y>=100 and y<=300:
                    
                    draw_piece.place_piece(graveyard1[Gameboard.highlight_index], click, graveyard1, army1)
            if Gameboard.player_turn == 2:
                if x>= 200 and x <= 700 and y<=600 and y>=400:
                    draw_piece.place_piece(graveyard2[Gameboard.highlight_index], click, graveyard2, army2)
            

                    
        
        if game_state == "play":
            click = (x,y)
            print(click)
            print("working")

            print(len(Gameboard.total_pieces))
            for piece in Gameboard.total_pieces:


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
                else:
                    print (draw_piece.select_piece(piece, click))

            if Gameboard.selected != None:
                is_valid_move, cell_occupant = draw_piece.is_move_available(Gameboard.total_pieces, Gameboard.selected, click)
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
                            draw_piece.combat(Gameboard.selected, cell_occupant, click, graveyard1, graveyard2, army1, army2) #p1_pieces/p2_pieces = Temp Variables
                            Gameboard.turn_screen(self)
                        elif is_orthogonal:
                            if cell_occupant.getType() == "Flg":
                                view = win.Win()
                                self.window.show_view(view)
                            else:
                                draw_piece.combat(Gameboard.selected, cell_occupant, click, graveyard1, graveyard2, army1, army2) #p1_pieces/p2_pieces = Temp Variables
                                Gameboard.turn_screen(self)
                    Gameboard.selected = None
            else:
                Gameboard.selected = None
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        Gameboard.hover = x,y
        # Move the player sprite to place its center on the mouse x, y
        
    
    def on_key_press(self, key, key_modifiers ):
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        if (game_state == "setup"):
            if Gameboard.player_turn == 1:
                yard = graveyard1
                army = army1
            else:
                yard = graveyard2
                army = army2
            if (key == arcade.key.LEFT):
                    if Gameboard.highlight_index != 0:
                        Gameboard.highlight_index = Gameboard.highlight_index -1
            if (key == arcade.key.RIGHT):
                if Gameboard.highlight_index+1 < len(yard): 
                    Gameboard.highlight_index = Gameboard.highlight_index + 1
            if (key == arcade.key.DOWN):
                if Gameboard.highlight_index + 4 < len(yard):
                    Gameboard.highlight_index = Gameboard.highlight_index + 4
            if (key == arcade.key.UP):
                if Gameboard.highlight_index>=4:
                    Gameboard.highlight_index = Gameboard.highlight_index - 4
            if (key == arcade.key.R):
                index = 0
                print(len(yard))
                if Gameboard.player_turn == 1:
                    for i in range(4):
                        for x in range (10):
                            draw_piece.place_piece(yard[0], (x,i), yard, army)
                else:
                    for i in range(4):
                        for x in range(10):
                            draw_piece.place_piece(yard[0], (x,9-i), yard, army)

                            
        if key == arcade.key.Y:
            if game_state == "setup": 
                x = Gameboard.hover[0]
                y = Gameboard.hover[1]
                if Gameboard.player_turn == 1:
                    if x >= 200 and x <= 700 and y>=100 and y<=300:
                        draw_piece.place_piece(graveyard1[Gameboard.highlight_index], Gameboard.hover, graveyard1, army1)
                if Gameboard.player_turn == 2:
                    if x>= 200 and x <= 700 and y<=600 and y>=400:
                        draw_piece.place_piece(graveyard2[Gameboard.highlight_index], Gameboard.hover, graveyard2, army2)
            

                    

                
                    

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
    
