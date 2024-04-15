# import packages
import arcade
import arcade.gui
import gameboard

# Define constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

default_style = {
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": arcade.color.BLACK,
            "bg_color": arcade.color.GRAY_ASPARAGUS,
            "font_name": "Kenney Future",

            # used if button is pressed
            "bg_color_pressed": arcade.color.WHITE,
            "border_color_pressed": arcade.color.WHITE,  # also used when hovered
            "font_color_pressed": arcade.color.BLACK,
        }

# Creates a class to define the look for when the game is switching between each player. This way in two player mode,
# each player cannot see the others board by accident
class Pass_Turn(arcade.View):

    player_turn = 1

    def on_show_view(self):

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Buttons
        self.v_box = arcade.gui.UIBoxLayout()
        player_switch_button = arcade.gui.UIFlatButton(text="Ready", width=200, style= default_style)
        self.v_box.add(player_switch_button.with_space_around(top=50))
        player_switch_button.on_click = self.on_click_switch

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    # This function adds the functionality to the switch player button so that it returns to the board when the user
    # presses the button
    def on_click_switch(self, event):
        self.manager.disable()
        board_view = gameboard.Gameboard()
        self.window.show_view(board_view)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()
        # Background Image
        img = arcade.load_texture('SettingsMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)
        img = arcade.load_texture('SmallMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.485, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 
        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text(" Player " + str(Pass_Turn.player_turn) + "\nReady?",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .265),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * 1.3,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
        
    # The functions below deal with the manegment of the player_turn Variable: 
    # Toggle, View Shift, getter
    def change_turn():
        if Pass_Turn.player_turn == 1:
            Pass_Turn.player_turn = 2
        else:
            Pass_Turn.player_turn = 1

    def turn_screen(self):
        Pass_Turn.change_turn()
        view = Pass_Turn()
        self.window.show_view(view)
    
    def get_turn():
        return Pass_Turn.player_turn