import arcade
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Starting Template"
ROW_COUNT = 10
COLUMN_COUNT = 10
BOARD_RIGHT = 250
BOARD_LEFT = 200
BOARD_BOTTOM = 100
BOARD_TOP = 150
BOARD_MARGIN = 50
class Gameboard(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AVOCADO)
        self.clear()

        # Call draw() on all your sprite lists below

        
        

    def on_draw(self):
        arcade.start_render()
        """
        Render the screen.
        
        """
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

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        


        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass



    

