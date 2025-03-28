import pygame
import sys

pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Dimensions de la fenêtre
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Settings")

FONT = pygame.font.Font(None, 30)


class Settings:
    def __init__(self):
        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0
        self.resolutions = [("1080x720", (1080, 720)), ("720x450", (720, 450))]
        self.resolution_index = 0
        self.languages = ["fr", "eng"]
        self.language_index = 0

    def draw_text(self, text, position, color=BLACK):
        text_surface = FONT.render(text, True, color)
        screen.blit(text_surface, position)

    def draw_button(self, text, center):
        button_rect = pygame.Rect(0, 0, 140, 40)
        button_rect.center = center
        pygame.draw.rect(screen, GRAY, button_rect, border_radius=10)
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)
        return button_rect

    def option_button(self, label, options, index, center):
        label_surface = FONT.render(f"{label}:", True, BLACK)
        label_rect = label_surface.get_rect(midright=(center[0] - 100, center[1]))

        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]
        option_surface = FONT.render(option_text, True, BLACK)
        option_rect = option_surface.get_rect(midleft=(label_rect.right + 50, center[1]))

        left_button = pygame.Rect(option_rect.left - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_rect.right + 10, center[1] - 15, 30, 30)

        pygame.draw.rect(screen, GRAY, left_button)
        pygame.draw.rect(screen, GRAY, right_button)

        screen.blit(label_surface, label_rect)
        screen.blit(option_surface, option_rect)

        self.draw_text("<", (left_button.centerx - 5, left_button.centery - 10), BLACK)
        self.draw_text(">", (right_button.centerx - 5, right_button.centery - 10), BLACK)

        return left_button, right_button

    def get_current_settings(self):
        settings = {
            "Difficulté": self.difficulties[self.difficulty_index],
            "Résolution": self.resolutions[self.resolution_index][0],
            "Langue": self.languages[self.language_index],
        }

        print("\nParamètres appliqués :")
        for key, value in settings.items():
            print(f"{key}: {value}")

        return settings
    
    def get_single_setting(self, setting_name):
        """Récupère la valeur et l'index d'un seul paramètre et l'affiche."""
        settings = {
            "Difficulté": (self.difficulties[self.difficulty_index], self.difficulty_index),
            "Résolution": (self.resolutions[self.resolution_index][0], self.resolution_index),  # On ne garde que le texte
            "Langue": (self.languages[self.language_index], self.language_index),
        }

        valeur, index = settings.get(setting_name, ("Paramètre invalide", -1))

        # Affichage automatique
        print(f"{setting_name} actuelle : {valeur} (Index: {index})")

        return valeur, index


    def apply_settings(self):
        settings = self.get_current_settings()
        print("Les paramètres ont été appliqués !")
        return settings  # Tu peux utiliser cette valeur pour les sauvegarder

    def draw_settings_screen(self):
        running = True
        while running:
            screen.fill(WHITE)

            # Position des options
            left_difficulty, right_difficulty = self.option_button(
                "Difficulté", self.difficulties, self.difficulty_index, (SCREEN_WIDTH // 2, 60)
            )
            left_resolution, right_resolution = self.option_button(
                "Résolution", self.resolutions, self.resolution_index, (SCREEN_WIDTH // 2, 120)
            )
            left_language, right_language = self.option_button(
                "Langue", self.languages, self.language_index, (SCREEN_WIDTH // 2, 180)
            )

            # Boutons Retour et Appliquer
            button_back = self.draw_button("Retour", (SCREEN_WIDTH // 3, 240))
            button_apply = self.draw_button("Appliquer", (2 * SCREEN_WIDTH // 3, 240))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if left_difficulty.collidepoint(event.pos):
                        self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulties)
                    if right_difficulty.collidepoint(event.pos):
                        self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)

                    if left_resolution.collidepoint(event.pos):
                        self.resolution_index = (self.resolution_index - 1) % len(self.resolutions)
                    if right_resolution.collidepoint(event.pos):
                        self.resolution_index = (self.resolution_index + 1) % len(self.resolutions)

                    if left_language.collidepoint(event.pos):
                        self.language_index = (self.language_index - 1) % len(self.languages)
                    if right_language.collidepoint(event.pos):
                        self.language_index = (self.language_index + 1) % len(self.languages)

                    if button_back.collidepoint(event.pos):
                        print("Retour au menu")
                        running = False

                    if button_apply.collidepoint(event.pos):
                        self.apply_settings()  # Applique les paramètres

                         # Afficher chaque paramètre individuellement
                        self.get_single_setting("Difficulté")
                        self.get_single_setting("Résolution")
                        self.get_single_setting("Langue")


            pygame.display.flip()


# Lancer la fenêtre des paramètres
settings = Settings()
settings.draw_settings_screen()

pygame.quit()
sys.exit()
