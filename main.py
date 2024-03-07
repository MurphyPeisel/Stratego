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
        

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = menu.Menu() 
    window.show_view(menu_view)
    arcade.run()
    

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