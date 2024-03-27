import arcade
import esc_menu
import pass_turn
import Piece
import draw_piece

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
tester_piece1 = Piece.Piece("Sct", 2, 0, 0)
tester_piece2 = Piece.Piece("Sct", 2, 2, 0)
total_pieces = [tester_piece1, tester_piece2]

# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    last_screen = "game_board"
    
    click_counter = 0
    selected = None

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


        #draw it
        for piece in total_pieces:
            draw_piece.draw(piece)

    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        else:
            click = [x,y]
            # we need to have an array of all the pieces on the board
            for piece in total_pieces:
                if draw_piece.select_piece(piece, click) == True:
                    print(piece.getType() + " selected")
                    Gameboard.selected = piece

            if Gameboard.selected != None:
                if (draw_piece.is_move_available(total_pieces, Gameboard.selected, click)):
                    draw_piece.select_move(Gameboard.selected, click)
                    Gameboard.selected = None

            # Gameboard.click_counter = Gameboard.click_counter + 1
            # print(Gameboard.click_counter)
            # if Gameboard.click_counter == 2:
            #     Gameboard.click_counter = 0
            #     view = pass_turn.Pass_Turn()
            #     self.window.show_view(view)
    
    def on_key_press(self, key, key_modifiers):
        if (key == arcade.key.ESCAPE):
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen