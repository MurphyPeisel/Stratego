import arcade
import arcade.gui
import rules
import gameboard
import pass_turn
import menu
import rules
import win
import Piece
import menu as mn

# initialize formatting details
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

# A class to define the view and buttons for the escape menu which is pulled up whenever a user presses the escape
# button
class Escape(arcade.View):
    win_view = "view"
    gameboard_view = "view"
    last_screen = "esc_menu"
    
    def __init__(self, menu_instance):
        super().__init__()
        self.menu_instance = menu_instance

    # Defines the view of the window when open
    def on_show_view(self):

        arcade.set_background_color(arcade.color.GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        # Button formatting
        resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)
        self.v_box.add(resume_button.with_space_around(bottom=20))
        rules_button = arcade.gui.UIFlatButton(text="Rules", width=200)
        self.v_box.add(rules_button.with_space_around(bottom=20))
        back_to_menu_button = arcade.gui.UIFlatButton(text="Return to Menu", width=200)
        self.v_box.add(back_to_menu_button.with_space_around(bottom=20))
        resign_button = arcade.gui.UIFlatButton(text="Resign", width=200)
        self.v_box.add(resign_button.with_space_around(bottom=20))
        exit_button = arcade.gui.UIFlatButton(text="Exit Program", width=200)
        self.v_box.add(exit_button.with_space_around(bottom=20))
        
        resume_button.on_click = self.on_click_resume
        rules_button.on_click = self.on_click_rules
        back_to_menu_button.on_click = self.on_click_back
        resign_button.on_click = self.on_click_resign
        exit_button.on_click = self.on_click_exit

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    # Functionality for when the user presses the resume button
    # This function unlike the others needs to get a hold of the previous screen displayed in order to return the user
    # to it when pressed. That is why there get_last_screen was added to other classes. This function will return the
    # user to the last screen they were on.
    def on_click_resume(self, event):
        self.manager.disable()
        last_screen = self.menu_instance.get_last_screen()
        if last_screen == "menu":
            board_view = mn.Menu()
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

    # This method opens the rules screen which will return to the esc menu when called from there.
    def on_click_rules(self, event):
        self.manager.disable()
        board_view = rules.Rules(self)
        self.window.show_view(board_view)
        rules.Rules.last_screen = Escape.last_screen

    # Functionality for when the user presses the back to menu button to change the screen back to the menu screen
    def on_click_back(self, event):
        self.manager.disable()
        
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
        gameboard.Gameboard.text_index = 0
        gameboard.Gameboard.text = [""]

        

        gameboard.Gameboard.total_pieces = gameboard.Gameboard.army1 + gameboard.Gameboard.army2
        board_view = mn.Menu()
        #   Stop playing sound from gameboard
        if gameboard.Gameboard.sound.is_playing(gameboard.Gameboard.media_player) or gameboard.Gameboard.playing == True:
                gameboard.Gameboard.sound.stop(gameboard.Gameboard.media_player)
                gameboard.Gameboard.playing = False
                print("stopped gameboard music")
        self.window.show_view(board_view)
    
    def on_click_resign(self, event):
        self.manager.disable()
        gameboard.Gameboard.set_is_menu(gameboard.Gameboard, True)
        self.manager.disable()
        print("test")
        if gameboard.Gameboard.player_turn == 1:
            gameboard.Gameboard.player_turn = 2
        else:
            gameboard.Gameboard.player_turn = 1
        #RESET GAME 
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
        gameboard.Gameboard.text_index = 0
        gameboard.Gameboard.text = [""]
        win_view = win.Win()
        # stop playing sound from gameboard
        if gameboard.Gameboard.sound.is_playing(gameboard.Gameboard.media_player) or gameboard.Gameboard.playing == True:
                gameboard.Gameboard.sound.stop(gameboard.Gameboard.media_player)
                gameboard.Gameboard.playing = False
                print("stopped gameboard music")
        self.window.show_view(win_view)


    # This function closes the program when the user hits the exit button
    def on_click_exit(self, event):
        self.manager.disable()
        arcade.exit()

    @classmethod
    def get_last_screen(cls):
        return cls.last_screen
    
    # This function draws the window when called
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()
