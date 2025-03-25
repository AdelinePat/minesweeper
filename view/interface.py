import pygame
from view.__settings__ import RESOLUTION, INDIGO_DYE, TITLE_FONT, TEXT_FONT
class Interface():
    def __init__(self, caption, width=RESOLUTION[0], height=RESOLUTION[1], background_color=INDIGO_DYE):
        self.width=width
        self.height=height
        self.resolution = (self.width, self.height)
        self.screen = pygame.display.set_mode((self.resolution))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.fps = 144
        self.background_color = background_color
        self.screen_center = (self.width//2, self.height//2)
        self.title_center = (self.width//2, self.height//12)
        self.screen.fill(self.background_color)
        # self.icon = pygame.display.set_icon(pygame.image.load("path")) # If we want an icon for the window

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.fps)    
        
    # def get_title_font(self):
    #     title_font_load = pygame.font.Font(jockey_one, font_size) # load font then text_font.render('text', true, color)
    #     return title_font_load
    
    # def get_text_font(self):
    #     title_text_load = pygame.font.Font(jersey_10, font_size) # load font then text_font.render('text', true, color)
    #     return title_text_load
    def create_text_rect(self, text, font, font_size, position, color=INDIGO_DYE):
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center=position)
        return dialog, dialog_rect
    
    def blit_text_from_rect(self, dialog, dialog_rect):
        self.screen.blit(dialog, dialog_rect)


    def draw_text(self, text, font, font_size, position, color=INDIGO_DYE):
        # dialog, dialog_rect = self.create_text_rect()
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center=position)
        self.screen.blit(dialog, dialog_rect)
        return dialog_rect
    
    # def draw_button_text(self, text, font, font_size, position, color=INDIGO_DYE)
