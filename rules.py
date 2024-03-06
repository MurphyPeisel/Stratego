"""
Example showing how to draw text to the screen.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_text
"""
import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Stratego Rules"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 18


class Rules(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background_color = arcade.color.BEIGE
        self.text_angle = 0
        self.time_elapsed = 0.0

    def on_update(self, delta_time):
        self.text_angle += 1
        self.time_elapsed += delta_time

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Add the screen title
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text("Stratego Rules",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 3,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")

        # start_x and start_y make the start point for the text. We draw a dot to make it
        # easy too see the text in relation to its start x and y.
        start_x = 50
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2.5
        arcade.draw_text("Welcome to Stratego:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE * 2, bold=True,
                         font_name = "Kenney Future")

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text("The object of the game is to capture the enemy Flag. "
                         "As the commander of an army you are in charge of 33 movable "
                         "units of differing rank and 7 immovable pieces.",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=1000,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT 
        col_2_start_y = start_y
        arcade.draw_text("MOVABLE PIECES:\n"
                         "----------------\n"
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
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=800,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT *  5.5
        arcade.draw_text("SETUP:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE * 1.5, bold=True,
                         font_name = "Kenney Future")
        
        start_y -= DEFAULT_LINE_HEIGHT * 0.5
        arcade.draw_text("Player 1 places all of their pieces on the first 4 rows of their side of the gameboard. "
                         "Then, player 2 does the same on their side of the gameboard. ",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=1000,
                         font_name = "Kenney Future")

        start_y -= DEFAULT_LINE_HEIGHT
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
                         "\t3. Pieces cannot jump over or move onto the two lake areas in the center of the gameboard.\n"
                         "\t4.  A piece cannot move back and forth between the same two squares in three consecutive turns. \n",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=1000,
                         font_name = "Kenney Future")
        # # --- Column 2 ---
        start_x = SCREEN_WIDTH / 4
        arcade.draw_text("IMMOVABLE PIECES:\n"
                         "----------------\n"
                         "Name (Quantity)\n"
                         "----------------\n"
                         "Bomb (6)\n"
                         "Flag (1)\n",
                         start_x,
                         col_2_start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=800,
                         font_name = "Kenney Future")
        
        col_2_start_y -= DEFAULT_LINE_HEIGHT * 2.5
        arcade.draw_text("NOTE:", 
                         start_x, 
                         col_2_start_y, 
                         arcade.color.FRENCH_WINE, 
                         DEFAULT_FONT_SIZE,
                         width = 50, 
                         bold = True,
                         font_name = "Kenney Future")
        
        col_2_start_y -= DEFAULT_LINE_HEIGHT * 0.5
        arcade.draw_text("Higher number indicates higher rank.\n"
                         "The lower-ranked pieces have unique privileges.",
                         start_x,
                         col_2_start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=800,
                         font_name = "Kenney Future")
def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()