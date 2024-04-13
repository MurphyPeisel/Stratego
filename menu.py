import arcade
import arcade.gui 
import esc_menu
import game_settings
import rules
import pyglet

# initialize formatting details
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

# The menu class displays three possible button options that navigates you to their resepective views
# This view is what is first displayed upon running main
class Menu(arcade.View):
    last_screen = "menu"
    Loop = 0
    sound = arcade.load_sound("Menu_Screen.wav",True)
    media_player = arcade.play_sound(sound, 4, 0)



    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

        

    # On draw will create all of our assets onto the screen
    def on_draw(self):
        arcade.start_render()
        self.clear()
        
        if(Menu.sound.is_playing(self.media_player) == False):
                self.media_player = arcade.play_sound(Menu.sound, 4, 0)

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5

        # Colored boxes "buttons"
        arcade.draw_rectangle_filled(160,160,275,100,
                                     arcade.color.GRANNY_SMITH_APPLE)
        arcade.draw_rectangle_filled(160,300,275,100,
                                     arcade.color.FRENCH_WINE)
        arcade.draw_rectangle_filled(160,440,275,100,
                                     arcade.color.LIGHT_STEEL_BLUE)
        
        # Text to communicate button purposes
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
        
    # Called when mouse is pressed, depending on the location of 
    # the mouse will direct user to selected destination
    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=23 and x<=298 and y<= 540 and y>= 340:
            settings_view = game_settings.Opponent()
            self.window.show_view(settings_view)
        if x>=23 and x<=298 and y<= 350 and y>= 250:
            rules_view = rules.Rules(self)
            self.window.show_view(rules_view)
        if x>=23 and x<=298 and y<= 210 and y>= 110:
            arcade.exit()

    # Listening for ESC menu call and opens that menu
    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.Q):
            global Quit
            Quit = True
        if(key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Menu.last_screen
    
    # Callable method to relay screen state
    @classmethod
    def get_last_screen(cls):
        return cls.last_screen

    #For later, disregard        
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
