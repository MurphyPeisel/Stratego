import arcade
import arcade.gui 
import esc_menu
import game_settings
import rules

# initialize formatting details
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

# The menu class displays three possible button options that navigates you to their resepective views
# This view is what is first displayed upon running main
class Menu(arcade.View):
    last_screen = "menu"
    
    #def on_show_view(self):

    # On draw will create all of our assets onto the screen
    def on_draw(self):
        arcade.start_render()
        self.clear()

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5

        #arcade.set_background_color(arcade.color.BLUE_YONDER)

        img = arcade.load_texture('MenuScreen.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)       

        # Text to communicate button purposes
        WIDTH_POSITIONING = .1
        underlay = .093
        FONT_SIZE = 2.3

        arcade.draw_text("Stratego",
                         start_x + (SCREEN_WIDTH * underlay),
                         start_y - (SCREEN_HEIGHT * .303),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         width=SCREEN_WIDTH,
                         font_name="Kenney Future")
        arcade.draw_text("Play",
                         start_x + (SCREEN_WIDTH * underlay),
                         start_y - (SCREEN_HEIGHT *.443),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         font_name="Kenney Future")
        arcade.draw_text("Rules",
                         start_x + (SCREEN_WIDTH * underlay),
                         start_y - (SCREEN_HEIGHT * .553),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         font_name="Kenney Future")
        arcade.draw_text("Quit",
                         start_x + (SCREEN_WIDTH * underlay),
                         start_y - (SCREEN_HEIGHT * .663),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         font_name="Kenney Future")

        arcade.draw_text("Stratego",
                         start_x + (SCREEN_WIDTH * WIDTH_POSITIONING),
                         start_y - (SCREEN_HEIGHT * .3),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         width=SCREEN_WIDTH,
                         font_name="Kenney Future")
        arcade.draw_text("Play",
                         start_x + (SCREEN_WIDTH * WIDTH_POSITIONING),
                         start_y - (SCREEN_HEIGHT *.44),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         font_name="Kenney Future")
        arcade.draw_text("Rules",
                         start_x + (SCREEN_WIDTH * WIDTH_POSITIONING),
                         start_y - (SCREEN_HEIGHT * .55),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         font_name="Kenney Future")
        arcade.draw_text("Quit",
                         start_x + (SCREEN_WIDTH * WIDTH_POSITIONING),
                         start_y - (SCREEN_HEIGHT * .66),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * FONT_SIZE,
                         font_name="Kenney Future")
         
    # Called when mouse is pressed, depending on the location of 
    # the mouse will direct user to selected destination
    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=77 and x<=287 and y<= 366 and y>= 323:
            settings_view = game_settings.Game_Settings()
            #settings_view = esc_menu.Escape(self)
            self.window.show_view(settings_view)
        if x>=77 and x<=287 and y<= 290 and y>= 246:
            rules_view = rules.Rules(self)
            self.window.show_view(rules_view)
        if x>=77 and x<=287 and y<= 211 and y>= 171:
            arcade.exit()

    # Listening for ESC menu call and opens that menu
    def on_key_press(self, key):
        if(key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Menu.last_screen
    
    # Callable method to relay screen state
    @classmethod
    def get_last_screen(cls):
        return cls.last_screen

    