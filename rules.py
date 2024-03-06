"""
Example showing how to draw text to the screen.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_text
"""
import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Drawing Text Example"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


class MyGame(arcade.Window):
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
        arcade.draw_text("Text Drawing Examples",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 2,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")

        # start_x and start_y make the start point for the text. We draw a dot to make it
        # easy too see the text in relation to its start x and y.
        start_x = 10
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3
        arcade.draw_text("Fonts:",
                         start_x,
                         start_y,
                         arcade.color.FRENCH_WINE,
                         DEFAULT_FONT_SIZE, bold=True)


        start_y -= DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text("The object of the game is to capture the enemy Flag. "
                         "As the commander of an army you are in charge of 33 movable "
                         "units of differing rank and 7 immovable pieces.",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         multiline=True,
                         width=800)
        
        start_y -= DEFAULT_LINE_HEIGHT * 3
        arcade.draw_text("MOVABLE PIECES:\n"
                         "----------------\n"
                         "Rank - Name (Quantity)\n"
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

        # # --- Column 2 ---
        # start_x = 750
        # start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3
        # arcade.draw_text("Text Positioning:",
        #                  start_x,
        #                  start_y,
        #                  arcade.color.FRENCH_WINE,
        #                  DEFAULT_FONT_SIZE,
        #                  bold=True)

        # # start_x and start_y make the start point for the text.
        # # We draw a dot to make it easy too see the text in relation to
        # # its start x and y.
        # start_y -= DEFAULT_LINE_HEIGHT
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("Default of 'baseline' and 'Left'",
        #                  start_x,
        #                  start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE)

        # start_y -= DEFAULT_LINE_HEIGHT
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("'bottom' and 'left'",
        #                  start_x,
        #                  start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE,
        #                  anchor_x="left",
        #                  anchor_y="bottom")

        # start_y -= DEFAULT_LINE_HEIGHT
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("'top' and 'left'",
        #                  start_x, start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE,
        #                  anchor_x="left",
        #                  anchor_y="top")

        # start_y -= DEFAULT_LINE_HEIGHT * 2
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("'baseline' and 'center'",
        #                  start_x, start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE,
        #                  anchor_x="center",
        #                  anchor_y="baseline")

        # start_y -= DEFAULT_LINE_HEIGHT
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("'baseline' and 'right'",
        #                  start_x,
        #                  start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE,
        #                  anchor_x="right",
        #                  anchor_y="baseline")

        # start_y -= DEFAULT_LINE_HEIGHT
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("'center' and 'center'",
        #                  start_x,
        #                  start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE,
        #                  anchor_x="center",
        #                  anchor_y="center")

        # start_y -= DEFAULT_LINE_HEIGHT * 4
        # # start_x = 0
        # # start_y = 0
        # arcade.draw_point(start_x, start_y, arcade.color.BARN_RED, 5)
        # arcade.draw_text("Rotating Text",
        #                  start_x, start_y,
        #                  arcade.color.BLACK,
        #                  DEFAULT_FONT_SIZE,
        #                  anchor_x="center",
        #                  anchor_y="center",
        #                  rotation=self.text_angle)


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()