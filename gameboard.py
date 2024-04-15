import arcade
import esc_menu
import pass_turn
import Piece
import draw_piece
import win
from constants import *
import Opponent_AI
import ai_layout
import sound_settings

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


   
    level = sound_settings.Sound.level + 2
    sound = arcade.load_sound("Gameboard_Screen.wav",False)
    media_player = arcade.play_sound(sound, level, 0, looping=True)
    sound.stop(media_player)
    playing = False
    
    
    game_state = "setup"
    highlight_index = 0
    last_screen = "game_board"
    is_menu = False
    last_placement = [] #MIGHT NEVER BE USED
    graveyard1 = Piece.initPieces(PLAYER_ONE)
    graveyard2 = Piece.initPieces(PLAYER_TWO)
    lake_piece_1 = Piece.Piece("Lke", NO_POWER, 2, 4, NON_PLAYER)
    lake_piece_2 = Piece.Piece("Lke", NO_POWER, 3, 4, NON_PLAYER)
    lake_piece_3 = Piece.Piece("Lke", NO_POWER, 2, 5, NON_PLAYER)
    lake_piece_4 = Piece.Piece("Lke", NO_POWER, 3, 5, NON_PLAYER)
    lake_piece_5 = Piece.Piece("Lke", NO_POWER, 6, 4, NON_PLAYER)
    lake_piece_6 = Piece.Piece("Lke", NO_POWER, 7, 4, NON_PLAYER)
    lake_piece_7 = Piece.Piece("Lke", NO_POWER, 6, 5, NON_PLAYER)
    lake_piece_8 = Piece.Piece("Lke", NO_POWER, 7, 5, NON_PLAYER)
    
    army1 = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
    army2 = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
    total_pieces = army1 + army2
    hover = []
    player_turn = 1
    text = [""]
    text_index = 0

    click_counter = 0
    selected = None
    viable = True
    AI = Opponent_AI.bot.ai
    

    AttackRight = None
    AttackLeft = None
    AttackAbove = None
    AttackBelow = None

    def set_is_menu(self, val):
        self.is_menu = val

    def get_is_menu(self):
        return self.is_menu

    def on_show_view(self):
        Gameboard.player_turn = 1
        self.clear()
        Gameboard.player_turn = 1
 
    # This method draws our assets including constructing a grid
    def on_draw(self):
        if self.is_menu == False:
            self.clear()
            arcade.start_render()

            img = arcade.load_texture('SettingsMenu.png')
            arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)           

            
            if Gameboard.sound.is_playing(Gameboard.media_player) == False:
                Gameboard.media_player.seek(0)
                Gameboard.media_player.play()
                Gameboard.playing = True
            
            #   draw game log + back and forwards arrows
            if Gameboard.text[Gameboard.text_index] != "":
                arcade.draw_text(f"{Gameboard.text_index} : {Gameboard.text[Gameboard.text_index]}",450,650,arcade.color.WHITE,15,font_name="Kenney Mini Square Font",bold=True,anchor_x= "center", anchor_y= "center", width=400, multiline = True, align="center", )
            arcade.draw_triangle_filled(TRIANGLE_X1, TRIANGLE_Y1, TRIANGLE_X1, TRIANGLE_Y2, TRIANGLE_X3, TRIANGLE_Y3, arcade.color.BUFF)
            arcade.draw_triangle_outline(TRIANGLE_X1, TRIANGLE_Y1, TRIANGLE_X1, TRIANGLE_Y2, TRIANGLE_X3, TRIANGLE_Y3, arcade.color.BLACK, 4)
            arcade.draw_triangle_filled(TRIANGLE2_X1, TRIANGLE_Y1, TRIANGLE2_X1, TRIANGLE_Y2, TRIANGLE2_X3, TRIANGLE_Y3, arcade.color.BUFF)
            arcade.draw_triangle_outline(TRIANGLE2_X1, TRIANGLE_Y1, TRIANGLE2_X1, TRIANGLE_Y2, TRIANGLE2_X3, TRIANGLE_Y3, arcade.color.BLACK, 4)


            # initialize formatting details
            start_x = 0
            start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.4

            arcade.draw_text("Esc",
                             start_x + (SCREEN_WIDTH *.9),
                             start_y,
                             arcade.color.WHITE,
                             DEFAULT_FONT_SIZE,
                             font_name="Kenney Future")

            # BOARD
            Board = ((GRID_LEFT, GRID_BOTTOM),
                     (GRID_RIGHT, GRID_BOTTOM),
                     (GRID_RIGHT, GRID_TOP),
                     (GRID_LEFT, GRID_TOP),)
            arcade.draw_polygon_filled(Board, arcade.color.BUFF)
            arcade.draw_polygon_outline(Board, arcade.color.BLACK,8)
            #DRAW BOARD GRID OUTLINE
            y = 0
            while (y < ROW_COUNT):
                x = 0
                while (x < COLUMN_COUNT):
                    point_list = ((BOARD_LEFT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y),
                        (BOARD_LEFT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                        (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_BOTTOM + BOARD_MARGIN*y),
                        (BOARD_RIGHT + BOARD_MARGIN*x, BOARD_TOP + BOARD_MARGIN*y))
                    arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 4)
                    x += 1
                y += 1

           # LAKES
            lake1 = ((LAKE1_LEFT, LAKE_BOTTOM),
                     (LAKE1_RIGHT, LAKE_BOTTOM),
                     (LAKE1_RIGHT, LAKE_TOP),
                     (LAKE1_LEFT, LAKE_TOP))
            arcade.draw_polygon_filled(lake1, arcade.color.BLUEBERRY)
            arcade.draw_polygon_outline(lake1, arcade.color.BLACK,4)
            lake2 = ((LAKE2_LEFT, LAKE_BOTTOM),
                     (LAKE2_RIGHT, LAKE_BOTTOM),
                     (LAKE2_RIGHT, LAKE_TOP),
                     (LAKE2_LEFT, LAKE_TOP),)
            arcade.draw_polygon_filled(lake2, arcade.color.BLUEBERRY)
            arcade.draw_polygon_outline(lake2, arcade.color.BLACK,4)
            # GRAVEYARDS
            yard1 = ((GRAVEYARD_1_LEFT, GRAVEYARD_BOTTOM),
                     (GRAVEYARD_1_RIGHT, GRAVEYARD_BOTTOM),
                     (GRAVEYARD_1_RIGHT, GRAVEYARD_TOP),
                     (GRAVEYARD_1_LEFT, GRAVEYARD_TOP),)
            arcade.draw_polygon_filled(yard1, arcade.color.DARK_TAUPE)
            arcade.draw_polygon_outline(yard1, arcade.color.BLACK,8)
            arcade.draw_text("1",
                             start_x - (SCREEN_WIDTH * .37),
                             start_y - (SCREEN_HEIGHT * .52),
                             arcade.color.GRAY,
                             DEFAULT_FONT_SIZE * 10,
                             width=SCREEN_WIDTH,
                             align="center",
                             font_name="Kenney Future")
            yard2 = ((GRAVEYARD_2_LEFT, GRAVEYARD_BOTTOM),
                     (GRAVEYARD_2_RIGHT, GRAVEYARD_BOTTOM),
                     (GRAVEYARD_2_RIGHT, GRAVEYARD_TOP),
                     (GRAVEYARD_2_LEFT, GRAVEYARD_TOP),)
            arcade.draw_polygon_filled(yard2, arcade.color.DARK_TAUPE)
            arcade.draw_polygon_outline(yard2, arcade.color.BLACK,8)
            arcade.draw_text("2",
                            start_x + (SCREEN_WIDTH * .42),
                            start_y - (SCREEN_HEIGHT * .52),
                            arcade.color.GRAY,
                            DEFAULT_FONT_SIZE * 10,
                            width=SCREEN_WIDTH,
                            align="center",
                            font_name="Kenney Future")

            # PIECES
            Gameboard.total_pieces = Gameboard.army1 + Gameboard.army2 
            for piece in Gameboard.army1:
                if piece.defeated != True:
                    draw_piece.draw(piece, 1)

            for piece in Gameboard.army2:
                if piece.defeated != True:
                    draw_piece.draw(piece, 2)

            i = 0
            for piece in Gameboard.graveyard1:
                 draw_piece.draw_start(piece, 1, i)
                 i += 1
            i = 0
            for piece in Gameboard.graveyard2:
                 draw_piece.draw_start(piece, 2, i)
                 i += 1

            if Gameboard.selected is not None:
                draw_piece.show_available_moves(Gameboard.selected, Gameboard.total_pieces)

            if Gameboard.AttackRight != None:
                arcade.draw_circle_filled(Gameboard.AttackRight[0], Gameboard.AttackRight[1], 
                                          Gameboard.AttackRight[2], Gameboard.AttackRight[3])
            if Gameboard.AttackLeft != None:
                arcade.draw_circle_filled(Gameboard.AttackLeft[0], Gameboard.AttackLeft[1], 
                                          Gameboard.AttackLeft[2], Gameboard.AttackLeft[3])
            if Gameboard.AttackAbove != None:
                arcade.draw_circle_filled(Gameboard.AttackAbove[0], Gameboard.AttackAbove[1],
                                          Gameboard.AttackAbove[2], Gameboard.AttackAbove[3])
            if Gameboard.AttackBelow != None:
                arcade.draw_circle_filled(Gameboard.AttackBelow[0], Gameboard.AttackBelow[1], 
                                          Gameboard.AttackBelow[2], Gameboard.AttackBelow[3])

            #Setup Phase: Place pieces from graveyards
            if Gameboard.game_state == "setup":
                if Gameboard.player_turn == PLAYER_ONE and len(Gameboard.graveyard1) != 0:
                    Gameboard.player_turn = PLAYER_ONE
                    draw_piece.show_available_placements(Gameboard.total_pieces, PLAYER_ONE)
                    draw_piece.add_highlight(1, Gameboard.highlight_index)
                    if Gameboard.highlight_index >= len(Gameboard.graveyard1):
                        Gameboard.highlight_index = Gameboard.highlight_index - 1
                else:
                    Gameboard.player_turn = PLAYER_TWO
                if Gameboard.player_turn == PLAYER_TWO and len(Gameboard.graveyard2) != 0:
                    if Gameboard.AI != AI_OFF:
                        ai_layout.gen_layout(1, Gameboard.graveyard2, Gameboard.army2)
                        pass_turn.Pass_Turn.change_turn()
                    else: 
                        pass_turn.Pass_Turn.player_turn = PLAYER_TWO
                        draw_piece.show_available_placements(Gameboard.total_pieces, 2)
                        draw_piece.add_highlight(2, Gameboard.highlight_index)
                        if Gameboard.highlight_index >= len(Gameboard.graveyard2):
                            Gameboard.highlight_index = Gameboard.highlight_index - 1
                else:
                    pass_turn.Pass_Turn.player_turn = PLAYER_ONE
                if len(Gameboard.graveyard1) == 0 and len(Gameboard.graveyard2) == 0:
                    Gameboard.game_state = "play"
             
    def on_mouse_press(self, x, y, button, key_modifiers):
        click = (x,y)
        if x >= ESC_LEFT and x <= ESC_RIGHT and y <= ESC_TOP and y >= ESC_BOTTOM:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        if x>=215 and x<= 260 and y>= 625 and y<= 670:
            if Gameboard.text_index > 1:
                Gameboard.text_index = Gameboard.text_index -1
        if x>= 640 and x<=685 and y>= 625 and y<= 670:
            if Gameboard.text_index < len(Gameboard.text)-1:
                Gameboard.text_index = Gameboard.text_index +1


        if Gameboard.game_state == "setup":
            click = (x,y)
            if pass_turn.Pass_Turn.player_turn == 1:
                if x >= GRID_LEFT and x <= GRID_RIGHT and y >= GRID_BOTTOM and y <= GRID_BOTTOM + NUM_START_ROWS*CELL_WIDTH:
                    draw_piece.place_piece(Gameboard.graveyard1[Gameboard.highlight_index], click, Gameboard.graveyard1, Gameboard.army1)
                    place_sound = arcade.load_sound("Placed.wav",False)
                    arcade.play_sound(place_sound, Gameboard.level, 0)
            if pass_turn.Pass_Turn == PLAYER_TWO and Gameboard.AI == AI_OFF:
                if x >= GRID_LEFT and x <= GRID_RIGHT and y <= GRID_TOP and y >= GRID_TOP - NUM_START_ROWS*CELL_WIDTH:
                    draw_piece.place_piece(Gameboard.graveyard2[Gameboard.highlight_index], click, Gameboard.graveyard2, Gameboard.army2)
                    place_sound = arcade.load_sound("Placed.wav",False)
                    arcade.play_sound(place_sound, Gameboard.level, 0)

        if Gameboard.game_state == "play":
            click = (x,y)
            for piece in Gameboard.total_pieces:
                
                if draw_piece.select_piece(piece, click, pass_turn.Pass_Turn.player_turn) == True:
                    if Gameboard.selected != None:
                        if Gameboard.selected.getPlayer() == piece.getPlayer():
                            Gameboard.selected = piece
                    else:
                        Gameboard.selected = piece

            if Gameboard.selected != None:
                is_valid_move, cell_occupant = draw_piece.is_move_available(Gameboard.total_pieces, Gameboard.selected, click)
                if is_valid_move and cell_occupant == None:
                    draw_piece.move_piece(Gameboard.selected, click)
                    # Make a sound
                    place_sound = arcade.load_sound("Placed.wav",False)
                    arcade.play_sound(place_sound, Gameboard.level, 0)
                    
                    Gameboard.selected = None
                    Gameboard.text.append("PLAYER MOVES")
                    Gameboard.text_index = len(Gameboard.text)-1
                    if Gameboard.AI == 0:
                        pass_turn.Pass_Turn.turn_screen(self)
                    else:
                        pass_turn.Pass_Turn.change_turn()
                if is_valid_move and cell_occupant != None:
                    if cell_occupant.getType() != "Lke":
                        is_orthogonal = Piece.check_orthogonal(Gameboard.selected, cell_occupant, Gameboard.total_pieces)
                        if is_orthogonal:
                            if cell_occupant.getType() == "Flg":
                                if Gameboard.sound.is_playing(Gameboard.media_player) or Gameboard.playing == True:
                                    Gameboard.sound.stop(Gameboard.media_player)
                                    Gameboard.playing = False
                                self.window.show_view(win.Win(self))
                            else:
                                Gameboard.text.append(draw_piece.combat(Gameboard.selected, cell_occupant, click, Gameboard.graveyard1, Gameboard.graveyard2, Gameboard.army1, Gameboard.army2)) #p1_pieces/p2_pieces = Temp Variables
                                Gameboard.text_index = len(Gameboard.text)-1
                                if Gameboard.AI == 0:
                                    # set time of move, this is used as a marker for a timer for the delay to see your piece move before the screen changes
                                    # pass_turn.Pass_Turn.turn_pause = time.time()
                                    Gameboard.turn_screen(self)
                                else:
                                    pass_turn.Pass_Turn.change_turn()
                    Gameboard.selected = None
            else:
                Gameboard.selected = None

            if (Gameboard.AI == EASY or Gameboard.AI == MEDIUM or Gameboard.AI == HARD) and (pass_turn.Pass_Turn.player_turn == PLAYER_TWO):
                Opponent_AI.bot.select_piece(self, Gameboard.army2)
                pass_turn.Pass_Turn.change_turn()
                
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
        
    
    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.ESCAPE):
            self.window.show_view(esc_menu.Escape(self))
            esc_menu.Escape.last_screen = Gameboard.last_screen

        if (Gameboard.game_state == "setup"):
            
            if Gameboard.player_turn == PLAYER_ONE:
                yard = Gameboard.graveyard1
                army = Gameboard.army1
            else:
                yard = Gameboard.graveyard2
                army = Gameboard.army2

            if (key == arcade.key.LEFT):
                    if Gameboard.highlight_index != 0:
                        Gameboard.highlight_index = Gameboard.highlight_index - 1
            if (key == arcade.key.RIGHT):
                if Gameboard.highlight_index+1 < len(yard): 
                    Gameboard.highlight_index = Gameboard.highlight_index + 1
            if (key == arcade.key.DOWN):
                if Gameboard.highlight_index + 4 < len(yard):
                    Gameboard.highlight_index = Gameboard.highlight_index + GRAVEYARD_CELLS_WIDE
            if (key == arcade.key.UP):
                if Gameboard.highlight_index>=4:
                    Gameboard.highlight_index = Gameboard.highlight_index - GRAVEYARD_CELLS_WIDE

            #Place a full army by hitting the R key.
            if key == arcade.key.R:
                if pass_turn.Pass_Turn.player_turn == 1 and len(Gameboard.graveyard1) == NUM_PIECES:
                    for i in range(NUM_START_ROWS):
                        for x in range (COLUMN_COUNT):
                            if pass_turn.Pass_Turn.player_turn == 1 and len(Gameboard.graveyard1) == NUM_PIECES:
                                for i in range(NUM_START_ROWS):
                                    for x in range (COLUMN_COUNT):
                                        draw_piece.place_piece(yard[0], (x,i), yard, army)
                    pass_turn.Pass_Turn.change_turn()
                    place_sound = arcade.load_sound("Placed.wav",False)
                    arcade.play_sound(place_sound, Gameboard.level, 0)
                elif pass_turn.Pass_Turn.player_turn == 2 and Gameboard.AI == 0 and len(Gameboard.graveyard2) == NUM_PIECES:
                    for i in range(4):
                        for x in range(10):
                            draw_piece.place_piece(yard[0], (x,9-i), yard, army)
                    pass_turn.Pass_Turn.change_turn()
                    place_sound = arcade.load_sound("Placed.wav",False)
                    arcade.play_sound(place_sound, Gameboard.level, 0)



                            
        if key == arcade.key.Y:
            if Gameboard.game_state == "setup": 
                x = Gameboard.hover[0]
                y = Gameboard.hover[1]
                if pass_turn.Pass_Turn.player_turn == PLAYER_ONE:
                    if x >= 200 and x <= 700 and y>=100 and y<=300:
                        draw_piece.place_piece(Gameboard.graveyard1[Gameboard.highlight_index], Gameboard.hover, Gameboard.graveyard1, Gameboard.army1)
                        place_sound = arcade.load_sound("Placed.wav",False)
                        arcade.play_sound(place_sound, Gameboard.level, 0)
                if Gameboard.player_turn == PLAYER_TWO:
                    if x >= GRID_LEFT and x <= GRID_RIGHT and y <= GRID_TOP and y >= GRID_TOP - NUM_START_ROWS*CELL_WIDTH:
                        draw_piece.place_piece(Gameboard.graveyard2[Gameboard.highlight_index], Gameboard.hover, Gameboard.graveyard2, Gameboard.army2)
                        place_sound = arcade.load_sound("Placed.wav",False)
                        arcade.play_sound(place_sound, Gameboard.level, 0)
                    
    def change_turn():
        if Gameboard.player_turn == PLAYER_ONE:
            Gameboard.player_turn = PLAYER_TWO
        else:
            Gameboard.player_turn = PLAYER_ONE

    def turn_screen(self):
        pass_turn.Pass_Turn.change_turn()
        view = pass_turn.Pass_Turn()
        self.window.show_view(view)

    def get_visibility(self):
        return Gameboard.visible
    
    def set_visibility(self, visible):
        Gameboard.visible = visible

    def get_ai():
        return Gameboard.AI

    def changeAI(ai):
        Gameboard.AI = ai

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen
    
