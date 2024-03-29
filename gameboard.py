import arcade
import esc_menu
import pass_turn
import win

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

GRAVEYARD_1_LEFT = 25
GRAVEYARD_1_RIGHT = 175

GRAVEYARD_2_LEFT = 725
GRAVEYARD_2_RIGHT = 875

GRAVEYARD_BOTTOM = 100
GRAVEYARD_TOP = 600

#LAKE FORMATTING
LAKE2_LEFT = 500
LAKE2_RIGHT = 600
LAKE1_LEFT = 300
LAKE1_RIGHT = 400
LAKE_BOTTOM = 300
LAKE_TOP = 400

# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    last_screen = "game_board"
    
    player_turn = 2
    click_counter = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AVOCADO)
        #AVOCADO
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
        
        #FILL IN BOARD WITH BACKGROUND COLOR
        Board = ((200, 100),
                 (700, 100),
                 (700, 600),
                 (200, 600),)
        arcade.draw_polygon_filled(Board, arcade.color.BUFF)
        
        #DRAW BOARD OUTLINE
        arcade.draw_polygon_outline(Board, arcade.color.BLACK,8)
        
        #DRAW OUTLINES OF SPACES ON BOARD 
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
        
        #DRAW LEFT LAKE
        Lake1 = ((LAKE1_LEFT, LAKE_BOTTOM),
                 (LAKE1_RIGHT, LAKE_BOTTOM),
                 (LAKE1_RIGHT, LAKE_TOP),
                 (LAKE1_LEFT, LAKE_TOP),)
        arcade.draw_polygon_filled(Lake1, arcade.color.BLUEBERRY)
        arcade.draw_polygon_outline(Lake1, arcade.color.BLACK,4)
        #DRAW RIGHT LAKE
        Lake2 = ((LAKE2_LEFT, LAKE_BOTTOM),
                 (LAKE2_RIGHT, LAKE_BOTTOM),
                 (LAKE2_RIGHT, LAKE_TOP),
                 (LAKE2_LEFT, LAKE_TOP),)
        arcade.draw_polygon_filled(Lake2, arcade.color.BLUEBERRY)
        arcade.draw_polygon_outline(Lake2, arcade.color.BLACK,4)
        
        yard1 = ((GRAVEYARD_1_LEFT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_1_RIGHT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_1_RIGHT, GRAVEYARD_TOP),
                 (GRAVEYARD_1_LEFT, GRAVEYARD_TOP),)
        arcade.draw_polygon_filled(yard1, arcade.color.BLACK_OLIVE)
        arcade.draw_polygon_outline(yard1, arcade.color.BLACK,8)
        
        yard2 = ((GRAVEYARD_2_LEFT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_2_RIGHT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_2_RIGHT, GRAVEYARD_TOP),
                 (GRAVEYARD_2_LEFT, GRAVEYARD_TOP),)
        arcade.draw_polygon_filled(yard2, arcade.color.BLACK_OLIVE)
        arcade.draw_polygon_outline(yard2, arcade.color.BLACK,8)

    #ADD COMMENTS?
           
    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = win.Win()
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        else:
            Gameboard.click_counter = Gameboard.click_counter + 1
            print(Gameboard.click_counter)
            if Gameboard.click_counter == 2:
                Gameboard.click_counter = 0
                Gameboard.player_ready()
                view = pass_turn.Pass_Turn()
                self.window.show_view(view)
    
    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

    def player_ready():
        if Gameboard.player_turn == 1:
            Gameboard.player_turn = 2
        else:
            Gameboard.player_turn = 1
    
    def get_turn():
        return Gameboard.player_turn

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen
    
def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "title")
    menu_view = Gameboard()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()