import pygame
import sys
from view.__settings__ import TITLE_FONT, TEXT_FONT, CYAN, INDIGO_DYE, GHOST_WHITE, AGRESSIVE_PINK,CELESTE, DIFFICULTY, RESOLUTIONS, LANGUAGES
from view.menu import Menu
from view.interface import Interface


class SettingsMenu(Menu):
    def __init__(self, game_controller, data_access, caption="Paramètres"):
        super().__init__(caption)
        self.caption = caption
        self.difficulties = DIFFICULTY
        self.difficulty_index = 0
        self.resolutions = RESOLUTIONS
        self.resolution_index = 0
        self.languages = LANGUAGES
        self.yes_no_choice = ['Oui', 'Non']
        self.yes_index = 1
        self.language_index = 0
        self.game_controller = game_controller
        self.data_access = data_access
        
        self.get_resolution(self.resolution)

    def option_button(self, option_surface, label, options, index, center):
        if options == self.resolutions:
            pass
            
        label_rect = self.draw_text(f"{label}",
                       TEXT_FONT,
                       self.height//18,
                       (option_surface.midleft[0] + self.win_width // 4, option_surface.midleft[1])
                       )
        
        option_text = options[index][0] if isinstance(options[index], tuple) else options[index]
        if options == self.resolutions:
            option_text = f'{self.resolutions[index][0]}x{self.resolutions[index][1]}'
        
        option_rect = self.draw_text(str(option_text), TEXT_FONT, self.height//18, (option_surface.midright[0] - self.win_width // 4, option_surface.midright[1]), color=AGRESSIVE_PINK)


        return option_rect

    def arrow_button(self, button_text, center, option_index,  options, left_right, background=CYAN, background_hovered=AGRESSIVE_PINK, color=INDIGO_DYE, color_hover=GHOST_WHITE):
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

        return self.check_arrow_click(hovered, option_index, options, left_right)

    def check_arrow_click(self, hovered, option_index, options, left_right):

        if hovered and pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
            return option_index   
        elif hovered and not pygame.mouse.get_pressed()[0] and self.clicked:
            self.clicked = False
            if left_right == 'left':
                option_index = (option_index - 1) % len(options)
                return option_index
            elif left_right == 'right':
                option_index = (option_index + 1) % len(options)
                return option_index
        else:
            return option_index


    def draw_arrow_button(self, option_rect, option_index, options):
        actual_index = self.arrow_button("<",
                        (option_rect.midleft[0] - 30 , option_rect.midleft[1]),
                        option_index,
                        options,
                        'left')
        
        actual_index = self.arrow_button(">",            
                        (option_rect.midright[0] + 30, option_rect.midright[1]),
                        actual_index,
                        options,
                        'right')
        return actual_index

    def get_current_settings(self):
            self.game_controller.resolution = self.resolutions[self.resolution_index]

            self.game_controller.language = self.languages[self.language_index]
            self.game_controller.difficulty = self.difficulty_index
            self.game_controller.difficulty_string = self.difficulties[self.difficulty_index]
            self.game_controller.reset_top_3 = self.yes_index
            if self.game_controller.reset_top_3 == 0:
                self.data_access.reset_top_3_players()
                self.yes_index = 1
                self.game_controller.reset_top_3 = self.yes_index


            self.get_resolution(self.game_controller.resolution)
            self.get_actual_menu_window()
            self.draw_menu_window()

            
            settings = (
                (self.difficulty_index, self.difficulties[self.difficulty_index]),
                (self.resolution_index, self.resolutions[self.resolution_index]),
                (self.language_index, self.languages[self.language_index]),
            )
            return settings

    def apply_settings(self):
        settings = self.get_current_settings()
        return settings 
    
    def draw_window_settings(self, controller):
        self.set_caption(self.caption)
        self.reset_background_screen()
        self.draw_menu_window()

        self.draw_text("Paramètres",
                        TITLE_FONT,
                        self.height//9,
                        self.title_center,
                        color=CELESTE)
        
       # Create row surface for blitting option labels, button and option
        difficulty_surface = self.get_full_rect((self.screen_center[0], self.screen_center[1] - self.height // 8 * 1.5))
        resolution_surface = self.get_full_rect((self.screen_center[0], self.screen_center[1] - self.height // 8 * 0.5))
        yes_no_choice_surface = self.get_full_rect((self.screen_center[0], self.screen_center[1] + self.height // 8 * 0.5))
        
        option_difficulty_rect = self.option_button(difficulty_surface,
                "Difficulté", self.difficulties, self.difficulty_index, (self.width // 2, 60)
            )
        
        self.difficulty_index = self.draw_arrow_button(option_difficulty_rect, self.difficulty_index, self.difficulties)

        yes_no_choice_options = self.option_button(yes_no_choice_surface,
            "Supprimer le top 3", self.yes_no_choice, self.yes_index, (self.width // 2, 120)
        )
        self.yes_index = self.draw_arrow_button(yes_no_choice_options,
            self.yes_index, self.yes_no_choice)
        
        option_resolution_rect = self.option_button(resolution_surface,
            "Résolution", self.resolutions, self.resolution_index, (self.width // 2, 120)
        )
        self.resolution_index = self.draw_arrow_button(option_resolution_rect,
            self.resolution_index, self.resolutions)

        yes_no_choice_options = self.option_button(yes_no_choice_surface,
            "Supprimer le top 3", self.yes_no_choice, self.yes_index, (self.width // 2, 120)
        )
        self.yes_index = self.draw_arrow_button(yes_no_choice_options,
            self.yes_index, self.yes_no_choice)

        # Return button and Apply button to save parameters
        self.button_return = self.small_button("Retour",
                                (self.screen_center[0] - self.win_width // 4,
                                self.screen_center[1] + self.height//8*1.5))
        self.button_apply = self.small_button("Appliquer",
                                        (self.screen_center[0] + self.win_width // 4,
                                self.screen_center[1] + self.height//8*1.5))
        
        if self.button_apply:
            self.apply_settings()

        return self.button_return  