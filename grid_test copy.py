from view.menu import Menu
import pygame
import sys
from view.__settings__ import NOT_SO_GHOST_WHITE, GHOST_WHITE, CERULEAN, INDIGO_DYE, TEXT_FONT
import random

actual_screen = Menu('Grille de jeu')
pygame.init()

# pygame.display.get_surface().fill((NOT_SO_GHOST_WHITE))  # background

class Board():
    # alphabet = string.ascii_uppercase
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
        self.bomb_positions = []
        self.click = 0
        self.revealed_square = []


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
        
        self.grid_node_width = (self.grid_rect.height // self.rows)  
        self.grid_node_height = (self.grid_rect.height // self.rows)
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

    
    def draw_text(self, text, font, font_size, position, color=INDIGO_DYE):
        # dialog, dialog_rect = self.create_text_rect()
        font_load = pygame.font.Font(font, font_size)
        dialog = font_load.render(text, True, color)
        dialog_rect = dialog.get_rect(center=position)
        actual_screen.screen.blit(dialog, dialog_rect)
        return dialog_rect

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
                # self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                # if index % 2 == 0:
                #     if other_index % 2 == 0:
                square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                content = [square_hitbox, None]

                if (index, other_index) in self.bomb_positions:
                    content = [square_hitbox, 'bomb']
                #     else:
                #         square_hitbox = self.createSquare(GHOST_WHITE, x, y)
                #         content = [square_hitbox, None]
                # else:
                #     if other_index % 2 != 0:
                #         square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                #         content = [square_hitbox, None]
                #     else:
                #         square_hitbox = self.createSquare(GHOST_WHITE, x, y)
                #         content = [square_hitbox, None]
                
                row_list.append(content)
                x += (self.grid_node_width + 2)
            board.append(row_list)
            x = self.grid_top_left[1] + 80
            y += (self.grid_node_height + 2)
            # print(board)
        return board
    
    def set_range(self, value, max_value):
        if value == 0:
            min_range = 0
            max_range = value + 2
        elif value == (max_value-1):
            min_range = value - 1
            max_range = value 
        else:
            min_range = value - 1
            max_range = value + 2
        
        return min_range, max_range

    

    def count_surrounding_bombs(self, row, column):
        bomb_count = 0
        min_row_range, max_row_range = self.set_range(row, self.rows)
        min_column_range, max_column_range = self.set_range(column, self.columns)
       
        for actual_row in range(min_row_range, max_row_range):
            for actual_col in range(min_column_range, max_column_range):
                if (actual_row, actual_col) in self.bomb_positions:     
                    bomb_count += 1

            # self.board[row][column][1] = bomb_count

        # print(self.board[row][column][1])
        return bomb_count
        
    def set_board_values(self):
        for bomb_position in self.bomb_positions:
            x = bomb_position[0]
            y = bomb_position[1]
            self.board[x][y][1] = 'bomb'

        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column][1] == None:
                    self.board[row][column][1] = self.count_surrounding_bombs(row, column)
                print(f'value at {row},{column} : {self.board[row][column][1]}')

    
    def check_user_click(self,row, column, mouse_position, hitbox):
        if hitbox[0].collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            self.click += 1
            if self.click == 1:
                self.bomb_positions = self.get_bomb_positions_list(row, column)
                self.set_board_values()

            if (row, column) in self.bomb_positions:
                print("AIE, raté ! Il y avait une bombe , tu as perdu")
            else:
                self.reveal_square(row, column)
                # self.count_surrounding_bombs(row, column)
                # hitbox[1] = 2
                hitbox[0] = self.createSquare('green',
                            hitbox[0].topleft[0],
                            hitbox[0].topleft[1])
                
                # print(hitbox[0].topleft)
                # print(f'value of square = {hitbox[1]}')
    def reveal_number(self):
        pass
    def reveal_square(self, row, column):
        min_row_range, max_row_range = self.set_range(row, self.rows)
        min_column_range, max_column_range = self.set_range(column, self.columns)

        
        for actual_row in range(min_row_range, max_row_range):
            for actual_col in range(min_column_range, max_column_range):
                
                if self.board[actual_row][actual_col][1] == 0 and (actual_row,actual_col) not in self.revealed_square:

                    self.createSquare('green',
                        self.board[actual_row][actual_col][0].topleft[0],
                        self.board[actual_row][actual_col][0].topleft[1])
                    
                    # font, font_size, position
                    # self.draw_text(str(self.board[actual_row][actual_col][1]),
                    #                TEXT_FONT,
                    #                self.board[actual_row][actual_col][0].height - 5,
                    #                self.board[actual_row][actual_col][0].center
                    #                )
            
                    position = (actual_row, actual_col)
                    self.revealed_square.append(position)
                    print(position)
                    self.reveal_square(actual_row, actual_col)

                elif self.board[actual_row][actual_col][1] in (1,2,3,4,5,6,7,8):
                    self.draw_text(str(self.board[actual_row][actual_col][1]),
                        TEXT_FONT,
                        self.board[actual_row][actual_col][0].height - 5,
                        self.board[actual_row][actual_col][0].center
                        )
                
        print(self.revealed_square)


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

    def get_bomb_positions_list(self, row, column):

        bomb_positions_list = []

        bomb_number = random.randrange(5,10)

        for bomb in range(0, bomb_number):
            position = self.get_random_position_tuple()
            while position in bomb_positions_list or position == (row, column):
                position = self.get_random_position_tuple()
            bomb_positions_list.append(position)
        print(bomb_positions_list)
        return bomb_positions_list
                

    
        

# we use the sizes to draw as well as to do our "steps" in the loops. 
matrix = Board(10,10)
# matrix_grid = matrix.create_board()


board = matrix.create_board()
# visualizeGrid()  # call the function    
while True:
    

    actual_screen.update()
    
    matrix.go_through_board()
    # matrix.visualizeGrid()  # call the function    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
        
            print("A key has been pressed")

    
    
      # keeps the window open so you can see the result.