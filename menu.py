import arcade
import arcade.gui 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

SCREEN_TITLE = "Drawing Text Example"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

Screen = "m"


class Menu(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None
       
        
       
        
        


    def setup(self):
        

        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        

        """
        Render the screen.
        """

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text("Text Drawing Examples",
                         start_x,
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 2,
                         width=SCREEN_WIDTH,
                         align="center")

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text("Stratego",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .1),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 4,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")

        arcade.draw_text("Play",
                         start_x + (SCREEN_WIDTH *.05),
                         start_y - (SCREEN_HEIGHT *.3),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 2,
                         font_name="Kenney Future")
        
        arcade.draw_text("Rules",
                         start_x + (SCREEN_WIDTH * .05),
                         start_y - (SCREEN_HEIGHT * .5),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 2,
                         font_name="Kenney Future")
        
        arcade.draw_text("Quit",
                         start_x + (SCREEN_WIDTH * .05),
                         start_y - (SCREEN_HEIGHT * .7),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 2,
                         font_name="Kenney Future")
        
    def on_mouse_motion(self, x, y, dx, dy): 
        """ 
        Called whenever the mouse moves. 
        """
        self.x = x 
        self.y = y  
    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=23 and x<=298 and y<= 540 and y>= 340:
            global Screen
            Screen = 'b'
            arcade.close_window()
        #RULES
        #center (160,300)
        
        #PLAY
        #center (160,440)
        #width 275
        #100
        
        #QUIT
        #center (160,160)
        #width 275
        #height 100
        
        
    def get_screen():
        return Screen
        