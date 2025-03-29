import pygame, sys
from view.menu import Menu
import json
from datetime import datetime
from view.__settings__ import TITLE_FONT, CELESTE, TEXT_FONT, GHOST_WHITE, CERULEAN, AGRESSIVE_PINK, INDIGO_DYE, CYAN, NOT_SO_GHOST_WHITE

class RollOfFame(Menu):
    def __init__(self, controller):
        super().__init__('Wall of Fame')
        self.controller = controller
        self.game_controller = self.controller.game_controller
        # self.in_settings_screen = False

    def draw_wall_of_fame_menu(self):
        self.reset_background_screen()
        self.draw_menu_window()

        my_title = self.draw_text('Wall of Fame',
                                       TITLE_FONT,
                                       self.height//9,
                                       self.title_center,
                                       color=CELESTE)

        # Load player data from JSON file
        try:
            with open('view/wall_of_fame.json', 'r') as file:
                players = json.load(file)
        except(FileExistsError, json.JSONDecodeError):
            player = []        


        # Draw buttons with player names and times
        for index, player in enumerate(players[:3]):  # Display only the top 3 players
            player_name_display_top3 = player.get("name", f"Player {index + 1}")
            player_time = player.get("time", 0)
            button_text = f"{player_name_display_top3}: {player_time}s"

            if index == 0:
                player_name_display_top3  = self.draw_full_button(button_text,
                                                     (self.screen_center[0],
                                                      self.screen_center[1] - self.height//8*1.5))
            elif index == 1:
                player_name_display_top3 = self.draw_full_button(button_text,
                                                                               (self.screen_center[0],
                                                                                self.screen_center[1] - self.height//8*0.5))
            elif index == 2:
                player_name_display_top3 = self.draw_full_button(button_text,
                                                                           (self.screen_center[0],
                                                                            self.screen_center[1] + self.height//8*0.5))

        self.button_return = self.draw_full_button('Retour',
                                                        (self.screen_center[0],
                                                         self.screen_center[1] + self.height//8*1.5))

        return self.button_return
    
    # def bouton(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             mouse_pos = pygame.mouse.get_pos()
    #             if self.button_retour.collidepoint(mouse_pos):
    #                 self.controller.go_to_main_menu()
    #                 self.draw_wall_of_fame_menu() 



