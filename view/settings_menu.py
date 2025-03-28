import pygame
import sys
from view.__settings__ import TITLE_FONT, TEXT_FONT, CYAN, INDIGO_DYE, GHOST_WHITE, AGRESSIVE_PINK, CELESTE
from view.menu import Menu
from view.interface import Interface

class SettingsMenu(Menu):
    def __init__(self, caption="Settings"):
        super().__init__(caption)
        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0
        self.resolutions = ["1080x720", "720x450"]
        self.resolution_index = 0
        self.languages = ["fr", "eng"]
        self.language_index = 0

    def special_button(self, button_text, center, background=GHOST_WHITE, background_hovered=AGRESSIVE_PINK, color=INDIGO_DYE, color_hover=GHOST_WHITE, font=TEXT_FONT):
        special_button_rect = pygame.Rect(
            0, 0,
            self.win_width - self.border_thickness * 2, self.button_height
        )
        special_button_rect.center = center

        mouse_position = pygame.mouse.get_pos()
        hovered = special_button_rect.collidepoint(mouse_position)

        actual_bg_color = background_hovered if hovered else background
        pygame.draw.rect(self.screen, actual_bg_color, special_button_rect)

        actual_font_color = color_hover if hovered else color
        button_draw_text = self.draw_setting_text(button_text, font, special_button_rect.height - 10, center, actual_font_color)

        button_draw_text.height = self.button_height
        button_draw_text.width = self.win_width - self.border_thickness * 2

        if hovered and pygame.mouse.get_pressed()[0]:
            return special_button_rect
        else:
            return special_button_rect
        
    def draw_setting_text(self, text, font, font_size, position, color=INDIGO_DYE):
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center=position)
        self.screen.blit(dialog, dialog_rect)
        return dialog_rect 

    def option_button(self, label, options, index, center):
        # Positionne le bouton du label à gauche
        label_button = self.special_button(f"{label}:", center=(center[0] - 100, center[1]), background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TEXT_FONT)
        
        # Récupère le texte de l'option sélectionnée
        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]

        # Positionne le bouton de l'option à droite du label
        option_button = self.special_button(option_text, center=(label_button.right + 50, center[1]), background=CYAN, background_hovered=AGRESSIVE_PINK, color=GHOST_WHITE, color_hover=INDIGO_DYE, font=TEXT_FONT)

        # Ajuste les positions des boutons "<" et ">"
        left_button = pygame.Rect(option_button.left - 60, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_button.right + 10, center[1] - 15, 30, 30)

        # Vérifie que les boutons ne dépassent pas la fenêtre
        screen_width = self.win_width
        if left_button.left < 0:
            left_button.left = 0
        if right_button.right > screen_width:
            right_button.right = screen_width

        # Dessine les boutons "<" et ">"
        pygame.draw.rect(self.screen, INDIGO_DYE, left_button)
        pygame.draw.rect(self.screen, AGRESSIVE_PINK, right_button)

        # Affiche les symboles "<" et ">" dans leurs boutons respectifs
        self.draw_setting_text("<", TEXT_FONT, 24, (left_button.centerx, left_button.centery), color=INDIGO_DYE)
        self.draw_setting_text(">", TEXT_FONT, 24, (right_button.centerx, right_button.centery), color=INDIGO_DYE)

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
    
    def apply_settings(self):
        print(f"Paramètres appliqués :\n"
            f"Difficulté: {self.difficulties[self.difficulty_index]}\n"
            f"Résolution: {self.resolutions[self.resolution_index]}\n"
            f"Langue: {self.languages[self.language_index]}")

        if self.resolutions[self.resolution_index] == "1080x720":
            self.win_width = 1080
            self.win_height = 720
        elif self.resolutions[self.resolution_index] == "720x450":
            self.win_width = 720
            self.win_height = 450

        if self.languages[self.language_index] == "fr":
            print("Langue changée en Français")
        elif self.languages[self.language_index] == "eng":
            print("Language changed to English")

    def get_single_setting(self, setting_name):
        settings = {
            "Difficulté": (self.difficulties[self.difficulty_index], self.difficulty_index),
            "Résolution": (self.resolutions[self.resolution_index][0], self.resolution_index),
            "Langue": (self.languages[self.language_index], self.language_index),
        }

        valeur, index = settings.get(setting_name, ("Paramètre invalide", -1))

        print(f"{setting_name} actuelle : {valeur} (Index: {index})")

        return valeur, index

    def draw_window_settings(self, controller):
        self.reset_background_screen()
        self.draw_menu_window()

        self.draw_setting_text("Paramètres", TITLE_FONT, self.height // 9, self.title_center, color=CELESTE)

        # Drawing buttons for difficulty, resolution, and language
        self.left_difficulty, self.right_difficulty = self.option_button("Difficulté", self.difficulties, self.difficulty_index, (self.screen_center[0], self.screen_center[1] - self.height // 8 * 1.5))
        self.left_resolution, self.right_resolution = self.option_button("Résolution", self.resolutions, self.resolution_index, (self.screen_center[0], self.screen_center[1] - self.height // 8 * 0.5))
        self.left_language, self.right_language = self.option_button("Langue", self.languages, self.language_index, (self.screen_center[0], self.screen_center[1] + self.height // 8 * 0.5))

        # Drawing the apply and return buttons
        self.button_apply = self.special_button("Appliquer", 
                                                (self.screen_center[0] - self.width // 6,  
                                                 self.screen_center[1] + self.height // 8 * 1.5))
        self.button_return = self.special_button("Retour", 
                                                 (self.screen_center[0] + self.width // 6,  
                                                  self.screen_center[1] + self.height // 8 * 1.5))

        # Event handling loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Vérifie si le clic est à l'intérieur des zones de chaque bouton
                    if self.left_difficulty.collidepoint(event.pos):
                        print("Clic sur le bouton gauche de la difficulté")
                        self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulties)
                    if self.right_difficulty.collidepoint(event.pos):
                        print("Clic sur le bouton droit de la difficulté")
                        self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)

                    if self.left_resolution.collidepoint(event.pos):
                        print("Clic sur le bouton gauche de la résolution")
                        self.resolution_index = (self.resolution_index - 1) % len(self.resolutions)
                    if self.right_resolution.collidepoint(event.pos):
                        print("Clic sur le bouton droit de la résolution")
                        self.resolution_index = (self.resolution_index + 1) % len(self.resolutions)

                    if self.left_language.collidepoint(event.pos):
                        print("Clic sur le bouton gauche de la langue")
                        self.language_index = (self.language_index - 1) % len(self.languages)
                    if self.right_language.collidepoint(event.pos):
                        print("Clic sur le bouton droit de la langue")
                        self.language_index = (self.language_index + 1) % len(self.languages)

                    if self.button_return.collidepoint(event.pos):
                        print("Retour au menu")
                        running = False

                    if self.button_apply.collidepoint(event.pos):
                        print("Application des paramètres")
                        self.apply_settings()  
                        self.get_single_setting("Difficulté")
                        self.get_single_setting("Résolution")
                        self.get_single_setting("Langue")

            pygame.display.update()  
        return self.button_return
