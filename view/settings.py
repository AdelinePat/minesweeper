import pygame
import sys
from view.__settings__ import TITLE_FONT, CELESTE, RESOLUTION  # Necessary imports
# from view.interface import Interface
from view.menu import Menu



class Settings(Menu):
    def __init__(self, caption="Settings"):
        # Calling the parent class constructor (Interface)
        super().__init__(caption)
        # self.menu = Menu(caption)
        
        # Attributes specific to the settings window
        self.difficulties = ["Facile", "Difficile"]
        self.resolutions = ["1080x720", "720x450"]
        self.difficulty_index = 0
        self.resolution_index = 0
        self.setting_win = self.draw_menu_window()
        # self.draw_full_button = self.draw_full_button()

    def draw_settings_screen(self):
        """Handles the display of the settings screen with dropdown menus"""
        while True:
            # Display settings screen title
            # self.draw_text('Settings', TITLE_FONT, 60, self.title_center, color=CELESTE)

            # ==== Difficulty dropdown menu ====
            # self.draw_text('Difficulty', TITLE_FONT, 40, (self.screen_center[0], self.screen_center[1] - 100), color=CELESTE)

            # Arrows for navigation (left and right)
            self.option_button('Difficulté', self.difficulties[self.difficulty_index],
                            self.screen_center)
            # left_arrow_difficulty = self.draw_full_button('< ', (self.screen_center[0] - 100, self.screen_center[1] - 50))
            # right_arrow_difficulty = self.draw_full_button('>', (self.screen_center[0] + 100, self.screen_center[1] - 50))

            # Display the current difficulty option
            # self.draw_text(self.difficulties[self.difficulty_index], TITLE_FONT, 40, (self.screen_center[0], self.screen_center[1] - 50), color=CELESTE)

            # ==== Resolution dropdown menu ====
            # self.draw_text('Resolution', TITLE_FONT, 40, (self.screen_center[0], self.screen_center[1] + 50), color=CELESTE)

            # left_arrow_resolution = self.draw_full_button('<', (self.screen_center[0] - 100, self.screen_center[1] + 100))
            # right_arrow_resolution = self.draw_full_button('>', (self.screen_center[0] + 100, self.screen_center[1] + 100))

            # self.draw_text(self.resolutions[self.resolution_index], TITLE_FONT, 40, (self.screen_center[0], self.screen_center[1] + 100), color=CELESTE)

            # ==== Back button ====
            # button_back = self.draw_full_button('Back', (self.screen_center[0], self.screen_center[1] + 200))

            # Handle mouse click events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     # Handle difficulty change on arrow button clicks
            #     if left_arrow_difficulty.collidepoint(event.pos):
            #         self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulties)
            #     if right_arrow_difficulty.collidepoint(event.pos):
            #         self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)

            #     # Handle resolution change on arrow button clicks
            #     if left_arrow_resolution.collidepoint(event.pos):
            #         self.resolution_index = (self.resolution_index - 1) % len(self.resolutions)
            #     if right_arrow_resolution.collidepoint(event.pos):
            #         self.resolution_index = (self.resolution_index + 1) % len(self.resolutions)

            #     # Handle Back button click
            #     if button_back.collidepoint(event.pos):
            #         self.in_settings_screen = False  # Return to main menu
            #         self.controller.change_screen("main")  # Go back to main menu

    def update(self):
        """Update the screen"""
        pygame.display.update()

