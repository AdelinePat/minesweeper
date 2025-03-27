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
            #  text, font, font_size, position, color=INDIGO_DYE
            

            # small_button = self.menu.small_button('POO PI POO PI POOOOO',
            #                         (self.menu.screen_center[0],
            #                         self.menu.screen_center[1] + self.menu.height//8*1.5))
            
            self.controller.screen_access()
            # self.controller.start_game()
            # self.controller.set_settings(self.controller.is_screen_settings)
            # self.controller.get_top_players(self.controller.is_screen_record)

            if self.button_quit == True:
                pygame.quit()

            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                
                    print("A key has been pressed")

            self.menu.update()
            
        pygame.quit()
