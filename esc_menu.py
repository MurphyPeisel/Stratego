import arcade
import arcade.gui
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
SCREEN_TITLE = "Starting Template"

class escape(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GRAY)

        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        back_to_menu_button = arcade.gui.UIFlatButton(text="Back to menu", width=200)
        back_to_menu_button.on_click = self.on_buttonclick
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=back_to_menu_button)
            )
        exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)
        exit_button.on_click = self.on_buttonclick
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                child=exit_button)
        )

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        arcade.start_render()
        self.uimanager.draw()

    def on_buttonclick(selfself, event):
        print("button is clicked")
def main():
    """ Main function """
    game = escape(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()