# import packages
import arcade
import arcade.gui
import menu
import gameboard
import game_settings
import Piece
import pass_turn


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


# Creates a win screen that identifies the user that won the round and provides three options to move forward
# The options are to replay with the same settings, return to game settings menu and to return to main menu
class Win(arcade.View):

    level = 4
    sound = arcade.load_sound("Win.wav",False)
    media_player = arcade.play_sound(sound, level, 0, looping=True)
    sound.stop(media_player)
    playing = False

    def __init__(self, menu_instance):
        super().__init__()
        self.menu_instance = menu_instance

    # Defines the view of the window when open
    def on_show_view(self):

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        # Button formatting
        replay_button = arcade.gui.UIFlatButton(text="Replay", width=200, style= default_style)
        self.v_box.add(replay_button.with_space_around(top = 80, bottom=10))

        game_settings_button = arcade.gui.UIFlatButton(text="Game Settings", width=200, style= default_style)
        self.v_box.add(game_settings_button.with_space_around(bottom=10))

        exit_button = arcade.gui.UIFlatButton(text="Exit", width=200, style= default_style)
        self.v_box.add(exit_button.with_space_around(bottom=10))

        
        replay_button.on_click = self.on_replay_click
        game_settings_button.on_click = self.on_game_settings_click
        exit_button.on_click = self.on_exit_click
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="bottom",
                child=self.v_box)
        )

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    # Navigation on button clicks
    # On replay will reset the board and keep current settings
    def on_replay_click(self, event):
        gameboard.Gameboard.set_is_menu(gameboard.Gameboard, False)
        self.manager.disable()
        board_view = gameboard.Gameboard()
        if Win.sound.is_playing(Win.media_player) or Win.playing == True:
                Win.sound.stop(Win.media_player)
                Win.playing = False

        gameboard.Gameboard.game_state = "setup"
        lake_piece_1 = Piece.Piece("Lke", 0, 2, 4, 3)
        lake_piece_2 = Piece.Piece("Lke", 0, 3, 4, 3)
        lake_piece_3 = Piece.Piece("Lke", 0, 2, 5, 3)
        lake_piece_4 = Piece.Piece("Lke", 0, 3, 5, 3)
        lake_piece_5 = Piece.Piece("Lke", 0, 6, 4, 3)
        lake_piece_6 = Piece.Piece("Lke", 0, 7, 4, 3)
        lake_piece_7 = Piece.Piece("Lke", 0, 6, 5, 3)
        lake_piece_8 = Piece.Piece("Lke", 0, 7, 5, 3)
        #RESET GAME
        gameboard.Gameboard.game_state = "setup"
        gameboard.Gameboard.army1 = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
        gameboard.Gameboard.army2 = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
        gameboard.Gameboard.graveyard1 = Piece.initPieces(1)
        gameboard.Gameboard.graveyard2 = Piece.initPieces(2)
        gameboard.Gameboard.AI = 0
        gameboard.Gameboard.player_turn = 1
        gameboard.Gameboard.highlight_index = 0
        gameboard.Gameboard.selected = None
        gameboard.Gameboard.AttackRight = None
        gameboard.Gameboard.AttackLeft = None
        gameboard.Gameboard.AttackAbove = None
        gameboard.Gameboard.AttackBelow = None

        self.window.show_view(board_view)

    # On Game Settings will return you to the head of that line and let you reset the settings
    def on_game_settings_click(self, event):
        self.manager.disable()
        board_view = game_settings.Game_Settings()
        # stop playing sound
        if Win.sound.is_playing(Win.media_player) or Win.playing == True:
                Win.sound.stop(Win.media_player)
                Win.playing = False
                menu.Menu.media_player.seek(0)
                menu.Menu.media_player.play()
                menu.Menu.playing = True
        self.window.show_view(board_view)

    def on_exit_click(self, event):
        self.manager.disable()
        board_view = menu.Menu()
        if Win.sound.is_playing(Win.media_player) or Win.playing == True:
                Win.sound.stop(Win.media_player)
                Win.playing = False
        self.window.show_view(board_view)
 
    @classmethod
    def get_last_screen(cls):
        return cls.last_screen
    
    # This function draws the window when called
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()
        img = arcade.load_texture('SettingsMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)
        img = arcade.load_texture('SmallMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.485, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 
        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5

        arcade.draw_text(" Player " + str(pass_turn.Pass_Turn.get_turn())+ " Won!",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .265),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * 1.2,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")