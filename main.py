import arcade
import tester
import gameboard
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
    game = tester.MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()