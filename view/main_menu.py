import pygame
import sys
from view.menu import Menu
from controller.menu_controller import MenuController
from view.__settings__ import TITLE_FONT, CELESTE

class MainMenu:
    def __init__(self):
        self.menu = Menu('Minesweeper')  # Main game menu
        self.controller = MenuController()
        self.in_settings_screen = False  # Track if we are in settings screen
    
    def draw_main_menu(self):
        # Reset background and draw the main menu
        self.menu.reset_background_screen()
        self.menu.draw_menu_window()

        # Title of the game
        my_title = self.menu.draw_text('Minesweeper',
                                       TITLE_FONT,
                                       self.menu.height // 9,
                                       self.menu.title_center,
                                       color=CELESTE)
        
        # "Play" button
        self.controller.is_screen_in_game = self.menu.draw_full_button('Jouer', 
                                  (self.menu.screen_center[0], self.menu.screen_center[1] - self.menu.height // 8 * 1.5))

        # "Settings" button
        if self.menu.draw_full_button('Paramètres',
                            (self.menu.screen_center[0], self.menu.screen_center[1] - self.menu.height // 8 * 0.5)):
            self.controller.go_to_settings()  # Utilise la fonction de transition


        # "Leaderboard" button
        self.controller.is_screen_win = self.menu.draw_full_button('Palmarès', 
                                (self.menu.screen_center[0], self.menu.screen_center[1] + self.menu.height // 8 * 0.5))
        
        if self.controller.is_screen_win==True:
            print("hola")
        # "Quit" button
        self.button_quit = self.menu.draw_full_button('Quitter', 
                                (self.menu.screen_center[0], self.menu.screen_center[1] + self.menu.height // 8 * 1.5))

    def main_loop(self):
        pygame.init()

        while True:
            # Draw the main menu screen
            if self.controller.is_screen_main:
                self.draw_main_menu()
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
            self.menu.update()
