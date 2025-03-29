from view.__settings__ import MINE_ASSETS, FLAG_ASSETS
import pygame
pygame.init()
class GameInfo():
    def __init__(self):
        self.difficulty = 0 # 0 = Easy, 1 = Difficult , possibility to have more difficulties with time
        self.difficulty_string = "Facile"
        self.language = 'fr' # fr = french, en = english
        self.square_surface = None
        self.mine_img = pygame.image.load(MINE_ASSETS)
        self.flag_img = pygame.image.load(FLAG_ASSETS)
        self.player_name = None
        self.grid_rows = None
        self.grid_columns = None
        self.mines_number = None
        self.flag_number = None
        self.interrogation_point_number = None
        self.mines_positions = None # list of tuples
        self.game_time = None

    def set_mine_resized(self):
        self.mine_img = pygame.transform.smoothscale(self.mine_img.convert_alpha(), (self.square_surface[0] - 6, self.square_surface[1] - 6))
        
    def set_flag_resized(self):
        self.flag_img = pygame.transform.smoothscale(self.flag_img.convert_alpha(), (self.square_surface[0] - 6, self.square_surface[1] - 6))


    
    def set_grid(self):
        match self.difficulty:
            case 0:
                self.grid_rows = 8
                self.grid_columns = 8                   
            case 1:
                self.grid_rows = 12
                self.grid_columns = 12
            case 2:
                self.grid_rows = 15
                self.grid_columns = 15
