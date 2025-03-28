import pygame
import sys
from view.__settings__ import TITLE_FONT, TEXT_FONT, CYAN  # Utiliser BLACK à la place de INDIGO_DYE
from view.menu import Menu
from view.interface import Interface


BLACK = (0, 0, 0)



class SettingsMenu(Menu):
    def __init__(self, caption="Settings"):
        super().__init__(caption)
        
        self.interface = Interface(caption)
        self.screen = self.interface.screen
        
        # Attributs spécifiques à la fenêtre de paramètres
        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0
        self.resolutions = ["1080x720", "720x450"]
        self.resolution_index = 0
        self.languages = ["fr", "eng"]
        self.language_index = 0
        self.setting_win = self.draw_menu_window()

    def draw_text(self, text, position, color=TEXT_FONT):  
        text_surface = color.render(text, True, color) 
        self.screen.blit(text_surface, position)

    def draw_button(self, text, center):
        button_rect = pygame.Rect(0, 0, 120, 50)
        button_rect.center = center
        pygame.draw.rect(self.screen, CYAN, button_rect, border_radius=10)
        text_surface = TITLE_FONT.render(text, True, TEXT_FONT)  
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        return button_rect
    

    def option_button(self, label, options, index, center):
        label_surface = TEXT_FONT.render(f"{label}:", True, BLACK)  # Remplacer INDIGO_DYE par BLACK ici
        label_rect = label_surface.get_rect(midright=(center[0] - 100, center[1]))

        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]
        option_surface = TEXT_FONT.render(option_text, True, BLACK)  # Remplacer INDIGO_DYE par BLACK ici
        option_rect = option_surface.get_rect(midleft=(label_rect.right + 50, center[1]))

        left_button = pygame.Rect(option_rect.left - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_rect.right + 10, center[1] - 15, 30, 30)

        pygame.draw.rect(self.screen, BLACK, left_button)  # Remplacer INDIGO_DYE par BLACK ici
        pygame.draw.rect(self.screen, BLACK, right_button)  # Remplacer INDIGO_DYE par BLACK ici

        self.screen.blit(label_surface, label_rect)
        self.screen.blit(option_surface, option_rect)

        self.draw_text("<", (left_button.centerx - 10, left_button.centery - 15), CYAN)
        self.draw_text(">", (right_button.centerx - 10, right_button.centery - 15),  CYAN)

        return left_button, right_button

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

    def draw_settings_screen(self):
        running = True
        while running:
            self.screen.fill(CYAN)

            left_difficulty, right_difficulty = self.option_button(
                "Difficulté", self.difficulties, self.difficulty_index, (self.win_width // 1.13, self.win_height // 8 * 1.5)
            )
            left_resolution, right_resolution = self.option_button(
                "Résolution", self.resolutions, self.resolution_index, (self.win_width // 1.13, self.win_height // 8 * 3.5)
            )
            left_language, right_language = self.option_button(
                "Langue", self.languages, self.language_index, (self.win_width // 1.13, self.win_height // 8 * 5.5)
            )

            button_back = self.draw_button("Back", (self.win_width // 1.35, self.win_height // 8 * 7))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if left_difficulty.collidepoint(event.pos):
                        self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulties)
                        self.get_current_settings() 
                    if right_difficulty.collidepoint(event.pos):
                        self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)
                        self.get_current_settings()

                    if left_resolution.collidepoint(event.pos):
                        self.resolution_index = (self.resolution_index - 1) % len(self.resolutions)
                        self.get_current_settings()
                    if right_resolution.collidepoint(event.pos):
                        self.resolution_index = (self.resolution_index + 1) % len(self.resolutions)
                        self.get_current_settings()

                    if left_language.collidepoint(event.pos):
                        self.language_index = (self.language_index - 1) % len(self.languages)
                        self.get_current_settings()
                    if right_language.collidepoint(event.pos):
                        self.language_index = (self.language_index + 1) % len(self.languages)
                        self.get_current_settings()

                    if button_back.collidepoint(event.pos):
                        print("Retour au menu")  
                        running = False  
            pygame.display.flip()

settings = SettingsMenu()
settings.draw_settings_screen()

def update(self):
    pygame.display.flip()
