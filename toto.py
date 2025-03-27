import pygame
import sys
from view.menu import Menu

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Settings")

FONT = pygame.font.Font(None, 40)

class Settings(Menu):
    def __init__(self, caption="Settings"):
        super().__init__(caption)
        self.difficulties = ["Facile", "Difficile"]
        self.difficulty_index = 0
        self.resolutions = [("1080x720", (1080, 720)), ("720x450", (720, 450))]
        self.resolution_index = 0
        self.languages = ["fr", "eng"]
        self.language_index = 0
        self.setting_win = self.draw_menu_window()

    def draw_text(self, text, position, color=BLACK):
        text_surface = FONT.render(text, True, color)
        screen.blit(text_surface, position)

    def draw_button(self, text, center):
    
        button_rect = pygame.Rect(0, 0, 120, 50)
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

        self.draw_text("<", (left_button.centerx - 10, left_button.centery - 15), BLACK)
        self.draw_text(">", (right_button.centerx - 10, right_button.centery - 15), BLACK)

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
            screen.fill(WHITE)

           
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
                        self.get_current_settings()  # Affiche les valeurs mises à jour en console
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


settings = Settings()
settings.draw_settings_screen()

pygame.quit()
sys.exit()
