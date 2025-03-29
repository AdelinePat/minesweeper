# from view.interface import Interface
from view.menu import Menu
from view.__settings__ import TITLE_FONT, CELESTE, TEXT_FONT, GHOST_WHITE, CERULEAN, AGRESSIVE_PINK, TEXT_FONT, INDIGO_DYE, CYAN, NOT_SO_GHOST_WHITE 
import pygame

class Winner(Menu):
    def __init__(self, caption, controller, identification=0):
        super().__init__(caption, identification)
        self.game_controller = controller
        self.get_resolution(self.resolution)
        
        self.draw_menu_window()
        self.player_name_to_input = ""

    def draw_window_winner_not_top_3(self, controller):
        # self.get_resolution(controller.resolution)

        self.reset_background_screen()
        self.win_height = self.height // 3*1.2
        self.draw_menu_window()

        self.draw_subtitle(
                "Bravo, vous avez gagné !",
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
        # player_name_display = controller.player_name if controller.player_name else "nom-de_joueur"
        self.game_controller.game_info.player_name = self.player_name_to_input

        # controller.top_players = self.draw_full_button(
        #     player_name_display,
        #     (self.screen_center[0],
        #     self.screen_center[1] - self.height // 8 * 0.1)
        # )
        self.input_user_name()
    

        self.button_return = self.medium_button(
            'Retour',
            (self.screen_center[0],
            self.screen_center[1] + self.height // 8 * 1.5)
        )

        return self.button_return

    def input_user_name(self):
        #text, font, font_size, position,

        self.draw_full_button(self.player_name_to_input,
                            (self.screen_center[0],
                            self.screen_center[1] - self.height // 8 * 0.1))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.player_name_to_input:
                    return self.player_name_to_input
                            
                elif event.key == pygame.K_BACKSPACE:
                                self.player_name_to_input = self.player_name_to_input[:-1]

                elif event.unicode.isalnum():
                    self.player_name_to_input += event.unicode

