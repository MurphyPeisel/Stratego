import arcade
import esc_menu
import pass_turn
from Piece import * 

# initialize formatting details
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20
ROW_COUNT = 10
COLUMN_COUNT = 10
BOARD_RIGHT = 250
BOARD_LEFT = 200
BOARD_BOTTOM = 100
BOARD_TOP = 150
BOARD_MARGIN = 50

# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    last_screen = "game_board"
    
    click_counter = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AVOCADO)
        self.clear()

    # This method draws our assets including constructing a grid
    def on_draw(self):
        arcade.start_render()

        # initialize formatting details
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5

        # Shape for esc button
        arcade.draw_rectangle_filled(840,640,84,50,
                                     arcade.color.GRANNY_SMITH_APPLE)
        # Text for esc button
        arcade.draw_text("ESC",
                         start_x + (SCREEN_WIDTH *.9),
                         start_y,
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE,
                         font_name="Kenney Future")
        
        # This is the Grid layout
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
    
        
        Gameboard.draw_cell(x, y)


    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        else:
            Gameboard.click_counter = Gameboard.click_counter + 1
            print(Gameboard.click_counter)

            # Convert the clicked mouse position into grid coordinates
            if x >= 200 and x <= 700 and y >= 100 and y <= 600:   
                row = int((abs(600 - y)) // (50)) + 1 # add 1 to make 1-index
                column = int((abs(x - 200)) // (50)) + 1 # add 1 to make 1-index
                print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

            if Gameboard.click_counter == 2:
                Gameboard.click_counter = 0
                view = pass_turn.Pass_Turn()
                self.window.show_view(view)
    
    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

    def draw_cell(x, y):
        arcade.draw_lrtb_rectangle_filled(200+50*(x-1), 200+100*(x-1), 600-50*(y-1), 600-100*(y-1), arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_outline(200+50*(x-1), 200+100*(x-1), 600-50*(y-1), 600-100*(y-1), arcade.color.BLACK, 4)
        


    @classmethod
    def get_last_screen(cls):
        return cls.last_screen