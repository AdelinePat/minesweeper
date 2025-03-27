import pygame, sys

from controller.menu_controller import MenuController
from controller.game_controller import GameController
from view.__settings__ import TITLE_FONT, CELESTE
from view.interface import Interface
from view.menu_copy import Menu

class SomeClass:
    def __init__(self):
        self.controller = MenuController()  



class WinnerButton:
    def __init__(self):
        self.menu = Menu('Bravo vous avez gagné')
        self.controller = MenuController()
        self.game_controller = GameController()

    def main_loop(self):
        pygame.init()

        while True:
     
            

            
            

            self.controller.is_screen_in_game = self.menu.draw_subtitle(
                "Veuillez entrer votre nom dans l'histoire",
                (self.menu.screen_center[0],
                 self.menu.screen_center[1] - self.menu.height // 8*0.01)
            )

            

            button_return = self.menu.medium_button(
                'Retour',
                (self.menu.screen_center[0],
                 self.menu.screen_center[1] + self.menu.height // 8*2.7)
            )

            self.controller.screen_access()

            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_return.collidepoint(mouse_position):
                        
                        self.controller.return_menu_principal()  
                        return  

                if event.type == pygame.KEYDOWN:
                    print("A key has been pressed")

            self.menu.update()

        pygame.quit()

if __name__ == "__main__":
    winner_button = WinnerButton()
    winner_button.main_loop()