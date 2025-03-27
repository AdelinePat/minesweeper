from view.in_game_menu import InGameMenu
from view.__settings__ import CERULEAN, NOT_SO_GHOST_WHITE, GHOST_WHITE, TEXT_FONT, TITLE_FONT, CYAN, AGRESSIVE_PINK
import random
import pygame

class GameBoard(InGameMenu):
    def __init__(self, caption, rows, columns):
        super().__init__(caption)
        self.win_width = self.width // 3*2
        self.win_height = self.height // 3*2
        self.padding = 2
        self.border_thickness = 5
        self.border_radius = 15
        self.button_height = self.height // 12

        self.click = 0
        self.rows = rows
        self.columns = columns
        self.bomb_positions = []
        self.revealed_square = []

        self.window_rect =  pygame.Rect(
                            0,0,
                            self.win_width, self.win_height)
        
        self.window_rect.center = self.screen_center

        self.grid_surface_tuple = (self.height//3*2, self.height//3*2)

        self.grid_rect = pygame.Rect(self.window_rect.topleft[0],
                                     self.window_rect.topleft[1],
                                     self.grid_surface_tuple[0],
                                    self.grid_surface_tuple[1])
        
        self.grid_rect_draw = pygame.draw.rect(self.screen,
                                               CERULEAN,
                                               self.grid_rect,
                                               border_radius=self.border_radius)
        
        self.grid_node_width = self.get_grid_node_size()
        
        self.grid_node_height = self.get_grid_node_size()

        self.grid_top_left = self.get_grid_top_left()
        
        self.board = self.create_board()

    def draw_in_game_screen(self):

        self.set_title('1:01')

        nombre_mine = len(self.bomb_positions)

        self.display_game_info('Mines :', f'{len(self.bomb_positions)}',
                               self.height // 4
                               )
        
        print(len(self.bomb_positions))
        
        self.display_game_info('Drapeau(x) posé(s) :', f'0',
                               self.height // 4*1.5
                               )
        
        self.display_game_info('? posé(s) :', f'0',
                               self.height // 4*2
                               )
        
        # self.small_button()
        
        self.go_through_board()

    def get_grid_node_size(self):
        size = (
            (self.grid_rect.height - self.border_thickness*2 ) // self.rows)- self.padding
        return size
    
    def get_grid_top_left(self):
        my_top_left = (self.grid_rect.topleft[0] + self.border_thickness+ self.padding//2,
                              self.grid_rect.topleft[1] + self.border_thickness+ self.padding//2 )
        return my_top_left

    def create_board(self):
        x = self.grid_top_left[0]
        y = self.grid_top_left[1]
        board = []
        
        for index in range(self.rows): # rows
            row_list = []

            for other_index in range(self.columns):
    
                square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                content = [square_hitbox, None]

                if (index, other_index) in self.bomb_positions:
                    content = [square_hitbox, 'bomb']
               
                row_list.append(content)
                x += (self.grid_node_width + self.padding)

            board.append(row_list)
            x = self.grid_top_left[0]
            y += (self.grid_node_height + self.padding)
        
        self.draw_grid_border()
        return board
    
    def createSquare(self,  color, x, y):
        actual_square = pygame.rect.Rect([x, y, self.grid_node_width, self.grid_node_height])
        pygame.draw.rect(self.screen, color, actual_square)

        return actual_square
    
    def draw_grid_border(self):
        self.grid_border = pygame.draw.rect(self.screen,
                                         CERULEAN,
                                         self.grid_rect,
                                         self.border_thickness,
                                         border_radius=self.border_radius)
        
    def reveal_square(self, row, column):
        min_row_range, max_row_range = self.set_range(row, self.rows)
        min_column_range, max_column_range = self.set_range(column, self.columns)

        
        for actual_row in range(min_row_range, max_row_range):
            for actual_col in range(min_column_range, max_column_range):
                
                if self.board[actual_row][actual_col][1] == 0 and (actual_row,actual_col) not in self.revealed_square:

                    self.createSquare(GHOST_WHITE,
                        self.board[actual_row][actual_col][0].topleft[0],
                        self.board[actual_row][actual_col][0].topleft[1])
                    
                    position = (actual_row, actual_col)
                    self.revealed_square.append(position)
                    print(position)
                    self.reveal_square(actual_row, actual_col)

                elif self.board[actual_row][actual_col][1] in (1,2,3,4,5,6,7,8):
                    self.createSquare(GHOST_WHITE,
                        self.board[actual_row][actual_col][0].topleft[0],
                        self.board[actual_row][actual_col][0].topleft[1])

                    self.draw_text(str(self.board[actual_row][actual_col][1]),
                        TEXT_FONT,
                        self.board[actual_row][actual_col][0].height - 5,
                        self.board[actual_row][actual_col][0].center
                        )
                    
            self.draw_grid_border()

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
    
    def set_range(self, value, max_value):
        if value == 0:
            min_range = 0
            max_range = value + 2
        elif value == (max_value-1):
            min_range = value - 1
            max_range = value + 1
        else:
            min_range = value - 1
            max_range = value + 2
        
        return min_range, max_range
    
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

    def count_surrounding_bombs(self, row, column):
        bomb_count = 0
        min_row_range, max_row_range = self.set_range(row, self.rows)
        min_column_range, max_column_range = self.set_range(column, self.columns)
       
        for actual_row in range(min_row_range, max_row_range):
            for actual_col in range(min_column_range, max_column_range):
                if (actual_row, actual_col) in self.bomb_positions:     
                    bomb_count += 1

        return bomb_count
    
    def go_through_board(self):
        mouse_position = pygame.mouse.get_pos()
        for row in range(self.rows):
            for column in range(self.columns):
                hitbox = self.board[row][column]
                self.check_user_click(row, column, mouse_position, hitbox)