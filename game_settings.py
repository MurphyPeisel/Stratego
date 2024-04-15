import arcade
import arcade.gui
import gameboard
import Opponent_AI
import menu
import time
from arcade.experimental.uislider import UISlider
from arcade.gui import UIManager, UIAnchorWidget, UILabel
from arcade.gui.events import UIOnChangeEvent

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

# Game Settings Creates a view that allows the user to select between 2 player and computer settings
class Game_Settings(arcade.View):

    mode = ""

    # This function Defines what the window will look like when called
    def on_show_view(self):

        self.manager = arcade.gui.UIManager()
        self.manager.enable() 

        self.v_box = arcade.gui.UIBoxLayout()

        play_button = arcade.gui.UIFlatButton(text="2 Players", width=200, style= default_style)
        self.v_box.add(play_button.with_space_around(top= 90,bottom=20))
        play_bot_button = arcade.gui.UIFlatButton(text="Computer", width=200, style= default_style)
        self.v_box.add(play_bot_button.with_space_around(bottom=20))
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=150, style= default_style)
        self.v_box.add(quit_button.with_space_around(top=10, bottom=20))

        play_bot_button.on_click = self.on_click_bot
        play_button.on_click = self.on_click_play
        quit_button.on_click = self.on_quit_click


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    # Opens Computer Settings Menu
    def on_click_bot(self, event):
        mode = "comp"
        self.manager.disable()
        self.window.show_view(Computer())
        
    
    #Function called when play_buton is clicked
    def on_click_play(self, event):
        mode = "2play"
        self.manager.disable()
        self.window.show_view(Players2())

    def on_quit_click(self, event):
        self.manager.disable()
        board_view = menu.Menu()
        self.window.show_view(board_view)
    

    # This function draws all that is defined in show view to allow the window to appear. The text will show who won
    def on_draw(self):
        self.clear()
        arcade.start_render()
        img = arcade.load_texture('SettingsMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)
        img = arcade.load_texture('SmallMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.485, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 
        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        #img = arcade.load_texture('SettingsMenu.png')
        #arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 
        arcade.draw_text(" Game Settings",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .265),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * 1.2,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
              
# The Computer view shows the user settings to play against computer opponents
# User can toggle sight on defender pieces and can also set the difficulty
class Computer(arcade.View):

    difficulty = "Medium"
    vision = " -Toggle Seeing Defender Pieces-"
    sight = True

    def on_show_view(self):

        self.manager = arcade.gui.UIManager()
        self.manager.enable()               

        self.v_box = arcade.gui.UIBoxLayout()
        
        #Initialize Start Button
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style= default_style)
        self.v_box.add(start_button.with_space_around(top= 260))
        start_button.on_click = self.on_click_start        

        ui_slider = UISlider(value=50, width=200, height=50)
        @ui_slider.event()
        def on_change(event: UIOnChangeEvent):
            ui_slider.value = ui_slider.value
            if ui_slider.value < 33:
                Computer.difficulty = "Easy"
            elif ui_slider.value < 66:
                Computer.difficulty = "Medium"
            else:
                Computer.difficulty = "Hard"
        self.manager.add(UIAnchorWidget(child=ui_slider))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=288 and x<=628 and y<= 324 and y>= 270:
            if Computer.sight == False:
                Computer.vision = " o Show Pieces o"
                Computer.sight = True  
            else:
                Computer.vision = " * Hide Pieces *"
                Computer.sight = False  

    #Called when easy_button is clicked
    def on_click_start(self, event):
        if Computer.vision != " -Toggle Seeing Defender Pieces-":
            if Computer.difficulty == "Hard":
                Opponent_AI.bot.generate_bot(3)
            elif Computer.difficulty == "Medium":
                Opponent_AI.bot.generate_bot(2)
            else:
                Opponent_AI.bot.generate_bot(1)

            if Computer.sight == True:
                gameboard.Gameboard.set_visibility(gameboard, True)
            else:
                gameboard.Gameboard.set_visibility(gameboard, False)
            #Stop playing sound from menu
            if menu.Menu.sound.is_playing(menu.Menu.media_player) or menu.Menu.playing == True:
                menu.Menu.sound.stop(menu.Menu.media_player)
                menu.Menu.playing = False
            self.window.show_view(gameboard.Gameboard())
            gameboard.Gameboard.set_is_menu(gameboard.Gameboard, False)


    #On draw will create all of our assets onto the screen
    def on_draw(self):
        self.clear()
        arcade.start_render()
        img = arcade.load_texture('SettingsMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)
        img = arcade.load_texture('SmallMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.485, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 

        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        arcade.draw_text(" Game Settings",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .265),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * 1.2,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
        arcade.draw_text(" " + Computer.difficulty, 
                         start_x,
                         start_y - (SCREEN_HEIGHT * .35),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * .7,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
        arcade.draw_text(" " + Computer.vision, 
                         start_x,
                         start_y - (SCREEN_HEIGHT * .49),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * .7,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
        
# The Players2 Displays the options for 2 Play settings
# User Toggles between Showing Pieces or hiding them
class Players2(arcade.View):
    difficulty = "Medium"
    vision = " -Toggle Seeing Defender Pieces-"
    sight = True

    def on_show_view(self):

        self.manager = arcade.gui.UIManager()
        self.manager.enable()               

        self.v_box = arcade.gui.UIBoxLayout()
        
        #Initialize Start Button
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style= default_style)
        self.v_box.add(start_button.with_space_around(top= 260))
        start_button.on_click = self.on_click_start        

        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_mouse_press(self, x, y, button, key_modifiers):
        if x>=288 and x<=628 and y<= 324 and y>= 270:
            if Computer.sight == False:
                Computer.vision = " o Show Pieces o"
                Computer.sight = True  
            else:
                Computer.vision = " * Hide Pieces *"
                Computer.sight = False     
    
    #Called when easy_button is clicked
    def on_click_start(self, event):
        if Computer.vision != " -Toggle Seeing Defender Pieces-":
            if Computer.sight == True:
                gameboard.Gameboard.set_visibility(gameboard, True)
            else:
                gameboard.Gameboard.set_visibility(gameboard, False)
            #stop playing sound from menu
            if menu.Menu.sound.is_playing(menu.Menu.media_player) or menu.Menu.playing == True:
                menu.Menu.sound.stop(menu.Menu.media_player)
                menu.Menu.playing = False
            self.window.show_view(gameboard.Gameboard())
            gameboard.Gameboard.set_is_menu(gameboard.Gameboard, False)
   
    def on_draw(self):
        self.clear()
        arcade.start_render()
        img = arcade.load_texture('SettingsMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img)
        img = arcade.load_texture('SmallMenu.png')
        arcade.draw_texture_rectangle (SCREEN_WIDTH*.485, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 
        self.manager.draw()
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        #img = arcade.load_texture('SettingsMenu.png')
        #arcade.draw_texture_rectangle (SCREEN_WIDTH*.5, SCREEN_HEIGHT*.5, SCREEN_WIDTH, SCREEN_HEIGHT, img) 
        arcade.draw_text(" Game Settings",
                         start_x,
                         start_y - (SCREEN_HEIGHT * .265),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * 1.2,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")
        arcade.draw_text(" " + Computer.vision, 
                         start_x,
                         start_y - (SCREEN_HEIGHT * .49),
                         arcade.color.WHITE,
                         DEFAULT_FONT_SIZE * .7,
                         width=SCREEN_WIDTH,
                         align="center",
                         font_name="Kenney Future")