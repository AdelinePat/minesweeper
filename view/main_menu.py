import pygame, sys
from view.menu import Menu
from controller.menu_controller import MenuController
from controller.game_controller import GameController
from view.__settings__ import TITLE_FONT, CELESTE

class MainMenu():
    def __init__(self):
        self.menu = Menu('Minesweeper')
        self.controller = MenuController()
        self.game_controller = GameController()

    def main_loop(self):
        pygame.init()

        while True:
            # Check the current screen and handle accordingly
            if self.controller.current_screen == "main":
                self.main_menu_screen()  # Main menu screen
            elif self.controller.current_screen == "settings":
                self.settings_screen()  # Settings screen

            self.menu.update()  # Update the menu each loop

    def main_menu_screen(self):
        """This method handles the main menu screen."""
        # Draw title text
        my_title = self.menu.draw_text('Minesweeper',
                                       TITLE_FONT,
                                       self.menu.height//9,
                                       self.menu.title_center,
                                       color=CELESTE)
        
        # Draw buttons and check if they're pressed (for the main menu only)
        button_play = self.menu.draw_full_button('Jouer', 
                                                 (self.menu.screen_center[0],
                                                  self.menu.screen_center[1]- self.menu.height//8*1.5))
        
        button_settings = self.menu.draw_full_button('Paramètres',
                                                     (self.menu.screen_center[0],
                                                      self.menu.screen_center[1]- self.menu.height//8*0.5))
        
        button_record = self.menu.draw_full_button('Palmarès', 
                                                   (self.menu.screen_center[0],
                                                    self.menu.screen_center[1] + self.menu.height//8*0.5))
        
        button_quit = self.menu.draw_full_button('Quitter', 
                                                 (self.menu.screen_center[0],
                                                  self.menu.screen_center[1] + self.menu.height//8*1.5))

        # Handle button clicks and navigate accordingly (for the main menu only)
        if button_play:
             self.controller.start_game()  # Start the game
        elif button_settings:
             self.controller.set_settings()  # Go to settings screen
        elif button_record:
             self.controller.show_leaderboard()  # Show leaderboard
        elif button_quit:
             pygame.quit()  # Quit the game
             sys.exit()

        # Event handling for mouse clicks or key presses (for the main menu only)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def settings_screen(self):
        """This method handles the settings screen, which is similar to the main menu."""
        # Draw title text for settings
        my_title = self.menu.draw_text('Paramètres',
                                       TITLE_FONT,
                                       self.menu.height//9,
                                       self.menu.title_center,
                                       color=CELESTE)
        
        # Draw different buttons for the settings menu (only settings-related buttons)
        button_difficulty = self.menu.draw_full_button('Difficultés', 
                                                 (self.menu.screen_center[0],
                                                 self.menu.screen_center[1]- self.menu.height//8*1.5))
        
        button_language = self.menu.draw_full_button('Langues', 
                                                   (self.menu.screen_center[0],
                                                    self.menu.screen_center[1] - self.menu.height//8*0.5))
        
        button_resolution = self.menu.draw_full_button('Résolution', 
                                                 (self.menu.screen_center[0],
                                                  self.menu.screen_center[1] + self.menu.height//8*1.5))
        
        button_back = self.menu.draw_full_button('Retour', 
                                                 (self.menu.screen_center[0],
                                                  self.menu.screen_center[1] + self.menu.height//8*2))

        # Handle button clicks for settings screen
        if button_difficulty:
            # Add your audio settings logic here
            print("Difficultés settings clicked!")
        elif button_language:
            # Add your language settings logic here
            print("Language settings clicked!")
        elif button_resolution:
            print("Resolution settings clicked!")  # Add resolution logic
        elif button_back:
            # Go back to the main menu when the 'Retour' button is pressed
            self.controller.change_screen("main")

        # Event handling for the settings screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
