import arcade
import menu
import esc_menu
import pass_turn
import Piece
import draw_piece
import time
import win
from constants import *
import Opponent_AI
import ai_layout









lake_piece_1 = Piece.Piece("Lke", 0, 2, 4, 3)
lake_piece_2 = Piece.Piece("Lke", 0, 3, 4, 3)
lake_piece_3 = Piece.Piece("Lke", 0, 2, 5, 3)
lake_piece_4 = Piece.Piece("Lke", 0, 3, 5, 3)

lake_piece_5 = Piece.Piece("Lke", 0, 6, 4, 3)
lake_piece_6 = Piece.Piece("Lke", 0, 7, 4, 3)
lake_piece_7 = Piece.Piece("Lke", 0, 6, 5, 3)
lake_piece_8 = Piece.Piece("Lke", 0, 7, 5, 3)


# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    game_state = "setup"
    highlight_index = 0
    last_screen = "game_board"
    last_placement = [] #MIGHT NEVER BE USED
    graveyard1 = Piece.initPieces(1)
    graveyard2 = Piece.initPieces(2)
    army1 = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
    army2 = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
    total_pieces = army1 + army2
    hover = []
    player_turn = 1
    click_counter = 0
    selected = None
    AI = Opponent_AI.bot.ai
    

    AttackRight = None
    AttackLeft = None
    AttackAbove = None
    AttackBelow = None

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AVOCADO)
        #AVOCADO
        self.clear()
        if menu.Menu.sound.is_playing(menu.Menu.media_player) or menu.Menu.playing == True:
            menu.Menu.sound.stop(menu.Menu.media_player)
            menu.Menu.playing = False



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
        
        Gameboard.total_pieces = Gameboard.army1 + Gameboard.army2

            
       
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
        for piece in Gameboard.army1:
            if piece.defeated != True:
                draw_piece.draw(piece, 1)
               

        for piece in Gameboard.army2:
            if piece.defeated != True:
                draw_piece.draw(piece)  
            if pass_turn.Pass_Turn.turn_pause != 0:
                if time.time() - pass_turn.Pass_Turn.turn_pause > .4:
                    pass_turn.Pass_Turn.turn_pause = 0
                    pass_turn.Pass_Turn.turn_screen(self)
            #else:
                # piece is defeated --> draw it, but in the graveyary           
                draw_piece.draw(piece, 2)
        
        
        if Gameboard.AttackRight != None:
            arcade.draw_circle_filled(Gameboard.AttackRight[0], Gameboard.AttackRight[1], Gameboard.AttackRight[2], Gameboard.AttackRight[3])

        if Gameboard.AttackLeft != None:
            arcade.draw_circle_filled(Gameboard.AttackLeft[0], Gameboard.AttackLeft[1], Gameboard.AttackLeft[2],
                                      Gameboard.AttackLeft[3])
        if Gameboard.AttackAbove != None:
            arcade.draw_circle_filled(Gameboard.AttackAbove[0], Gameboard.AttackAbove[1], Gameboard.AttackAbove[2],
                                      Gameboard.AttackAbove[3])
        if Gameboard.AttackBelow != None:
            arcade.draw_circle_filled(Gameboard.AttackBelow[0], Gameboard.AttackBelow[1], Gameboard.AttackBelow[2],
                                      Gameboard.AttackBelow[3])
        
        
        if Gameboard.game_state == "setup":
            if Gameboard.player_turn == 1 and len(Gameboard.graveyard1) !=0:
                Gameboard.player_turn = 1
                draw_piece.show_available_placements(Gameboard.total_pieces, 1)
                draw_piece.add_highlight(1, Gameboard.highlight_index)
                if Gameboard.highlight_index >= len(Gameboard.graveyard1):
                    Gameboard.highlight_index = Gameboard.highlight_index-1 

                


            else:
                Gameboard.player_turn = 2
            if Gameboard.player_turn == 2 and len(Gameboard.graveyard2) !=0:
                Gameboard.player_turn = 2
                draw_piece.show_available_placements(Gameboard.total_pieces, 2)
                draw_piece.add_highlight(2, Gameboard.highlight_index)
                if Gameboard.highlight_index >= len(Gameboard.graveyard2):
                    Gameboard.highlight_index = Gameboard.highlight_index-1 

                

            else:
                Gameboard.player_turn = 1
            if len(Gameboard.graveyard1) == 0 and len(Gameboard.graveyard2) == 0:
                Gameboard.game_state = "play"
                print(Gameboard.game_state)



        #draw army 1
        i = 0
        for piece in Gameboard.graveyard1:
             draw_piece.draw_start(piece, 1, i)
             i = i+1
        #draw army 2
        i = 0
        for piece in Gameboard.graveyard2:
             draw_piece.draw_start(piece, 2, i)
             i = i+1
        for piece in Gameboard.army1:
                    draw_piece.draw(piece, 1)
        for piece in Gameboard.army2:
                    draw_piece.draw(piece, 2)
                    

                
    
   

        if Gameboard.AttackRight != None:
            arcade.draw_circle_filled(Gameboard.AttackRight[0], Gameboard.AttackRight[1], Gameboard.AttackRight[2], Gameboard.AttackRight[3])

        if Gameboard.AttackLeft != None:
            arcade.draw_circle_filled(Gameboard.AttackLeft[0], Gameboard.AttackLeft[1], Gameboard.AttackLeft[2],
                                      Gameboard.AttackLeft[3])
        if Gameboard.AttackAbove != None:
            arcade.draw_circle_filled(Gameboard.AttackAbove[0], Gameboard.AttackAbove[1], Gameboard.AttackAbove[2],
                                      Gameboard.AttackAbove[3])
        if Gameboard.AttackBelow != None:
            arcade.draw_circle_filled(Gameboard.AttackBelow[0], Gameboard.AttackBelow[1], Gameboard.AttackBelow[2],
                                      Gameboard.AttackBelow[3])

             
    def on_mouse_press(self, x, y, button, key_modifiers):
        print(f"THIS CLICK: {draw_piece.get_coordinates((x,y))}")
        print(Gameboard.player_turn)
        if Gameboard.selected:
            print(f"{Gameboard.selected.getType()} at {Gameboard.selected.getPosition()}")
        else:
            print("Nothing selected")
       # escape menu coordinates --> make constants
        click = (x,y)
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

        if Gameboard.game_state == "setup":
            click = (x,y)
            if Gameboard.player_turn == 1:
                if x >= 200 and x <= 700 and y>=100 and y<=300:
                    
                    draw_piece.place_piece(Gameboard.graveyard1[Gameboard.highlight_index], click, Gameboard.graveyard1, Gameboard.army1)
            if Gameboard.player_turn == 2 and Gameboard.AI == 0:
                if x>= 200 and x <= 700 and y<=600 and y>=400:
                    draw_piece.place_piece(Gameboard.graveyard2[Gameboard.highlight_index], click, Gameboard.graveyard2, Gameboard.army2)


        if Gameboard.game_state == "play":
            # if Gameboard.AI == 0:   #WHAT DOES THIS DO, IS THERE MORE CODE TO ADD?
            click = (x,y)
            for piece in Gameboard.total_pieces:


            # if the user has clicked any piece in the list of total pieces enter the if statement
                if draw_piece.select_piece(piece, click, Gameboard.player_turn) == True:
                    # if there is no selected piece assign it to the one clicked by the user
                    if Gameboard.selected != None:
                        if Gameboard.selected.getPlayer() == piece.getPlayer():
                            # player re-selects one of their other pieces
                            Gameboard.selected = piece
                    else:
                        print(piece.getType() + " selected")
                        Gameboard.selected = piece
                else:
                    pass
                    # print("else line 267")
                    # print (draw_piece.select_piece(piece, click, Gameboard.player_turn))

            if Gameboard.selected != None:
                is_valid_move, cell_occupant = draw_piece.is_move_available(Gameboard.total_pieces, Gameboard.selected, click)
                if is_valid_move and cell_occupant == None:
                    # move piece to open space
                    draw_piece.move_piece(Gameboard.selected, click)
                    Gameboard.selected = None
                    if Gameboard.AI == 0:
                        # set time of move, this is used as a marker for a timer for the delay to see your piece move before the screen changes
                    pass_turn.Pass_Turn.turn_pause = time.time()
                    else:
                        Gameboard.change_turn()
                if is_valid_move and cell_occupant != None:
                # player clicked opposing piece: check combat conditions
                    if cell_occupant.getType() != "Lke":
                        is_orthogonal = Piece.check_orthogonal(Gameboard.selected, cell_occupant, Gameboard.total_pieces)
                        if is_orthogonal:
                            if cell_occupant.getType() == "Flg":
                                view = win.Win()
                                self.window.show_view(view)
                            else:
                                draw_piece.combat(Gameboard.selected, cell_occupant, click, Gameboard.graveyard1, Gameboard.graveyard2, Gameboard.army1, Gameboard.army2) #p1_pieces/p2_pieces = Temp Variables
                                if Gameboard.AI == 0:
                                    # set time of move, this is used as a marker for a timer for the delay to see your piece move before the screen changes
                                pass_turn.Pass_Turn.turn_pause = time.time()
                                else:
                                    Gameboard.change_turn()
                    Gameboard.selected = None
            else:
                Gameboard.selected = None

            if (Gameboard.AI == 1 or Gameboard.AI == 2 or Gameboard.AI == 3) and (Gameboard.player_turn == 2):
                Opponent_AI.bot.select_piece(self, Gameboard.army2)
                print("AI Moved")
                Gameboard.change_turn()
                
    def setAttack(self, loc, x, y, num, color):
        if loc == "right":
            Gameboard.AttackRight = [x, y, num, color]
        elif loc == "left":
            Gameboard.AttackLeft = [x, y, num, color]
        elif loc == "up":
            Gameboard.AttackAbove = [x, y, num, color]
        elif loc == "down":
            Gameboard.AttackBelow = [x, y, num, color]

    def resetAttack(self):
        Gameboard.AttackRight = None
        Gameboard.AttackLeft = None
        Gameboard.AttackAbove = None
        Gameboard.AttackBelow = None
    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        Gameboard.hover = x,y
        # Move the player sprite to place its center on the mouse x, y
        
    
    def on_key_press(self, key, key_modifiers ):
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        if (Gameboard.game_state == "setup"):
            if Gameboard.player_turn == 1:
                yard = Gameboard.graveyard1
                army = Gameboard.army1
            else:
                yard = Gameboard.graveyard2
                army = Gameboard.army2
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
            #Place a full army by hitting the R key.
            if (key == arcade.key.R):
                print(len(yard))
                if Gameboard.player_turn == 1:
                    for i in range(4):
                        for x in range (10):
                            draw_piece.place_piece(yard[0], (x,i), yard, army)
                elif Gameboard.player_turn == 2 and Gameboard.AI == 0:
                    for i in range(4):
                        for x in range(10):
                            draw_piece.place_piece(yard[0], (x,9-i), yard, army)
                elif Gameboard.player_turn == 2 and Gameboard.AI != 0:
                    ai_layout.gen_layout(1, Gameboard.graveyard2, Gameboard.army2)
                    Gameboard.change_turn()
                    print(f"Done! {Gameboard.AI}")


                            
        if key == arcade.key.Y:
            if Gameboard.game_state == "setup": 
                x = Gameboard.hover[0]
                y = Gameboard.hover[1]
                if Gameboard.player_turn == 1:
                    if x >= 200 and x <= 700 and y>=100 and y<=300:
                        draw_piece.place_piece(Gameboard.graveyard1[Gameboard.highlight_index], Gameboard.hover, Gameboard.graveyard1, Gameboard.army1)
                if Gameboard.player_turn == 2:
                    if x>= 200 and x <= 700 and y<=600 and y>=400:
                        draw_piece.place_piece(Gameboard.graveyard2[Gameboard.highlight_index], Gameboard.hover, Gameboard.graveyard2, Gameboard.army2)
            

                    

                
                    

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

    def get_ai():
        return Gameboard.AI

    def changeAI(ai):
        Gameboard.AI = ai


    @classmethod
    def get_last_screen(cls):
        return cls.last_screen
    
