import arcade
import arcade.gui
import gameboard
import rules

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class Opponent(arcade.View):
    def on_show_view(self):

        arcade.set_background_color(arcade.color.GRAY)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

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
    def on_click_bot(self, event):
        print("back to menu pressed")
        self.manager.disable()
        self.window.show_view(Difficulty())
    def on_click_play(self, event):
        print("back to menu pressed")
        self.manager.disable()
        self.window.show_view(Other())
    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        arcade.start_render()
        self.manager.draw()

    def on_buttonclick(self, event):
        print("button is clicked")
    
class Difficulty(arcade.View):
    def on_show_view(self):
        
        arcade.set_background_color(arcade.color.GRAY)
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()
        
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
        
    def on_click_easy(self, event):
        #SET DIFFICULTY OF BOT TO EASY (FOR FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(Other())
        
    def on_click_medium(self, event):
        #SET DIFFICULTY OF BOT TO MEDIUM (FOR FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(Other())
        
    def on_click_hard(self, event):
        #SET DIFFICULTY OF BOT TO HARD (FOR FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(Other())


        
        
        
    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        arcade.start_render()
        self.manager.draw()
        
    

    
        
    
    def on_click_exit(self, event):
        print("exit button clicked")
        self.manager.disable()
        arcade.exit()   

class Other(arcade.View):
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
        
    def on_click_reveal(self, event):
        #CHANGE SETTING SO THAT DEFENDING PEICES ARE NOT REVEALED (FUTURE)
        
        self.window.show_view(gameboard.Gameboard())
        
    def on_click_hide(self, event):
        #CHANGE SETTING SO THAT DEFENDING PEICES ARE REVEALED (FUTURE)
        
        #CHANGE WINDOWS
        self.window.show_view(gameboard.Gameboard())
        
    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        arcade.start_render()
        self.manager.draw()




        

    