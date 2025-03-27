# from view.menu import Menu
from view.interface import Interface
from view.__settings__ import CELESTE, TITLE_FONT, TEXT_FONT, NOT_SO_GHOST_WHITE, CYAN, GHOST_WHITE, INDIGO_DYE
import random
# from model.game_board import GameBoard
import pygame

pygame.init()
class InGameMenu(Interface):
    def __init__(self, caption):
        super().__init__(caption)
    
    def set_title(self, text):
        self.title = self.draw_text(text,
            TITLE_FONT,
            self.height//9,
            (self.title_center[0] // 4*3, self.title_center[1]),
            color=CELESTE
        )

    def display_game_info(self, text_title, text_content, position_y):
        font = TEXT_FONT
        font_size = self.height // 24
        color = CYAN
        color_content = GHOST_WHITE
        position = (self.width // 4*3, position_y)
        position_content = (self.width // 4*3, position_y + font_size*1.5)
        

        content_rect = self.draw_text(text_content, font, font_size*2, position_content, color_content)

        back_rect = pygame.Rect(0, 0,
                    content_rect.width + 100,
                    content_rect.height)
        
        back_rect.center = content_rect.center
        
        # pygame.draw.rect(content_rect)
        # self.screen, self.win_bg_color, self.window_rect
        pygame.draw.rect(self.screen, INDIGO_DYE, back_rect)
        content_rect = self.draw_text(text_content, font, font_size*2, position_content, color_content)
        title_rect = self.draw_text(text_title, TITLE_FONT, font_size, position, color)
        
        return title_rect
