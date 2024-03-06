import arcade
import gameboard
import menu
import rules
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Main Window"
ROW_COUNT = 10
COLUMN_COUNT = 10
BOARD_RIGHT = 250
BOARD_LEFT = 200
BOARD_BOTTOM = 100
BOARD_TOP = 150
BOARD_MARGIN = 50

class iview(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.RED)
    
    def on_draw(self):
        arcade.start_render()
        

def main():
    """ Main function """
    Screen = 'm'
    quit = False
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = menu.Menu() 
    window.show_view(menu_view)
    arcade.run()


    board_view = gameboard.Gameboard()
    rules_view = rules.Rules()
    

"""

    while(quit == False):
    
        match Screen:
                case "b":
                    window.show_view(board_view)
                    arcade.run()

                case "m":
                    window.show_view(menu_view)
                    Screen = menu.Menu.get_screen()
                    arcade.run()
                case 'r': 
                    window.show_view(rules_view)
                    arcade.run()
                    
                case 'q':
                    quit = True
    
       """ 
    
        
    
if __name__ == "__main__":
    main()