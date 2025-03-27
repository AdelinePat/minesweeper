import pygame
import sys
from view.__settings__ import TITLE_FONT, TEXT_FONT, CYAN, INDIGO_DYE, GHOST_WHITE, AGRESSIVE_PINK
from view.menu import Menu
from view.interface import Interface


class SettingsMenu(Menu):
    def __init__(self, caption="Settings"):
        super().__init__(caption)

        self.interface = Interface(caption)
        self.screen = self.interface.screen
        

        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0
        self.resolutions = ["1080x720", "720x450"]
        self.resolution_index = 0
        self.languages = ["fr", "eng"]
        self.language_index = 0

    def draw_button(self, text, center):
        return self.draw_full_button(text, center, background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TITLE_FONT)
    
    
    def option_button(self, label, options, index, center):

        label_button = self.draw_full_button(f"{label}:", center=(center[0] - 100, center[1]), background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TEXT_FONT)
        
        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]

        option_button = self.draw_full_button(option_text, center=(label_button.right + 50, center[1]), background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TEXT_FONT)

        left_button = pygame.Rect(option_button.left - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_button.right + 10, center[1] - 15, 30, 30)

        pygame.draw.rect(self.screen, INDIGO_DYE, left_button)
        pygame.draw.rect(self.screen, INDIGO_DYE, right_button)

        self.interface.draw_text("<", (left_button.centerx - 10, left_button.centery - 15), color=GHOST_WHITE)
        self.interface.draw_text(">", (right_button.centerx - 10, right_button.centery - 15), color=GHOST_WHITE)

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
    
    def draw_window_settings(self, controller):
        """Affiche les boutons sur l'interface Settings et les rend accessibles dans la classe."""
       
        self.reset_background_screen()
        self.win_height = self.height // 3 * 1.2
        self.draw_menu_window()

        self.interface.draw_text("Paramètres", TITLE_FONT, 50, (self.win_width // 2, self.win_height // 8))

        # Création et affichage des boutons
        self.button_difficulty = self.draw_full_button("Difficulté", (self.win_width // 1.13, self.win_height // 8 * 1.5))
        if self.button_difficulty:
            self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)
            self.get_current_settings()

        self.button_resolution = self.draw_full_button("Résolution", (self.win_width // 1.13, self.win_height // 8 * 3.5))
        if self.button_resolution:
            self.resolution_index = (self.resolution_index + 1) % len(self.resolutions)
            self.get_current_settings()

        self.button_language = self.draw_full_button("Langue", (self.win_width // 1.13, self.win_height // 8 * 5.5))
        if self.button_language:
            self.language_index = (self.language_index + 1) % len(self.languages)
            self.get_current_settings()

        # Ajout du bouton Retour
        self.button_return = self.draw_full_button("Retour", (self.win_width // 1.35, self.win_height // 8 * 7))

        return self.button_return  # Retourne le bouton retour pour gestion dans le contrôleur




    def update(self):
        pygame.display.update()