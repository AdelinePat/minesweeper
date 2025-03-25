import pygame
from view.__settings__ import CELESTE

class Parametre:
    def __init__(self, title="Settings"):
        self.title = title
        self.width, self.height = 800, 600  # Size of the settings window
        self.screen_center = (self.width // 2, self.height // 2)
        self.title_center = (self.width // 2, self.height // 6)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def draw_text(self, text, font, font_size, position, color=CELESTE):
        """Method to draw text on the screen"""
        font = pygame.font.Font(font, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_full_button(self, text, position):
        """Method to draw a full button on the screen"""
        font = pygame.font.Font(None, 40)
        text_surface = font.render(text, True, (255, 255, 255))  # White text
        button_rect = pygame.Rect(position[0] - 100, position[1] - 25, 200, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), button_rect)  # Blue background
        self.screen.blit(text_surface, (position[0] - text_surface.get_width() // 2, position[1] - text_surface.get_height() // 2))
        
        return button_rect  # Assurez-vous que vous renvoyez bien un Rect

    def update(self):
        """Update the screen (refresh the display)"""
        pygame.display.update()
