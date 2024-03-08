# import packages
import arcade
import arcade.gui
import gameboard

# Define constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


# Creates a class to define the look for when the game is switching between each player. This way in two player mode,
# each player cannot see the others board by accident
class Pass_Turn(arcade.View):

    # This function Defines what the window will look like when called
    def on_show_view(self):

        arcade.set_background_color(arcade.color.GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()


        player_switch_button = arcade.gui.UIFlatButton(text="Ready", width=200)
        self.v_box.add(player_switch_button.with_space_around(bottom=150))

        player_switch_button.on_click = self.on_click_switch


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )

    # This function adds the functionality to the switch player button so that it returns to the board when the user
    # presses the button
    def on_click_switch(self, event):
        self.manager.disable()
        board_view = gameboard.Gameboard()
        self.window.show_view(board_view)

    # This function draws all that is defined in show view to allow the window to appear. it also adds text that exists
    # outside the buttons / manager so that the users are given context for what they are doing.
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text("Next Player Ready?",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .1),
                         arcade.color.BLACK,
                         DEFAULT_FONT_SIZE * 4,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
