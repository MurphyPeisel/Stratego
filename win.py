# import packages
import arcade
import arcade.gui
import menu
import gameboard
import game_settings


# Define constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


# Creates a class to define the look for when the game is switching between each player. This way in two player mode,
# each player cannot see the others board by accident
class Win(arcade.View):

    # This function Defines what the window will look like when called
    def on_show_view(self):

        arcade.set_background_color(arcade.color.YELLOW_ROSE)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        replay_button = arcade.gui.UIFlatButton(text="Replay", width=200)
        self.v_box.add(replay_button.with_space_around(bottom=50))

        game_settings_button = arcade.gui.UIFlatButton(text="Game Settings", width=200)
        self.v_box.add(game_settings_button.with_space_around(bottom=50))

        exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)
        self.v_box.add(exit_button.with_space_around(bottom=50))

        replay_button.on_click = self.on_replay_click
        game_settings_button.on_click = self.on_game_settings_click
        exit_button.on_click = self.on_exit_click


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )

    # This function adds the functionality to the switch player button so that it returns to the board when the user
    # presses the button
    def on_replay_click(self, event):
        self.manager.disable()
        board_view = gameboard.Gameboard()
        self.window.show_view(board_view)

    def on_game_settings_click(self, event):
        self.manager.disable()
        board_view = game_settings.Opponent()
        self.window.show_view(board_view)

    def on_exit_click(self, event):
        self.manager.disable()
        board_view = menu.Menu()
        self.window.show_view(board_view)
    

    # This function draws all that is defined in show view to allow the window to appear. it also adds text that exists
    # outside the buttons / manager so that the users are given context for what they are doing.
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text("Player " + str(gameboard.Gameboard.get_turn()) + "\nWins",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .1),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 4,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "title")
    menu_view = Win()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()