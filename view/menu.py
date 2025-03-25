from view.interface import Interface
from view.__settings__ import GHOST_WHITE, CERULEAN, AGRESSIVE_PINK, TEXT_FONT
import pygame

class Menu(Interface):
    def __init__(self, caption):
        super().__init__(caption)
        self.win_bg_color=GHOST_WHITE
        self.win_width = self.width // 3*2
        self.win_height = self.height // 3*2
        self.border_thickness = 5
        self.border_radius = 15
        self.button_height = self.height // 15
        self.draw_menu_window()
    
    def draw_menu_window(self):
        self.window_rect =  pygame.Rect(
            0,0,
            self.win_width, self.win_height)
        self.window_rect.center = self.screen_center
        window = pygame.draw.rect(self.screen, self.win_bg_color, self.window_rect, border_radius=self.border_radius)
        window_border = pygame.draw.rect(self.screen, CERULEAN, self.window_rect, self.border_thickness, border_radius=self.border_radius)
        # print(f"avant recentrage : {window.center}")
    
    def draw_full_button_hovered(self, button_text,  center):
        button_text = self.draw_text(button_text, TEXT_FONT, self.button_height-10, center, color=GHOST_WHITE)
        # print(button_text.height)
        button_text.height=self.button_height
        button_text.width=self.win_width - self.border_thickness*2

    def draw_full_button(self, button_text, center):
        hovered_button = pygame.Rect(
            0, 0,
            self.win_width - self.border_thickness*2, self.button_height
        )
        hovered_button.center = center

        hovered_button_rect = pygame.draw.rect(self.screen, AGRESSIVE_PINK, hovered_button)

        # return hovered_button
        # button = self.draw_full_button(screen.screen_center)
        button_text = self.draw_text(button_text, TEXT_FONT, hovered_button.height-10, center, color=GHOST_WHITE)
        # print(button_text.height)
        button_text.height=self.button_height
        button_text.width=self.win_width - self.border_thickness*2
        # print(button_text.height)

    def small_button(self):
        pass 
        # print(f"après recentrage : {window.center}")

# pygame.display.flip()

