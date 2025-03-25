import pygame
from view.interface import Interface
class Button():
    def __init__(self, identification, button_rect, screen, win_rect, center):
        # self.text = text
        self.identification = identification
        self.screen = screen
        self.center = center
        self.button_rect = button_rect
        self.button_rect.center  = center
        self.white_win_rect = win_rect
        self.button_rect.width = self.white_win_rect.win_width - self.white_win_rect.border_thickness*2
    
    def draw_full_button(self):
        pass
    def small_button(self):
        pass

    # def draw(self, color):
    #     font_load = pygame.font.Font(self.font, self.font_size)
    #     dialog = font_load.render(self.text, True, color)

    #     dialog_rect = dialog.get_rect(center = self.center)
    #     self.rect = dialog_rect
    #     self.screen.blit(dialog, dialog_rect)

    #     return self.rect
