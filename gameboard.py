import arcade
import menu
import esc_menu
import pass_turn

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20
SCREEN_TITLE = "Starting Template"
ROW_COUNT = 10
COLUMN_COUNT = 10
BOARD_RIGHT = 250
BOARD_LEFT = 200
BOARD_BOTTOM = 100
BOARD_TOP = 150
BOARD_MARGIN = 50
class Gameboard(arcade.View):
    last_screen = "game_board"
    click_counter = 0
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

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        # Call draw() on all your sprite lists below

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5

        arcade.draw_rectangle_filled(840,640,84,50,
                                     arcade.color.GRANNY_SMITH_APPLE)

        arcade.draw_text("ESC",
                         start_x + (SCREEN_WIDTH *.9),
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         font_name="Kenney Future")
        
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
            
    

    def on_mouse_press(self, x, y, button, key_modifiers):
        global Screen

        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        else:
            Gameboard.click_counter = Gameboard.click_counter + 1
            print(Gameboard.click_counter)
            if Gameboard.click_counter == 2:
                Gameboard.click_counter = 0
                view = pass_turn.Pass_Turn()
                self.window.show_view(view)
        
    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.Q):
            global Quit
            Quit = True
            print("HEHR")
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen