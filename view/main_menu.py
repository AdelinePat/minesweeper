
import pygame
import sys
from view.__settings__ import TITLE_FONT, CELESTE
from view.menu import Menu
from controller.menu_controller import MenuController

class MainMenu(Menu):
    def __init__(self, caption):
        super().__init__(caption)
        self.controller = MenuController()
        self.get_resolution(self.controller.resolution)
        self.button_quit = self.draw_full_button('Quitter', 
                                (self.screen_center[0], self.screen_center[1] + self.height // 8 * 1.5))
    
    def draw_main_menu(self):
        self.set_caption(self.caption)
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
        self.controller.is_screen_settings = self.draw_full_button('Paramètres',
                            (self.screen_center[0], self.screen_center[1] - self.height // 8 * 0.5))

        # "Leaderboard" button
        self.controller.is_screen_record = self.draw_full_button('Palmarès', 
                                (self.screen_center[0], self.screen_center[1] + self.height // 8 * 0.5))
        
        # "Quit" button
        self.button_quit = self.draw_full_button('Quitter', 
                                (self.screen_center[0], self.screen_center[1] + self.height // 8 * 1.5))
        
        

    def main_loop(self):
        pygame.init()

        while True:
            # Draw the main menu screen
            if self.controller.resolution != self.controller.settings_screen.resolution:
                    self.controller.resolution = self.controller.settings_screen.resolution
                    self.get_resolution(self.controller.resolution)
                    self.get_actual_menu_window()
                    
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

            self.update()

          
 