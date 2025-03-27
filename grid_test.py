from view.menu import Menu
import pygame
import sys
from view.__settings__ import NOT_SO_GHOST_WHITE, GHOST_WHITE, CERULEAN
import random

actual_screen = Menu('Grille de jeu')

# pygame.display.get_surface().fill((NOT_SO_GHOST_WHITE))  # background

class Board():
    # alphabet = string.ascii_uppercase
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid_node_width = 20  
        self.grid_node_height = 20
        self.bomb_positions = self.get_bomb_positions_list()


        self.grid_surface_tuple = (actual_screen.win_width//3*2, actual_screen.win_height//3*2)

        self.grid_rect = pygame.Rect(actual_screen.window_rect.topleft[0],
                                     actual_screen.window_rect.topleft[1],
                                     self.grid_surface_tuple[0],
                                    self.grid_surface_tuple[1])
        
        self.grid_rect_draw = pygame.draw.rect(actual_screen.screen,
                                               'black',
                                               self.grid_rect,
                                               border_radius=actual_screen.border_radius)

        self.grid_border = pygame.draw.rect(actual_screen.screen,
                                         CERULEAN,
                                         actual_screen.window_rect,
                                         actual_screen.border_thickness,
                                         border_radius=actual_screen.border_radius)
        # self.grid_surface_tuple = (actual_screen.width//3*2, actual_screen.height//3*2)
        
        # pygame.display.get_surface()
        # grid_surface = pygame.display.set_mode(grid_surface_tuple)
        # self.grid_surface = pygame.surface.Surface(self.grid_surface_tuple)
        # self.grid_fill_rect = self.grid_surface.get_rect()
        # self.grid_fill_rect.center = actual_screen.screen_center
        # self.grid_fill = self.grid_surface.fill('black')
        # self.grid_display = actual_screen.screen.blit(self.grid_surface, self.grid_fill_rect)

        self.grid_top_left = self.grid_rect.topleft

        self.board = self.create_board()



        # self.board[5][6] = 1
    
    def clear_previous_emplacement(self, x, y):
        self.board[y][x] = None

    # def create_board(self):
    #     board = []
    #     row_list = []
    #     x = self.grid_top_left[0]
    #     y = self.grid_top_left[1]

    #     for index in range(self.rows):
    #         row_list = []
    #         for other_index in range(self.columns):
    #             content = None
    #             row_list.append(content)
    #             # self.createSquare(NOT_SO_GHOST_WHITE, x, y)
    #         board.append(row_list)
    #     return board
    
    def createSquare(self,  color, x, y):
        actual_square = pygame.rect.Rect([x, y, self.grid_node_width, self.grid_node_height])
        pygame.draw.rect(actual_screen.screen, color, actual_square)

        return actual_square
    
    def uupdate_board(self):
        x = self.grid_top_left[0]
        y = self.grid_top_left[1]
        for index in range(self.rows): # rows
            for other_index in range(self.columns):
                y += self.grid_node_height
                if index % 2 == 0 and other_index % 2 == 0:
                    # self.board[index][other_index] = 1
                    self.createSquare(GHOST_WHITE, x, y)
                else:
                    self.createSquare(NOT_SO_GHOST_WHITE, x, y)
            
            x += self.grid_node_width
            # print(index)


    def create_board(self):
        y = self.grid_top_left[0] - 50
        x = self.grid_top_left[1] + 80
        board = []
        
        for index in range(self.rows): # rows
            row_list = []

            for other_index in range(self.columns):
                if index % 2 == 0:
                    if other_index % 2 == 0:
                        square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                        content = [square_hitbox, None]
                    else:
                        square_hitbox = self.createSquare(GHOST_WHITE, x, y)
                        content = [square_hitbox, None]
                else:
                    if other_index % 2 != 0:
                        square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                        content = [square_hitbox, None]
                    else:
                        square_hitbox = self.createSquare(GHOST_WHITE, x, y)
                        content = [square_hitbox, None]
                
                row_list.append(content)
                x += self.grid_node_width 
            board.append(row_list)
            x = self.grid_top_left[1] + 80
            y += self.grid_node_height
            # print(board)
        return board
    
    def check_square_surroundings(self, hitbox, row, column):
        bomb_count = 0
        bomb_count_list = []
        
        if row == 0:
            min_row_range = 0
            max_row_range = row + 2
        elif row == self.rows:
            min_row_range = row - 1
            max_row_range = row
        else:
            min_row_range = row - 1
            max_row_range = row + 2
            
        if column == 0:
            min_column_range = 0
            max_column_range = column + 2
        elif column == self.columns:
            min_column_range = column - 1
            max_column_range = column
        else:
            min_column_range = column - 1
            max_column_range = column + 2

            for actual_row in range(min_row_range, max_row_range):
                for actual_col in range(min_column_range, max_column_range):
                    if (actual_row, actual_col) in self.bomb_positions:
                    # if hitbox[actual_row][column-1][1] in self.bomb_positions:
                        bomb_count += 1
                        bomb_count_list.append(bomb_count)
            print(bomb_count_list)

        # (row-1 , column-1) (row-1, column) (row-1, column+1)
        # (row , column-1)                   (row, column+1)
        # (row+1 , column-1) (row+1, column) (row+1, column+1)
        
        pass
    
    def check_user_click(self,row, column, mouse_position, hitbox):
        if hitbox[0].collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            if (row, column) in self.bomb_positions:
                print("AIE, raté ! Il y avait une bombe , tu as perdu")
            else:
                self.check_square_surroundings(hitbox, row, column)
                # hitbox[1] = 2
                hitbox[0] = self.createSquare('red',
                            hitbox[0].topleft[0],
                            hitbox[0].topleft[1])
                
                # print(hitbox[0].topleft)
                # print(f'value of square = {hitbox[1]}')
    

    def go_through_board(self):
        mouse_position = pygame.mouse.get_pos()
        for row in range(self.rows):
            for column in range(self.columns):
                hitbox = self.board[row][column]
                self.check_user_click(row, column, mouse_position, hitbox)
    
    def get_random_position_tuple(self):
        x = random.randrange(self.rows)
        y = random.randrange(self.columns)
        position = (x,y)
        return position

    def get_bomb_positions_list(self):

        bomb_positions_list = []

        bomb_number = random.randrange(10)
        for bomb in range(0, 11):
            position = self.get_random_position_tuple()
            if position in bomb_positions_list:
                position = self.get_random_position_tuple()
            bomb_positions_list.append(position)
        print(bomb_positions_list)
        return bomb_positions_list
                

    
        

# we use the sizes to draw as well as to do our "steps" in the loops. 
matrix = Board(5,5)
# matrix_grid = matrix.create_board()



# visualizeGrid()  # call the function    
while True:
    

    actual_screen.update()
    board = matrix.create_board()
    matrix.go_through_board()
    # matrix.visualizeGrid()  # call the function    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
        
            print("A key has been pressed")

    
    
      # keeps the window open so you can see the result.