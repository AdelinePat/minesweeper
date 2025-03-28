from view.in_game_menu import InGameMenu
from view.__settings__ import CERULEAN, NOT_SO_GHOST_WHITE, GHOST_WHITE, TEXT_FONT, TITLE_FONT, CYAN, AGRESSIVE_PINK
import random
import pygame
import datetime
import time
from model.square import Square

class GameBoard(InGameMenu):
    def __init__(self, caption, game_info):
        super().__init__(caption)
        self.game_info = game_info
        self.win_width = self.width // 3*2
        self.win_height = self.height // 3*2
        self.padding = 2
        self.border_thickness = 5
        self.border_radius = 15
        self.button_height = self.height // 12
        

        self.stopwatch_start_time=pygame.time.get_ticks()

        self.click = 0
        self.start_game = False
        # self.rows = rows
        # self.columns = columns
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
        
        # self.grid_rect_draw = pygame.draw.rect(self.screen,
        #                                        CERULEAN,
        #                                        self.grid_rect,
        #                                        border_radius=self.border_radius)
        
        
        
        # self.board = self.create_board()
    
    def start_stopwatch(self):

        if self.click>=1:
            self.current_timer=int((pygame.time.get_ticks()-self.stopwatch_start_time)/1000)
            self.time_in_seconds=(self.current_timer%60)
            self.time_in_minutes=(self.current_timer//60)
            #↓ if it looks stupid, but it works, then it ain't stupid, space erases the previous title and puts in the timer
            self.time_to_show=str(f"                              {self.time_in_minutes:02}:{self.time_in_seconds:02}                                ")
            #↑ if it looks stupid, but it works, then it ain't stupid, space erases the previous title and puts in the timer
            return self.time_to_show

    def draw_in_game_screen(self):
        self.reset_background_screen()
        self.grid_rect_draw = pygame.draw.rect(self.screen,
                                               CERULEAN,
                                               self.grid_rect,
                                               border_radius=self.border_radius)

        if self.click == 0 and not self.start_game:
            self.board = self.create_board()
        else:
            self.redraw_board() 

        self.set_title(f'{self.start_stopwatch() if self.start_stopwatch() else "Cliquez pour commancer"}')

        self.display_game_info('Mines :', f'{len(self.bomb_positions)}',
                               self.height // 4
                               )
        
        #print(len(self.bomb_positions))
        
        self.display_game_info('Drapeau(x) posé(s) :', f'0',
                               self.height // 4*1.5
                               )
        
        self.display_game_info('? posé(s) :', f'0',
                               self.height // 4*2
                               )

        self.reset_game = self.small_button('Réinitialiser', (self.width // 4*3, self.height // 4 * 2.5))
        if self.reset_game:
            self.create_board()
            
        self.small_button('Quitter', (self.width // 4*3, self.height // 4 * 3))
        
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
        
        self.rows = self.game_info.grid_rows
        self.columns = self.game_info.grid_columns

        self.grid_node_width = self.get_grid_node_size()
        
        self.grid_node_height = self.get_grid_node_size()

        self.grid_top_left = self.get_grid_top_left()

        x = self.grid_top_left[0]
        y = self.grid_top_left[1]
        board = []
        
        for row in range(self.rows): # rows
            row_list = []

            for column in range(self.columns):
    
                square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                # content = [square_hitbox, None]
                content = Square(square_hitbox, None, False)
               
                row_list.append(content)
                x += (self.grid_node_width + self.padding)

            board.append(row_list)
            x = self.grid_top_left[0]
            y += (self.grid_node_height + self.padding)
        
        self.draw_grid_border()
        return board
    
    def redraw_board(self):
        # self.grid_rect_draw = pygame.draw.rect(self.screen,
        #                                        CERULEAN,
        #                                        self.grid_rect,
        #                                        border_radius=self.border_radius)
        x = self.grid_top_left[0]
        y = self.grid_top_left[1]

        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column].revealed == True:
                    if self.board[row][column].value != 0:
                        self.draw_revealed_square_with_value(row, column)
                    else:
                        self.createSquare(GHOST_WHITE,
                                          self.board[row][column].hitbox.topleft[0], 
                                          self.board[row][column].hitbox.topleft[1]) 
                else:
                    self.createSquare(NOT_SO_GHOST_WHITE,
                                    self.board[row][column].hitbox.topleft[0], 
                                    self.board[row][column].hitbox.topleft[1])
                    # print(f'redraw board when not so ghost white {row}, {column}')
            x = self.grid_top_left[0]
            y += (self.grid_node_height + self.padding)
        
        self.draw_grid_border()

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


        if self.board[row][column].value in (1,2,3,4,5,6,7,8):
                self.board[row][column].revealed = True
                self.draw_revealed_square_with_value(row, column)

        elif self.board[row][column].value == 0:
            for actual_row in range(min_row_range, max_row_range):
                for actual_col in range(min_column_range, max_column_range):
                    print(actual_row, actual_col)
                    
                    if self.board[actual_row][actual_col].value == 0 and (actual_row,actual_col) not in self.revealed_square:
                        self.board[actual_row][actual_col].revealed = True
                        # self.createSquare(GHOST_WHITE,
                        #     self.board[actual_row][actual_col].hitbox.topleft[0],
                        #     self.board[actual_row][actual_col].hitbox.topleft[1])
                        position = (actual_row, actual_col)
                        ## delete revelead_square list later
                        self.revealed_square.append(position)
                    
                        # print(position)
                        self.reveal_square(actual_row, actual_col)
                        # print(self.board[actual_row][actual_row])
                    elif self.board[actual_row][actual_col].value in (1,2,3,4,5,6,7,8):
                        self.board[actual_row][actual_col].revealed = True
                        self.draw_revealed_square_with_value(actual_row, actual_col)

                    
                        
                        # self.createSquare(GHOST_WHITE,
                        #     self.board[actual_row][actual_col].hitbox.topleft[0],
                        #     self.board[actual_row][actual_col].hitbox.topleft[1])

                        # self.draw_text(str(self.board[actual_row][actual_col].value),
                        #     TEXT_FONT,
                        #     self.board[actual_row][actual_col].hitbox.height - 5,
                        #     self.board[actual_row][actual_col].hitbox.center
                        #     )
                        
            self.draw_grid_border()

    def draw_revealed_square_with_value(self, actual_row, actual_col):
        self.createSquare(GHOST_WHITE,
                        self.board[actual_row][actual_col].hitbox.topleft[0],
                        self.board[actual_row][actual_col].hitbox.topleft[1])

        self.draw_text(str(self.board[actual_row][actual_col].value),
            TEXT_FONT,
            self.board[actual_row][actual_col].hitbox.height - 5,
            self.board[actual_row][actual_col].hitbox.center
            )
        
    def get_random_position_tuple(self):
        x = random.randrange(self.rows)
        y = random.randrange(self.columns)
        position = (x,y)
        return position

    def get_bomb_positions_list(self, row, column):

        bomb_positions_list = []
        if self.game_info.difficulty == 0:
            min_range = 8
            max_range = 15
        elif self.game_info.difficulty == 1:
            min_range = 30
            max_range = 40
        
        bomb_number = random.randrange(min_range, max_range)

        for bomb in range(0, bomb_number):
            position = self.get_random_position_tuple()
            while position in bomb_positions_list or position == (row, column):
                position = self.get_random_position_tuple()
            bomb_positions_list.append(position)
        # print(bomb_positions_list)
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
            self.board[x][y].value = 'bomb'

        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column].value == None:
                    self.board[row][column].value = self.count_surrounding_bombs(row, column)
                # print(f'value at {row},{column} : {self.board[row][column].value}')
    
    def check_user_click(self,row, column, mouse_position, hitbox):
        if hitbox.hitbox.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            self.click += 1
            self.start_game = True
            if self.click == 1:
                self.start_time = datetime.datetime.now()
                self.now = time.time()
# do some stuff

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