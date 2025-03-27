import pygame
from view.__settings__ import RESOLUTION, INDIGO_DYE, TITLE_FONT, TEXT_FONT, MINE_ICON, AGRESSIVE_PINK, CYAN, GHOST_WHITE, NOT_SO_GHOST_WHITE
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
        self.reset_background_screen()
        self.icon = pygame.display.set_icon(pygame.image.load(MINE_ICON)) # icon on the windows

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.fps)

    def reset_background_screen(self):
        self.screen.fill(self.background_color)
        
        
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

    def small_button(self, button_text, center, background=CYAN, background_hovered=AGRESSIVE_PINK, color=INDIGO_DYE, color_hover=GHOST_WHITE):
        # Create rectangle for text -> self.button_height//2 = font_size
        button_draw_text, button_text_rect = self.create_text_rect(button_text,
                                            TEXT_FONT,
                                            self.button_height//2,
                                            center)

        button_text_rect.width = button_text_rect.width + 30
        button_text_rect.height = button_text_rect.height + 20
        button_text_rect.center = center

        mouse_position = pygame.mouse.get_pos()
        hovered = button_text_rect.collidepoint(mouse_position)

        actual_bg_color = background_hovered if hovered else background
        actual_font_color = color_hover if hovered else color

        # Create rectangle for small button
        small_button = pygame.Rect(
            0, 0,
            button_text_rect.width, button_text_rect.height
        )
        small_button.center = center
       
        # Draw rectangle and text for button
        pygame.draw.rect(self.screen, actual_bg_color, small_button, border_radius=self.border_radius)
        button_draw_text, button_text_rect = self.create_text_rect(button_text,
                                            TEXT_FONT,
                                            self.button_height//2,
                                            center,
                                            actual_font_color)
        self.blit_text_from_rect(button_draw_text, button_text_rect)

        if hovered and pygame.mouse.get_pressed()[0]:
            print(button_text)
            return True
        else:
            return False
            # return something usefull, I guess

