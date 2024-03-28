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

# BOARD CONSTANTS
ROW_COUNT = 10
COLUMN_COUNT = 10
BOARD_RIGHT = 250
BOARD_LEFT = 200
BOARD_BOTTOM = 100
BOARD_TOP = 150
BOARD_MARGIN = 50

# GRID CONSTANTS
GRID_LEFT = 200
GRID_RIGHT = 700
GRID_BOTTOM = 100
GRID_TOP = 600
CELL_WIDTH = 50


# GRAVEYARD CONSTANTS
GRAVEYARD_1_LEFT = 0
GRAVEYARD_1_RIGHT = 200
GRAVEYARD_2_LEFT = 700
GRAVEYARD_2_RIGHT = 900
GRAVEYARD_BOTTOM = 100
GRAVEYARD_TOP = 600

#LAKE FORMATTING
LAKE2_LEFT = 500
LAKE2_RIGHT = 600
LAKE1_LEFT = 300
LAKE1_RIGHT = 400
LAKE_BOTTOM = 300
LAKE_TOP = 400

p1_tester_piece1 = Piece.Piece("Sct", 2, 0, 0, 1)
p1_tester_piece2 = Piece.Piece("Msh", 2, 2, 0, 1)
p1_tester_piece3 = Piece.Piece("Gen", 10, 4, 0, 1)
p1_tester_piece4 = Piece.Piece("Bom", 12, 6, 0, 1)
p1_tester_piece5 = Piece.Piece("Flg", 0, 8, 0, 1)

p2_tester_piece1 = Piece.Piece("Sct", 2, 0, 9, 2)
p2_tester_piece2 = Piece.Piece("Msh", 2, 2, 9, 2)
p2_tester_piece3 = Piece.Piece("Gen", 10, 4, 9, 3)
p2_tester_piece4 = Piece.Piece("Bom", 12, 6, 9, 2)
p2_tester_piece5 = Piece.Piece("Flg", 0, 8, 9, 2)

p1_pieces = [p1_tester_piece1, p1_tester_piece2, p1_tester_piece3, p1_tester_piece4, p1_tester_piece5]
p2_pieces = [p2_tester_piece1, p2_tester_piece2, p2_tester_piece3, p2_tester_piece4, p2_tester_piece5]
total_pieces = p1_pieces + p2_pieces

# The gameboard class is where the user will engage in gameplay. They can exit via the ESC key and button.  
# To pass turn, the user must double click the board. 
class Gameboard(arcade.View):
    last_screen = "game_board"

    def __init__(self):
        super().__init__()

        # array backed grid
        self.grid = []
        for row in range(10):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)  # Append a cell

    click_counter = 0
    second_piece_select = False
    selected = None

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
        
        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = 200 + (50) * column + 50 // 2
                y = 100 + (50) * row + 50 // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, 50, 50, arcade.color.AFRICAN_VIOLET)
                arcade.draw_rectangle_outline(x, y, 50, 50, arcade.color.BLACK, 2)
        
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
        arcade.draw_polygon_filled(yard1, arcade.color.DARK_TAUPE)
        arcade.draw_polygon_outline(yard1, arcade.color.BLACK,8)
        
        yard2 = ((GRAVEYARD_2_LEFT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_2_RIGHT, GRAVEYARD_BOTTOM),
                 (GRAVEYARD_2_RIGHT, GRAVEYARD_TOP),
                 (GRAVEYARD_2_LEFT, GRAVEYARD_TOP),)
        arcade.draw_polygon_filled(yard2, arcade.color.DARK_TAUPE)
        arcade.draw_polygon_outline(yard2, arcade.color.BLACK,8)


    #ADD COMMENTS?
           

    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=798 and x<=882 and y<= 665 and y>= 615:
            board_view = esc_menu.Escape(self)
            self.window.show_view(board_view)
            esc_menu.Escape.last_screen = Gameboard.last_screen
        else:   
            # Gameboard.click_counter = Gameboard.click_counter + 1
            # print(Gameboard.click_counter)
            # if Gameboard.click_counter == 2:
            #     Gameboard.click_counter = 0
            #     view = pass_turn.Pass_Turn()
            #     self.window.show_view(view)
                
            click = [x,y]
            # we need to have an array of all the pieces on the board
            for piece in total_pieces:
                if draw_piece.select_piece(piece, click) == True and Gameboard.second_piece_select == False:
                    Gameboard.second_piece_select = True
                    print(piece.getType() + " selected")
                    Gameboard.selected = piece
                    # draw_piece.show_available_moves(Gameboard.selected)

            if Gameboard.selected != None and Gameboard.second_piece_select == True:
                other_selection = draw_piece.is_move_available(total_pieces, Gameboard.selected, click)
                # if valid move and the other selection is not a piece, move piece
                if (other_selection[0] and other_selection[1] == None):
                    draw_piece.select_move(Gameboard.selected, click)
                    Gameboard.second_piece_select = False
                    Gameboard.selected = None
                # if valid move and other selection is a piece, check capture condition 
                if (other_selection[0] and other_selection[1] != None):
                    print("COMBAT185")
                    print(piece)
                    print(other_selection[1])
                    draw_piece.combat(piece, other_selection[1], click)
                    Gameboard.second_piece_select = False
            else:
                Gameboard.second_piece_select = False



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
    
def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "title")
    menu_view = Gameboard()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()