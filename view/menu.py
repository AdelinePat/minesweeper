from view.interface import Interface
from view.__settings__ import GHOST_WHITE, CERULEAN, AGRESSIVE_PINK, TEXT_FONT, INDIGO_DYE, CYAN, NOT_SO_GHOST_WHITE 
import pygame

class Menu(Interface):
    def __init__(self, caption, identification=0):
        super().__init__(caption) 
        self.identification = identification # main_menu, settings_menu, wall_of_fame_screen, winner_screen
        self.win_bg_color=GHOST_WHITE
        self.win_width = self.width // 3*2
        self.win_height = self.height // 3*2
        self.border_thickness = 5
        self.border_radius = 15
        self.button_height = self.height // 12
        self.draw_menu_window()
    
    def draw_menu_window(self):
        self.window_rect =  pygame.Rect(
            0,0,
            self.win_width, self.win_height)
        self.window_rect.center = self.screen_center
        window = pygame.draw.rect(self.screen, self.win_bg_color, self.window_rect, border_radius=self.border_radius)
        window_border = pygame.draw.rect(self.screen, CERULEAN, self.window_rect, self.border_thickness, border_radius=self.border_radius)

    def draw_full_button(self, button_text, center, background=GHOST_WHITE, background_hovered=AGRESSIVE_PINK, color=INDIGO_DYE, color_hover=GHOST_WHITE):
        hovered_button = pygame.Rect(
            0, 0,
            self.win_width - self.border_thickness*2, self.button_height
        )
        hovered_button.center = center

        mouse_position = pygame.mouse.get_pos()
        hovered = hovered_button.collidepoint(mouse_position)

        actual_bg_color = background_hovered if hovered else background
        pygame.draw.rect(self.screen, actual_bg_color, hovered_button)

        actual_font_color = color_hover if hovered else color
        button_draw_text = self.draw_text(button_text, TEXT_FONT, hovered_button.height-10, center, actual_font_color)
       
        button_draw_text.height=self.button_height
        button_draw_text.width=self.win_width - self.border_thickness*2

        if hovered and pygame.mouse.get_pressed()[0]:
            print(button_text)
            # return something usefull, I guess

        return hovered_button

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
        # small_button.center = center
        
        # Change button size (width and height) depending on text length
        # small_button.width = button_text_rect.width + 30
        # small_button.height = button_text_rect.height + 20
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
            # return button_text

        return small_button

