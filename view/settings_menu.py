import pygame
import sys
from view.__settings__ import TITLE_FONT, TEXT_FONT, CYAN, INDIGO_DYE, GHOST_WHITE, AGRESSIVE_PINK,CELESTE
from view.menu import Menu
from view.interface import Interface


class SettingsMenu(Menu):
    def __init__(self, caption="Settings"):
        super().__init__(caption)
        # self.interface = Interface(caption)
        # self.screen = self.interface.screen
        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0
        self.resolutions = ["1080x720", "720x450"]
        self.resolution_index = 0
        self.languages = ["fr", "eng"]
        self.language_index = 0

    # def draw_button(self, text, center):
    #     return self.draw_full_button(text, center, background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TITLE_FONT)
    
    
    def option_button(self, label, options, index, center):

        # label_button = self.draw_full_button(f"{label}:", center=(center[0] - 100, center[1]), background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TEXT_FONT)
        
        # option_text = options[index][0] if isinstance(options[index], tuple) else options[index]

        # option_button = self.draw_full_button(option_text, center=(label_button.right + 50, center[1]), background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TEXT_FONT)

        # left_button = pygame.Rect(option_button.left - 40, center[1] - 15, 30, 30)
        # right_button = pygame.Rect(option_button.right + 10, center[1] - 15, 30, 30)

        # pygame.draw.rect(self.screen, INDIGO_DYE, left_button)
        # pygame.draw.rect(self.screen, INDIGO_DYE, right_button)

        # self.draw_text("<", (left_button.centerx - 10, left_button.centery - 12), color=CYAN)
        # self.draw_text(">", (right_button.centerx - 10, right_button.centery - 12), color=CYAN)

        # return left_button, right_button
        option_surface = self.draw_full_text(center)

        #  text, font, font_size, position,
        label_rect = self.draw_text(f"{label}",
                       TEXT_FONT,
                       self.height//18,
                       (option_surface.midleft[0] + 20, option_surface.midleft)
                       )

        # label_surface = FONT.render(f"{label}:", True, BLACK)
        # label_rect = label_surface.get_rect(midright=(center[0] - 100, center[1]))

        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]
        option_rect = self.draw_text(option_text, TEXT_FONT, self.height//18, (option_surface.midright[0] - 100, option_surface.midright))

        # option_surface = FONT.render(option_text, True, BLACK)
        # option_rect = option_surface.get_rect(midleft=(label_rect.right + 50, center[1]))

        left_button = pygame.Rect(option_surface.left[0] - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_surface.right[0] + 10, center[1] - 15, 30, 30)

        pygame.draw.rect(self.screen, 'grey', left_button)
        pygame.draw.rect(self.screen, 'grey', right_button)

        # self.screen.blit(label_surface, label_rect)
        # self.screen.blit(option_surface, option_rect)

        actual_left_button = self.draw_text("<", (left_button.centerx - 5, left_button.centery - 10), 'black')
        actual_right_button = self.draw_text(">", (right_button.centerx - 5, right_button.centery - 10), 'black')

        return actual_left_button, actual_right_button
    

    def get_current_settings(self):
            settings = (
                (self.difficulty_index, self.difficulties[self.difficulty_index]),
                (self.resolution_index, self.resolutions[self.resolution_index]),
                (self.language_index, self.languages[self.language_index]),
            )

            print(f"Difficulté: Index {settings[0][0]}, Valeur {settings[0][1]}")
            print(f"Résolution: Index {settings[1][0]}, Valeur {settings[1][1]}")
            print(f"Langue: Index {settings[2][0]}, Valeur {settings[2][1]}")

            return settings
        
    # def draw_window_settings(self, controller): 
    #     # self.reset_background_screen()
    #     # self.win_height = self.height // 3 * 2
    #     self.draw_menu_window()

    #     self.draw_text("Paramètres", TITLE_FONT, 50, (self.height // 9, self.title_center))

    
    #     self.left_difficulty, self.right_difficulty = self.option_button("Difficulté", self.difficulties, self.difficulty_index, (self.win_width // 3, self.win_height // 8 * 1.5))
    #     self.left_resolution, self.right_resolution = self.option_button("Résolution", self.resolutions, self.resolution_index, (self.win_width // 3, self.win_height // 8 * 3.5))
    #     self.left_language, self.right_language = self.option_button("Langue", self.languages, self.language_index, (self.win_width // 3, self.win_height // 8 * 5.5))

       
    #     self.button_return = self.draw_full_button("Retour", (self.win_width // 2, self.win_height // 8 * 7))

    #     return self.button_return  

    
    def draw_window_settings(self, controller):
        self.reset_background_screen()
        self.draw_menu_window()

        self.draw_text("Paramètres",
                        TITLE_FONT,
                        self.height//9,
                        self.title_center,
                        color=CELESTE)
        
        # option_button(self, label, options, index, center):

        left_difficulty, right_difficulty = self.option_button(
                "Difficulté", self.difficulties, self.difficulty_index, (self.width // 2, 60)
            )
        left_resolution, right_resolution = self.option_button(
            "Résolution", self.resolutions, self.resolution_index, (self.width // 2, 120)
        )
        left_language, right_language = self.option_button(
            "Langue", self.languages, self.language_index, (self.width // 2, 180)
        )

        # Boutons Retour et Appliquer
        button_back = self.draw_button("Retour", (self.width // 3, 240))
        button_apply = self.draw_button("Appliquer", (2 * self.width // 3, 240))

        # self.button_difficulty = self.draw_full_button("Difficulté",(self.screen_center[0],
        #                     self.screen_center[1] - self.height//8*1.5))
        #                                             #    (self.win_width // 1.13, self.win_height // 8 * 1.5))
        # if self.button_difficulty:
        #     self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)
        #     self.get_current_settings()

        # self.button_resolution = self.draw_full_button("Résolution", 
        #                                                (self.screen_center[0],
        #                         self.screen_center[1] - self.height//8*0.5))
        #                                             #    (self.win_width // 1.13, self.win_height // 8 * 3.5))
        # if self.button_resolution:
        #     self.resolution_index = (self.resolution_index + 1) % len(self.resolutions)
        #     self.get_current_settings()

        # self.button_language = self.draw_full_button("Langue", (self.screen_center[0],
        #                         self.screen_center[1] + self.height//8*0.5))
        
        #                     # (self.win_width // 1.13, self.win_height // 8 * 5.5))
        # if self.button_language:
        #     self.language_index = (self.language_index + 1) % len(self.languages)
        #     self.get_current_settings()

        
        self.button_return = self.draw_full_button("Retour", 
                                                   (self.screen_center[0],
                                self.screen_center[1] + self.height//8*1.5))
        # (self.win_width // 1.35, self.win_height // 8 * 7))

        return self.button_return  
