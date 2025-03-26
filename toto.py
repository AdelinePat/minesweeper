import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Définition de la fenêtre
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Settings")

# Police d'écriture
FONT = pygame.font.Font(None, 40)

class Settings:
    def __init__(self):
        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0

    def draw_text(self, text, position, color=BLACK):
        """Affiche du texte à l'écran"""
        text_surface = FONT.render(text, True, color)
        screen.blit(text_surface, position)

    def option_button(self, index, center):
        """Crée des boutons < et > et affiche l'option actuelle avec 'Difficulté:' devant"""
        # Texte "Difficulté:"
        difficulty_label = FONT.render("Difficulté:", True, BLACK)
        difficulty_rect = difficulty_label.get_rect(midright=(center[0] - 100, center[1]))  

        # Option actuelle
        option_text = self.difficulties[index]
        option_surface = FONT.render(option_text, True, BLACK)
        option_rect = option_surface.get_rect(midleft=(difficulty_rect.right + 50, center[1]))

        # Création des boutons < et >
        left_button = pygame.Rect(option_rect.left - 40, center[1] - 15, 30, 30)
        right_button = pygame.Rect(option_rect.right + 10, center[1] - 15, 30, 30)

        # Dessin des rectangles des boutons
        pygame.draw.rect(screen, GRAY, left_button)
        pygame.draw.rect(screen, GRAY, right_button)

        # Dessin du texte de "Difficulté" et de l'option
        screen.blit(difficulty_label, difficulty_rect)
        screen.blit(option_surface, option_rect)

        # Dessin des flèches alignées avec le texte
        # Flèche gauche "<"
        self.draw_text("<", (left_button.centerx - 10, left_button.centery - 15), BLACK)
        # Flèche droite ">"
        self.draw_text(">", (right_button.centerx - 10, right_button.centery - 15), BLACK)

        return left_button, right_button, index, option_text

    def draw_settings_screen(self):
        """Affiche l'écran des paramètres et gère les interactions"""
        running = True
        while running:
            screen.fill(WHITE)  # Efface l'écran

            # Création des boutons et affichage de l'option
            left_button, right_button, index, option_text = self.option_button(
                self.difficulty_index, (WIDTH // 2, HEIGHT // 2)
            )


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if left_button.collidepoint(event.pos):
                        self.difficulty_index = (self.difficulty_index - 1) % len(self.difficulties)
                    if right_button.collidepoint(event.pos):
                        self.difficulty_index = (self.difficulty_index + 1) % len(self.difficulties)

            pygame.display.flip() 


settings = Settings()
settings.draw_settings_screen()

pygame.quit()
sys.exit()
