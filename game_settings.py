import arcade
import arcade.gui
import gameboard
import Opponent_AI

# initialize formatting details
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

#The Opponent Class displays 2 buttons: play_button and play_bot_button. 
#If the user selects the play button, they will be taken to the Gameplay page.
#If the user selects the play_bot_button they will be taken to the Difficulty page
class Opponent(arcade.View):
    def on_show_view(self):

        arcade.set_background_color(arcade.color.GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()
        
        #Intiialize Buttons
        play_button = arcade.gui.UIFlatButton(text="Pass And Play", width=200)
        self.v_box.add(play_button.with_space_around(bottom=20))
        play_bot_button = arcade.gui.UIFlatButton(text="Play Computer", width=200)
        self.v_box.add(play_bot_button.with_space_around(bottom=20))

        play_bot_button.on_click = self.on_click_bot
        play_button.on_click = self.on_click_play

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    #Function called when bot_button is clicked
    #Takes user to Difficulty screen
    def on_click_bot(self, event):
        #SET MODE TO PLAY AGAINST COMPUTER (FUTURE)
        Opponent_AI.generateBot()
        self.manager.disable()
        self.window.show_view(Difficulty())
    
    #Function called when play_buton is clicked
    #Takes user to Gameplay screen
    def on_click_play(self, event):
        #SET MODE TO PASS AND PLAY (FUTURE)
        
        self.manager.disable()
        self.window.show_view(Gameplay())
    
    #On draw will create all of our assets onto the screen
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()

#The Difficulty class displays 3 buttons: easy_button, medium_button, and hard_button
#Each button will take the user to the Gameplay page 
#Different buttons will affect the difficulty of the computer in future iterations
class Difficulty(arcade.View):
    def on_show_view(self):
        
        arcade.set_background_color(arcade.color.GRAY)
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()
        #Initialize Buttons
        easy_button = arcade.gui.UIFlatButton(text="EASY", width=200)
        self.v_box.add(easy_button.with_space_around(bottom=20))
        medium_button = arcade.gui.UIFlatButton(text="MEDIUM", width=200)
        self.v_box.add(medium_button.with_space_around(bottom=20))
        hard_button = arcade.gui.UIFlatButton(text="HARD", width=200)
        self.v_box.add(hard_button.with_space_around(bottom=20))
        
        easy_button.on_click = self.on_click_easy
        medium_button.on_click = self.on_click_medium
        hard_button.on_click = self.on_click_hard
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    #Called when easy_button is clicked
    def on_click_easy(self, event):
        #SET DIFFICULTY OF BOT TO EASY (FOR FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(Gameplay())
    
    #Called when medium_button is clicked    
    def on_click_medium(self, event):
        #SET DIFFICULTY OF BOT TO MEDIUM (FOR FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(Gameplay())
    
    #Called when hard_button is clicked 
    def on_click_hard(self, event):
        #SET DIFFICULTY OF BOT TO HARD (FOR FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(Gameplay())


        
        
    #On draw will create all of our assets onto the screen
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()  

#The Gameplay class has 2 butons reveal_button and hide_button
#Each button will take the user to the Gameplay page 
#Different buttons will affect the games rules in future iterations
class Gameplay(arcade.View):
    def on_show_view(self):
        
        arcade.set_background_color(arcade.color.GRAY)
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()
        
        reveal_button = arcade.gui.UIFlatButton(text="REVEAL DEFENDING PEICES", width=300)
        self.v_box.add(reveal_button.with_space_around(bottom=20))
        hide_button = arcade.gui.UIFlatButton(text="HIDE DEFENDING PEICES", width=300)
        self.v_box.add(hide_button.with_space_around(bottom=20))
        
        
        reveal_button.on_click = self.on_click_reveal
        hide_button.on_click = self.on_click_hide
        
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    
    #Called when reveal_button is pressed 
    def on_click_reveal(self, event):
        #CHANGE SETTING SO THAT DEFENDING PEICES ARE NOT REVEALED (FUTURE)
        
        self.window.show_view(gameboard.Gameboard())
    
    #Called when hide_button is pressed    
    def on_click_hide(self, event):
        #CHANGE SETTING SO THAT DEFENDING PEICES ARE REVEALED (FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(gameboard.Gameboard())
      
    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()




        

    