# from view.in_game_menu import InGameMenu
from model.game_board import GameBoard
import pygame
import sys

my_menu = GameBoard('grille de jeu')

board = my_menu.create_board()
while True:
    

    my_menu.update()
    # my_menu.draw_in_game_screen()
    # my_menu.go_through_board()
    my_menu.draw_in_game_screen()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
        
            print("A key has been pressed")