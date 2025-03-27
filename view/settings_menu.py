import pygame
import sys
from view.__settings__ import TITLE_FONT, TEXT_FONT, CYAN, INDIGO_DYE # Correction de l'importation
from view.menu import Menu
from view.interface import Interface



class SettingsMenu(Menu):
    def __init__(self, caption="Settings"):
        super().__init__(caption)
        
        # Crée une instance de l'interface pour accéder à l'écran
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

    def draw_text(self, text, position, color=TEXT_FONT):  # Correction ici : TEXT_FONT et non FONT
        text_surface = color.render(text, True, color)  # Utilisation de la bonne variable
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
       
        label_surface = FONT.render(f"{label}:", True, BLACK)
        label_rect = label_surface.get_rect(midright=(center[0] - 100, center[1]))

        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]
        option_surface = FONT.render(option_text, True, BLACK)
        option_rect = option_surface.get_rect(midleft=(label_rect.right + 50, center[1]))

        left_button = pygame.Rect(option_rect.left - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_rect.right + 10, center[1] - 15, 30, 30)

        pygame.draw.rect(self.screen, INDIGO_DYE, left_button)
        pygame.draw.rect(self.screen, INDIGO_DYE, right_button)

        self.screen.blit(label_surface, label_rect)
        self.screen.blit(option_surface, option_rect)

        self.draw_text("<", (left_button.centerx - 10, left_button.centery - 15), BLACK)
        self.draw_text(">", (right_button.centerx - 10, right_button.centery - 15), BLACK)

        return left_button, right_button

    def option_button(self, label, options, index, center):
        label_surface = TEXT_FONT.render(f"{label}:", True, TEXT_FONT)  # Utilisation de TEXT_FONT
        label_rect = label_surface.get_rect(midright=(center[0] - 100, center[1]))

        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]
        option_surface = TEXT_FONT.render(option_text, True, TEXT_FONT)  # Utilisation de TEXT_FONT
        option_rect = option_surface.get_rect(midleft=(label_rect.right + 50, center[1]))

        left_button = pygame.Rect(option_rect.left - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_rect.right + 10, center[1] - 15, 30, 30)

        pygame.draw.rect(self.screen, CYAN, left_button)
        pygame.draw.rect(self.screen, CYAN, right_button)

        self.screen.blit(label_surface, label_rect)
        self.screen.blit(option_surface, option_rect)

        self.draw_text("<", (left_button.centerx - 10, left_button.centery - 15), TEXT_FONT)
        self.draw_text(">", (right_button.centerx - 10, right_button.centery - 15), TEXT_FONT)

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
        """Gère l'affichage de l'écran des paramètres avec des menus déroulants"""
        while True:
            # Affichage du titre de l'écran des paramètres
            # self.draw_text('Settings', TITLE_FONT, 60, self.title_center, color=CELESTE)

            # Menu déroulant pour la difficulté
            # self.option_button('Difficulté', self.difficulties[self.difficulty_index],
            #                 self.screen_center)
            # # Option pour naviguer dans les difficultés
            # left_arrow_difficulty = self.draw_full_button('< ', (self.screen_center[0] - 100, self.screen_center[1] - 50))
            # right_arrow_difficulty = self.draw_full_button('>', (self.screen_center[0] + 100, self.screen_center[1] - 50))

            # Menu déroulant pour la résolution
            # self.draw_text('Resolution', TITLE_FONT, 40, (self.screen_center[0], self.screen_center[1] + 50), color=CELESTE)
            # left_arrow_resolution = self.draw_full_button('<', (self.screen_center[0] - 100, self.screen_center[1] + 100))
            # right_arrow_resolution = self.draw_full_button('>', (self.screen_center[0] + 100, self.screen_center[1] + 100))

            # Affichage de la résolution actuelle
            # self.draw_text(self.resolutions[self.resolution_index], TITLE_FONT, 40, (self.screen_center[0], self.screen_center[1] + 100), color=CELESTE)

            # Bouton de retour
            # button_back = self.draw_full_button('Back', (self.screen_center[0], self.screen_center[1] + 200))

            # Gestion des événements de clic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update()

    def update(self):
        """Met à jour l'écran"""
        pygame.display.update()
