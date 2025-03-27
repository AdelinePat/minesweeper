import pygame, sys
from view.menu import Menu
from controller.menu_controller import MenuController
from controller.game_controller import GameController
from view.__settings__ import TITLE_FONT, CELESTE
from view.settings_menu import SettingsMenu

class MainMenu():
    def __init__(self):
        self.menu = Menu('Minesweeper')  # Main game menu
        self.controller = MenuController()
        self.game_controller = GameController()
        self.in_settings_screen = False  # Track if we are in settings screen
        self.settings = SettingsMenu()

    def settings_screen(self):
        """Handles the display of the settings screen with dropdown menus"""
        self.settings.settings_screen()

    def main_loop(self):
        pygame.init()

        while True:
            self.controller.screen_access()
            self.main_menu_screen()
            

            if self.button_quit == True:
                pygame.quit()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            

            # Handle main menu and settings screen separately
            if self.controller.is_screen_main:
                self.main_menu_screen()  # Display main menu screen
            elif self.controller.is_screen_settings:
                self.settings_screen()  # Display settings screen

            pygame.display.update()

    def main_menu_screen(self):
        my_title = self.menu.draw_text('Minesweeper',
                                        TITLE_FONT,
                                        self.menu.height // 9,
                                        self.menu.title_center,
                                        color=CELESTE)

        # Main menu buttons
        self.controller.is_screen_in_game = self.menu.draw_full_button('Jouer', (self.menu.screen_center[0],
                                            self.menu.screen_center[1] - self.menu.height // 8 * 1.5))

        self.controller.is_screen_settings = self.menu.draw_full_button('Paramètres',
                                                (self.menu.screen_center[0],
                                                self.menu.screen_center[1] - self.menu.height // 8 * 0.5))

        self.controller.is_screen_record = self.menu.draw_full_button('Palmarès',
                                                (self.menu.screen_center[0],
                                                self.menu.screen_center[1] + self.menu.height // 8 * 0.5))

        self.button_quit = self.menu.draw_full_button('Quitter',
                                                (self.menu.screen_center[0],
                                                self.menu.screen_center[1] + self.menu.height // 8 * 1.5))
       
        # Handle button clicks
        # mouse_position = pygame.mouse.get_pos()
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()

        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if button_play.collidepoint(mouse_position):
        #             print("Game Started!")
        #             # Transition to game screen logic
        #             # self.controller.is_screen_main = False
        #             # self.controller.is_screen_in_game = True

        #         elif button_settings.collidepoint(mouse_position):
        #             self.controller.is_screen_main = False
        #             self.controller.is_screen_record = True
        #             self.controller.go_to_settings()  # Go to settings screen

        #         elif button_quit.collidepoint(mouse_position):
        #             pygame.quit()
        #             sys.exit()

          # Access the appropriate screen based on current state

