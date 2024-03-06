import arcade
import gameboard
import menu
import rules
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Starting Template"
ROW_COUNT = 10
COLUMN_COUNT = 10
BOARD_RIGHT = 250
BOARD_LEFT = 200
BOARD_BOTTOM = 100
BOARD_TOP = 150
BOARD_MARGIN = 50

def main():
    """ Main function """
    
    
    Screen = 'm'
    quit = False

    while(quit == False):

        match Screen:
            case "b":
                game = gameboard.Gameboard(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
                game.setup()
                arcade.run()
        
            case "m":
                game = menu.Menu(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
                game.setup()
                arcade.run()
                hold = Screen
                Screen = menu.Menu.get_screen()
                quit = menu.Menu.get_quit()
            case "r":
                game = rules.Rules(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
                arcade.run()
            case "q":
                quit = True
        
            
            
    
    
    
if __name__ == "__main__":
    main()