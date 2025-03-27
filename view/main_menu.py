import pygame, sys
from view.menu import Menu
from controller.menu_controller import MenuController
from controller.game_controller import GameController
from view.__settings__ import TITLE_FONT, CELESTE

class MainMenu():
    def __init__(self):
        self.menu = Menu('Minesweeper')  # Main game menu
        self.controller = MenuController()
        self.game_controller = GameController()
        self.in_settings_screen = False  # Track if we are in settings screen

    def draw_main_menu(self):
        self.menu.reset_background_screen()
        self.menu.draw_menu_window()

        my_title = self.menu.draw_text('Minesweeper',
                                           TITLE_FONT,
                                           self.menu.height//9,
                                           self.menu.title_center,
                                           color=CELESTE)
            
        self.controller.is_screen_in_game = self.menu.draw_full_button('Jouer', (self.menu.screen_center[0],
                            self.menu.screen_center[1]- self.menu.height//8*1.5))
        
        # self.controller.game_info.
        
        self.controller.is_screen_settings = self.menu.draw_full_button('Paramètres',
                                (self.menu.screen_center[0],
                                self.menu.screen_center[1]- self.menu.height//8*0.5))
        
        self.controller.is_screen_win = self.menu.draw_full_button('Palmarès', 
                                (self.menu.screen_center[0],
                                self.menu.screen_center[1] + self.menu.height//8*0.5))
        
        self.button_quit = self.menu.draw_full_button('Quitter', 
                                (self.menu.screen_center[0],
                                self.menu.screen_center[1] + self.menu.height//8*1.5))


    def main_loop(self):
        pygame.init()

        while True:

            if self.controller.is_screen_main:
                self.draw_main_menu()
        
            self.controller.screen_access()
            
            if self.button_quit == True:
                pygame.quit()

            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()