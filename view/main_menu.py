import pygame
import sys
from view.menu import Menu
from controller.menu_controller import MenuController
from view.__settings__ import TITLE_FONT, CELESTE

class MainMenu(Menu):
    def __init__(self, caption):
        super().__init__(caption)
        # self.menu = Menu('Minesweeper')  # Main game menu
        self.controller = MenuController()
        self.get_resolution(self.controller.resolution)
        
        self.in_settings_screen = False  # Track if we are in settings screen
        self.button_quit = self.draw_full_button('Quitter', 
                                (self.screen_center[0], self.screen_center[1] + self.height // 8 * 1.5))
    
    def draw_main_menu(self):
        # Reset background and draw the main menu
        self.reset_background_screen()
        self.draw_menu_window()

        # Title of the game
        my_title = self.draw_text('Minesweeper',
                                       TITLE_FONT,
                                       self.height // 9,
                                       self.title_center,
                                       color=CELESTE)
        
        # "Play" button
        self.controller.is_screen_in_game = self.draw_full_button('Jouer', 
                                  (self.screen_center[0], self.screen_center[1] - self.height // 8 * 1.5))

        # "Settings" button
        if self.draw_full_button('Paramètres',
                            (self.screen_center[0], self.screen_center[1] - self.height // 8 * 0.5)):
            self.controller.go_to_settings()  # Utilise la fonction de transition


        # "Leaderboard" button
        self.controller.is_screen_win = self.draw_full_button('Palmarès', 
                                (self.screen_center[0], self.screen_center[1] + self.height // 8 * 0.5))
        
        if self.controller.is_screen_win==True:
            print("hola")
        # "Quit" button
        self.button_quit = self.draw_full_button('Quitter', 
                                (self.screen_center[0], self.screen_center[1] + self.height // 8 * 1.5))
        
        

    def main_loop(self):
        pygame.init()

        

        while True:

            # if self.controller.resolution != self.controller.settings_screen.resolutions[0]:
            # self.get_resolution(self.controller.resolution)
            # Draw the main menu screen
            if self.controller.is_screen_main:
                self.draw_main_menu()

                if self.button_quit:
                    print("Exiting the game...")
                    pygame.quit()
                    sys.exit() 

            else:
                
                if self.button_quit:
                    print("Exiting the game...")
                    pygame.quit()
                    sys.exit()   
            
            self.controller.screen_access()

            # Event handling for window events (such as quit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
            # Update the display to show changes
            # pygame.display.update()
            self.update()
