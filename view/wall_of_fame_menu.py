import pygame, sys
from view.menu import Menu
from controller.menu_controller import MenuController
from controller.game_controller import GameController
import json
from datetime import datetime
from view.__settings__ import TITLE_FONT, CELESTE, TEXT_FONT, GHOST_WHITE, CERULEAN, AGRESSIVE_PINK, INDIGO_DYE, CYAN, NOT_SO_GHOST_WHITE

class Wall_of_fame_menu():
    def __init__(self):
        self.menu = Menu('Wall of Fame')
        self.controller = MenuController()
        self.game_controller = GameController()
        self.in_settings_screen = False

    def draw_wall_of_fame_menu(self):
        self.menu.reset_background_screen()
        self.menu.draw_menu_window()

        my_title = self.menu.draw_text('Wall of Fame',
                                       TITLE_FONT,
                                       self.menu.height//9,
                                       self.menu.title_center,
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
                player_name_display_top3  = self.menu.draw_full_button(button_text,
                                                     (self.menu.screen_center[0],
                                                      self.menu.screen_center[1] - self.menu.height//8*1.5))
            elif index == 1:
                player_name_display_top3 = self.menu.draw_full_button(button_text,
                                                                               (self.menu.screen_center[0],
                                                                                self.menu.screen_center[1] - self.menu.height//8*0.5))
            elif index == 2:
                player_name_display_top3 = self.menu.draw_full_button(button_text,
                                                                           (self.menu.screen_center[0],
                                                                            self.menu.screen_center[1] + self.menu.height//8*0.5))

        self.button_retour = self.menu.draw_full_button('Retour',
                                                        (self.menu.screen_center[0],
                                                         self.menu.screen_center[1] + self.menu.height//8*1.5))

        return self.button_retour
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.button_retour.collidepoint(mouse_pos):
                    self.controller.go_to_main_menu()
                    self.draw_wall_of_fame_menu() 



