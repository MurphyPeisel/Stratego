import arcade
import arcade.gui
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
SCREEN_TITLE = "Starting Template"

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()
class Escape(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        back_to_menu_button = arcade.gui.UIFlatButton(text="Back to menu", width=200)
        self.v_box.add(back_to_menu_button.with_space_around(bottom=20))
        cancel_button = arcade.gui.UIFlatButton(text="Cancel", width=200)
        self.v_box.add(cancel_button.with_space_around(bottom=20))
        exit_button = arcade.gui.UIFlatButton(text="Exit Program", width=200)
        self.v_box.add(exit_button.with_space_around(bottom=20))

        back_to_menu_button.on_click = self.on_click_back
        cancel_button.on_click = self.on_click_cancel
        exit_button.on_click = self.on_click_exit

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_back(self, event):
        print("back to menu pressed")

    def on_click_cancel(self, event):
        print("cancel button pressed")

    def on_click_exit(self, event):
        print("exit button clicked")


    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        arcade.start_render()
        self.manager.draw()
        #changes

    def on_buttonclick(selfself, event):
        print("button is clicked")
def main():
    """ Main function """
    game = Escape(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()