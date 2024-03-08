import arcade
import arcade.gui
import gameboard
import menu
import rules

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class Escape(arcade.View):
    def __init__(self, menu_instance):
        super().__init__()
        self.menu_instance = menu_instance
    last_screen = "menu"
    def on_show_view(self):

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
        self.manager.disable()
        board_view = menu.Menu()
        self.window.show_view(board_view)

    def on_click_cancel(self, event):
        print("cancel button pressed")
        self.manager.disable()
        last_screen = self.menu_instance.get_last_screen()
        if last_screen == "menu":
            board_view = menu.Menu()
            self.window.show_view(board_view)
        elif last_screen == "game_board":
            board_view = gameboard.Gameboard()
            self.window.show_view(board_view)
        elif last_screen == "rules":
            board_view = rules.Rules()
            self.window.show_view(board_view)
        elif last_screen == "exit":
            board_view = arcade.exit()
            self.window.show_view(board_view)

    def on_click_exit(self, event):
        print("exit button clicked")
        self.manager.disable()
        arcade.exit()


    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        arcade.start_render()
        self.manager.draw()

    def on_buttonclick(self, event):
        print("button is clicked")