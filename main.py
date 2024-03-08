import arcade
import menu

# initialize formatting details
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Main Window"        

def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = menu.Menu()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()