import arcade
import arcade.gui

import esc_menu
import gameboard
import rules

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

Screen = "m"
Quit = False


class Menu(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None
       
        
       
        
        


    def setup(self):
        

        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        arcade.start_render()
 

        """
        Render the screen.
        """


        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.

        # Call draw() on all your sprite lists below

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_rectangle_filled(160,160,275,100,
                                     arcade.color.GRANNY_SMITH_APPLE)
        arcade.draw_rectangle_filled(160,300,275,100,
                                     arcade.color.FRENCH_WINE)
        arcade.draw_rectangle_filled(160,440,275,100,
                                     arcade.color.LIGHT_STEEL_BLUE)
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
        
    #called when mouse moves   
    def on_mouse_motion(self, x, y, dx, dy): 
        self.x = x 
        self.y = y  
    #called when mouse is pressed
    def on_mouse_press(self, x, y, button, key_modifiers):
        global Screen

        if x>=23 and x<=298 and y<= 540 and y>= 340:
            board_view = gameboard.Gameboard()
            self.window.show_view(board_view)
        if x>=23 and x<=298 and y<= 350 and y>= 250:
            rules_view = rules.Rules()
            self.window.show_view(rules_view)
        if x>=23 and x<=298 and y<= 210 and y>= 110:
            arcade.exit()
    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.Q):
            global Quit
            Quit = True
        if(key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape()
            self.window.show_view(board_view)
            
    
            
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
    def get_quit():
        return Quit
        