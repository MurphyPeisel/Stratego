import arcade
import menu
import esc_menu

# initialize formatting details
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 30
DEFAULT_FONT_SIZE = 10

# initialize escape box 
ESC_BOX_CENTER = (810, 670)
ESC_BOX_WIDTH = 84
ESC_BOX_HEIGHT = 50

# calculate escape box bounds
ESC_BOX_X1 = ESC_BOX_CENTER[0] - ESC_BOX_WIDTH / 2
ESC_BOX_X2 = ESC_BOX_CENTER[0] + ESC_BOX_WIDTH / 2
ESC_BOX_Y1 = ESC_BOX_CENTER[1] - ESC_BOX_HEIGHT / 2
ESC_BOX_Y2 = ESC_BOX_CENTER[1] + ESC_BOX_HEIGHT / 2

class Rules(arcade.View):
    last_screen = "rules"

    def __init__(self, menu_instance):
        super().__init__()
        self.menu_instance = menu_instance

    def on_show_view(self):
        self.background_color = arcade.color.BEIGE

    def on_draw(self):
        self.clear()
        arcade.start_render()

        # draw rectangle for the 'esc' button
        arcade.draw_rectangle_filled(ESC_BOX_CENTER[0], 
                                     ESC_BOX_CENTER[1],
                                     ESC_BOX_WIDTH,
                                     ESC_BOX_HEIGHT,
                                     arcade.color.GRANNY_SMITH_APPLE)
        
        # initialize x, y variables for drawing text
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT
        arcade.draw_text("ESC",
                         start_x + (SCREEN_WIDTH *.88),
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         font_name="Kenney Future",
                         width=84,
                         align="left")

        arcade.draw_text("Stratego Rules",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 3,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")

        # update x, y variables as lines are drawn to the screen
        start_x = 10
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.7
        arcade.draw_text("Welcome to Stratego:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE * 2, bold=True,
                         font_name = "Kenney Future")

        start_y -= DEFAULT_LINE_HEIGHT * 0.7
        arcade.draw_text("The object of the game is to capture the enemy Flag. "
                         "As the commander of an army you are in charge of 33 movable "
                         "units of differing rank and 7 immovable pieces: 6 Bombs and 1 Flag.",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=SCREEN_WIDTH,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT * 1.5
        # keep track of this y-value for more text further along the x-axis
        col_2_start_y = start_y
        arcade.draw_text("MOVABLE PIECES:\n"
                         "Rank - Name (Quantity)\n"
                         "----------------\n"
                         "10 - Marshal (1)\n"
                         "9 - General (1)\n"
                         "8 - Colonel (2)\n"
                         "7 - Major (3)\n"
                         "6 - Captain (4)\n"
                         "5 - Lieutenant (4)\n"
                         "4 - Sergeant (4)\n"
                         "3 - Miner (5)\n"
                         "2 - Scout (8)\n"
                         "S - Spy (1)\n",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 0.8,
                         multiline=True,
                         width=SCREEN_WIDTH / 1.1,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT *  6
        arcade.draw_text("SETUP:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE * 1.5, bold=True,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT * 0.5
        arcade.draw_text("Player 1 places all of their pieces on the first 4 rows of their side of theboard. "
                         "Then, player 2 does the same on their side of the board. ",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=SCREEN_WIDTH,
                         font_name = "Kenney Future")

        start_y -= DEFAULT_LINE_HEIGHT * 1.15
        arcade.draw_text("GAMEPLAY:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE * 1.5, bold=True,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT * 0.5
        arcade.draw_text("On your turn you must do one of the following:\n"
                         "*MOVE* one of your playing pieces to an open adjacent space.\n"
                         "\t1. Pieces move one square at a time, forward, backward or sideways.\n"
                         "\t(Exception: See special Scout Movement Privilege)\n"
                         "\t2. Pieces cannot move diagonally. They cannot jump over another piece.\n"
                         "\tThey cannot move onto a square already occupied by another piece (unless attacking)\n"
                         "\t3. Pieces cannot jump over or move onto the two lake areas in the center of the board.\n"
                         "\t4.  A piece cannot move back and forth between the same two squares in three consecutive \n"
                         "\t turns.\n"
                         "*ATTACK* one of your opponents playing pieces.\n"
                         "\tNOTE: Flag and Bomb pieces cannot attack.\n"
                         "\t1. Attack Position: When a red and blue piece are orthogonally adjacent\n"
                         "\tthey are in a position to attack\n"
                         "\t2. How to Attack: To attack on your turn, click on your piece and then click on the piece\n"
                         "\tyou would like to attack. The rank of each piece is then revealed and the piece with the\n"
                         "\tlower rank is removed from the board. If the winning piece is the attacker, \n"
                         "\tit takes the place of the losing piece. If the winning piece is the defender, it does not move.\n"
                         "\t3. When pieces of the same rank battle, both pieces are removed from the board.\n",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=SCREEN_WIDTH,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT * 10
        arcade.draw_text("ENDING THE GAME:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE * 1.5, bold=True,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT * 0.5
        arcade.draw_text("The first player to attack an opponent's Flag captures it and wins the game.\n"
                         "Or, if all of a player's movable pieces have been removed, they lose.",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=SCREEN_WIDTH,
                         font_name = "Kenney Future")
        
        # x, y values for second column of text
        col_2_start_y += DEFAULT_LINE_HEIGHT * 0.5 
        col_2_start_x = SCREEN_WIDTH / 4.85
        arcade.draw_text("SPECIAL PRIVILEGES:", 
                         col_2_start_x, 
                         col_2_start_y, 
                         arcade.color.FRENCH_WINE, 
                         DEFAULT_FONT_SIZE * 0.8,
                         width = SCREEN_WIDTH, 
                         bold = True,
                         font_name = "Kenney Future")
        
        col_2_start_y -= DEFAULT_LINE_HEIGHT * 0.5
        arcade.draw_text("Scout:\n"
                         "\tScouts are the only pieces allowed to both move and attack on the same turn.\n"
                         "\tA Scout can move forward, backward, or sideways any number of open spaces into\n"
                         "\tan attack position. Once in position, it can attack.\n"
                         "Miner:\n"
                         "\tWhen any piece (except a Miner) strikes a Bomb, that piece is removed from the board.\n"
                         "\tException: When a Miner strikes a Bomb, it is defused and removed from the board.\n"
                         "\tThe Miner then moves onto the Bomb's space.\n"
                         "Spy:\n"
                         "\tThe Spy is rank \"S\". If any piece attacks the Spy, it is removed from the board. The Spy is\n"
                         "\talso the only piece that can capture a Marshal, if the Spy attacks the Marshal first.\n"
                         "\tIf the Marshal attacks first, then the Spy is removed.",
                         col_2_start_x,
                         col_2_start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 0.8,
                         multiline=True,
                         width=SCREEN_WIDTH,
                         font_name = "Kenney Future")
        
    def on_mouse_motion(self, x, y, dx, dy): 
        self.x = x 
        self.y = y 

    # Depending on where the rules page was called from is where it will be returned from upon clicking esc.
    def on_mouse_press(self, x, y, button, key_modifiers):
        # check if mouse click was in esc box bounds
        if x >= ESC_BOX_X1 and x <= ESC_BOX_X2 and y >= ESC_BOX_Y1 and y <= ESC_BOX_Y2:
            last_screen = self.menu_instance.get_last_screen()
            if last_screen == "menu":
                board_view = menu.Menu()
                self.window.show_view(board_view)
            else:
                board_view = esc_menu.Escape(self)
                self.window.show_view(board_view)

    # Listening for ESC key to open esc menu
    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.Q):
            global Quit
            Quit = True
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Rules.last_screen

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen