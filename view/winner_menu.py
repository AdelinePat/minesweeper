# from view.interface import Interface
from view.menu import Menu
from view.__settings__ import TITLE_FONT, CELESTE, TEXT_FONT, GHOST_WHITE, CERULEAN, AGRESSIVE_PINK, TEXT_FONT, INDIGO_DYE, CYAN, NOT_SO_GHOST_WHITE 
import pygame

class Winner(Menu):
    def __init__(self, caption, identification=0):
        super().__init__(caption, identification)
        
        self.get_resolution(self.resolution)
        
        self.draw_menu_window()

    def draw_window_winner_not_top_3(self, controller):
        # self.get_resolution(controller.resolution)

        self.reset_background_screen()
        self.win_height = self.height // 3*1.2
        self.draw_menu_window()

        self.draw_subtitle(
                "Veuillez entrer votre nom dans l'histoire",
                (self.screen_center[0],
                 self.screen_center[1] - self.height // 8*0.01)
            )
        
        self.button_return = self.medium_button(
            'Retour',
            (self.screen_center[0],
                self.screen_center[1] + self.height // 8*2.7)
        )
        
        return self.button_return

    def draw_winner_top_3(self, controller):
        self.reset_background_screen()
        self.win_height = self.height // 3*2
        if controller.resolution != controller.settings_screen.resolutions[0]:
            self.get_resolution(controller.resolution)
            
        self.draw_menu_window()

        my_title = self.draw_text('Vous avez gagné !',
                                           TITLE_FONT,
                                           self.height // 9,
                                           self.title_center,
                                           color=CELESTE)

        self.draw_subtitle(
                "Veuillez entrer votre nom dans l'histoire",
                (self.screen_center[0],
                 self.screen_center[1] - self.height // 8 * 1.5)
            )

        # prenom  MenuController 
        player_name_display = controller.player_name if controller.player_name else "nom-de_joueur"

        controller.top_players = self.draw_full_button(
            player_name_display,
            (self.screen_center[0],
            self.screen_center[1] - self.height // 8 * 0.1)
        )
    

        self.button_return = self.medium_button(
            'Retour',
            (self.screen_center[0],
            self.screen_center[1] + self.height // 8 * 1.5)
        )

        return self.button_return
