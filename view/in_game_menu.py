import pygame
from view.interface import Interface
from view.__settings__ import CELESTE, TITLE_FONT, TEXT_FONT, CYAN, GHOST_WHITE, INDIGO_DYE

pygame.init()
class InGameMenu(Interface):
    def __init__(self, caption):
        super().__init__(caption)
        self.get_resolution(self.resolution)
        self.set_caption(self.caption)
    

    def set_title(self, text, font_size=None):
        if font_size == None:
            font_size = self.height//9
        else:
            font_size = font_size

        self.title = self.draw_text(text,
            TITLE_FONT,
            font_size,
            (self.title_center[0] // 4*3, self.title_center[1]),
            color=CELESTE
        )

        back_rect = pygame.Rect(0, 0,
                    self.title.width + 100,
                    self.title.height)
        back_rect.center = self.title.center

        pygame.draw.rect(self.screen, INDIGO_DYE, back_rect)
        
        self.title = self.draw_text(text,
            TITLE_FONT,
            font_size,
            (self.title_center[0] // 4*3, self.title_center[1]),
            color=CELESTE
        )
    
    def set_bottom_text(self, text, font_size=None):
        if font_size == None:
            font_size = self.height//9
        else:
            font_size = font_size

        self.bottom_title = self.draw_text(text,
            TITLE_FONT,
            font_size,
            (self.title_center[0] // 4*3,self.height//1.1),
            color=CELESTE
        )

        back_rect = pygame.Rect(0, 0,
                    self.bottom_title.width + 100,
                    self.bottom_title.height)
        back_rect.center = self.bottom_title.center

        pygame.draw.rect(self.screen, INDIGO_DYE, back_rect)
        
        self.bottom_title = self.draw_text(text,
            TITLE_FONT,
            font_size,
            (self.title_center[0] // 4*3,self.height//1.1),
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
