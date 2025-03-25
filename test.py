import pygame, sys
# import pygame_menu
# import pygame_menu.themes
from view.__settings__ import CUSTOM_THEME, RESOLUTION, INDIGO_DYE, TITLE_FONT, GHOST_WHITE, CELESTE, TEXT_FONT, FPS, CERULEAN
from view.interface import Interface
from view.menu import Menu
from view.button import Button
pygame.init()

screen_main_menu = Menu('Minesweeper - Main menu')

while True:
    print("hahahahahaha")
    my_title = screen_main_menu.draw_text('Minesweeper', TITLE_FONT, screen_main_menu.height//9, screen_main_menu.title_center, color=CELESTE)
    

    button_play = screen_main_menu.draw_full_button('Jouer', (screen_main_menu.screen_center[0],
                        screen_main_menu.screen_center[1]- screen_main_menu.height//8*1.5))
    
    button_settings = screen_main_menu.draw_full_button('Paramètres',
                            (screen_main_menu.screen_center[0],
                            screen_main_menu.screen_center[1]- screen_main_menu.height//8*0.5))
    button_record = screen_main_menu.draw_full_button('Palmarès', 
                            (screen_main_menu.screen_center[0],
                            screen_main_menu.screen_center[1] + screen_main_menu.height//8*0.5))
    # button_quit = screen_main_menu.draw_full_button('Quitter', 
    #                         (screen_main_menu.screen_center[0],
    #                         screen_main_menu.screen_center[1] + screen_main_menu.height//8*1.5))

    small_button = screen_main_menu.small_button('POO PI POO PI POOOOO',
                            (screen_main_menu.screen_center[0],
                            screen_main_menu.screen_center[1] + screen_main_menu.height//8*1.5))

    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
        
            print("A key has been pressed")

    screen_main_menu.update()
     
pygame.quit()