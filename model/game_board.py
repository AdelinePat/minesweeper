import random
import pygame
from view.__settings__ import CERULEAN, NOT_SO_GHOST_WHITE, GHOST_WHITE, TEXT_FONT
from view.in_game_menu import InGameMenu
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
        self.is_victory = False
        
        self.stopwatch_start_time=None

        self.previous_mouse_state=pygame.mouse.get_pressed()

        self.click = 0
        self.start_game = False
        self.bomb_positions = []
        self.revealed_square = []
        self.flag_count = 0
        self.interrogation_count = 0
        self.game_over = False

        
        self.window_rect =  pygame.Rect(
                            0,0,
                            self.win_width, self.win_height)
        
        self.window_rect.center = self.screen_center

        self.grid_surface_tuple = (self.height//3*2, self.height//3*2)

        self.grid_rect = pygame.Rect(self.window_rect.topleft[0],
                                     self.window_rect.topleft[1],
                                     self.grid_surface_tuple[0],
                                    self.grid_surface_tuple[1])
    
    def start_stopwatch(self):
        if self.click>=1:
            if self.stopwatch_start_time==None:
                self.stopwatch_start_time=pygame.time.get_ticks()
            self.exact_current_timer=int((pygame.time.get_ticks()-self.stopwatch_start_time)//10)
            self.current_timer=int((pygame.time.get_ticks()-self.stopwatch_start_time)/1000)
            self.time_in_seconds=(self.current_timer%60)
            self.time_in_minutes=(self.current_timer//60)
            #↓ if it looks stupid, but it works, then it ain't stupid, space erases the previous title and puts in the timer
            self.time_to_show=str(f"                                                                   {self.time_in_minutes:02}:{self.time_in_seconds:02}                                                               ")
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

        if not self.game_over:
            self.set_title(f'{self.start_stopwatch() if self.start_stopwatch() else "Minesweeper MOUHAHAHAHAHA"}', self.height//25)
        else:
            self.set_title(f'Vous avez perdu', self.height//25)

        

        self.display_game_info('Mines :', f'{len(self.bomb_positions)}',
                               self.height // 4*0.75
                               )
        
        if self.flag_count <= 1:
            self.display_game_info('Drapeau posé :', f'{self.flag_count}',
                                self.height // 4*1.25
                                )
        else:
            self.display_game_info('Drapeaux posés :', f'{self.flag_count}',
                                self.height // 4*1.25
                                )

        if self.interrogation_count <= 1:
            self.display_game_info('? posé :', f'{self.interrogation_count}',
                                self.height // 4*1.75
                                )
        else:
            self.display_game_info('? posés :', f'{self.interrogation_count}',
                                self.height // 4*1.75
                                )
        
        self.reset_game = self.small_button('Réinitialiser', (self.width // 4*3, self.height // 4 * 2.5))
        if self.reset_game:
            self.reset_game_info()
            self.create_board()
            
        self.button_return = self.small_button('Retour', (self.width // 4*3, self.height // 4 * 3))

        self.go_through_board()

    def get_grid_node_size(self):
        size = (
            (self.grid_rect.height - self.border_thickness ) // self.rows)- self.padding
        return size
    
    def get_grid_top_left(self):
        my_top_left = (self.grid_rect.topleft[0] + self.border_thickness+ self.padding//2,
                              self.grid_rect.topleft[1] + self.border_thickness+ self.padding//2 )
        return my_top_left

    def reset_game_info(self):
        self.bomb_positions = []
        self.stopwatch_start_time=None
        self.click = 0
        self.start_game = False
        self.bomb_positions = []
        self.revealed_square = []
        self.is_victory = False
        self.game_over = False
        # self.flag_list = 0
        # self.interrogation_list = 0


    def create_board(self):
        self.rows = self.game_info.grid_rows
        self.columns = self.game_info.grid_columns

        
        self.grid_node_width = self.get_grid_node_size()
        
        self.grid_node_height = self.get_grid_node_size()
        self.game_info.square_surface = (self.grid_node_width, self.grid_node_height)
        self.game_info.set_mine_resized()
        self.game_info.set_flag_resized()

        self.grid_top_left = self.get_grid_top_left()

        x = self.grid_top_left[0]
        y = self.grid_top_left[1]
        board = []
        
        for row in range(self.rows): # rows
            row_list = []

            for column in range(self.columns):
    
                square_hitbox = self.createSquare(NOT_SO_GHOST_WHITE, x, y)
                content = Square(square_hitbox, None, False)
               
                row_list.append(content)
                x += (self.grid_node_width + self.padding)

            board.append(row_list)
            x = self.grid_top_left[0]
            y += (self.grid_node_height + self.padding)
        
        self.draw_grid_border()
        return board
    
    def redraw_board(self):
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
                
                elif self.board[row][column].revealed==False:

                    self.createSquare(NOT_SO_GHOST_WHITE,
                                    self.board[row][column].hitbox.topleft[0], 
                                    self.board[row][column].hitbox.topleft[1])
                    
                    if self.board[row][column].is_element and self.board[row][column].element in ("F", "?"):
                        self.draw_revealed_square_with_element(row, column)

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

                    if self.board[actual_row][actual_col].value == 0 and not self.board[actual_row][actual_col].revealed:
                        self.board[actual_row][actual_col].revealed = True
                        self.reveal_square(actual_row, actual_col)

                    elif self.board[actual_row][actual_col].value in (1,2,3,4,5,6,7,8) and not self.board[actual_row][actual_col].revealed:
                        self.board[actual_row][actual_col].revealed = True
                        self.draw_revealed_square_with_value(actual_row, actual_col)

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
        
    def draw_revealed_square_with_element(self, actual_row, actual_col):
        self.createSquare(NOT_SO_GHOST_WHITE,
                        self.board[actual_row][actual_col].hitbox.topleft[0],
                        self.board[actual_row][actual_col].hitbox.topleft[1])
        if self.board[actual_row][actual_col].element == "?":
            self.draw_text(str(self.board[actual_row][actual_col].element),
                TEXT_FONT,
                self.board[actual_row][actual_col].hitbox.height - 5,
                self.board[actual_row][actual_col].hitbox.center
                )
        elif self.board[actual_row][actual_col].element == "F":
            self.screen.blit(self.game_info.flag_img, self.board[actual_row][actual_col].hitbox)

        
    def get_random_position_tuple(self):
        x = random.randrange(self.rows)
        y = random.randrange(self.columns)
        position = (x,y)
        return position

    def get_bomb_positions_list(self, row, column):

        bomb_positions_list = []
        if self.game_info.difficulty == 0:
            min_range = 8
            max_range = 12
        elif self.game_info.difficulty == 1:
            min_range = 17
            max_range = 22
        else:
            min_range = 40
            max_range = 50

        
        bomb_number = random.randrange(min_range, max_range)

        for bomb in range(0, bomb_number):
            position = self.get_random_position_tuple()
            while position in bomb_positions_list or position == (row, column):
                position = self.get_random_position_tuple()
            bomb_positions_list.append(position)
        # print(bomb_positions_list)
        return bomb_positions_list
    
    def draw_element(self,actual_row, actual_col):
        self.createSquare(
            NOT_SO_GHOST_WHITE,
            self.board[actual_row][actual_col].hitbox.topleft[0],
            self.board[actual_row][actual_col].hitbox.topleft[1]
        )
        if self.board[actual_row][actual_col].element == "?":
            self.draw_text(str(self.board[actual_row][actual_col].element),
                TEXT_FONT,
                self.board[actual_row][actual_col].hitbox.height - 5,
                self.board[actual_row][actual_col].hitbox.center
                )
        elif self.board[actual_row][actual_col].element == "F":
            self.screen.blit(self.game_info.flag_img, self.board[actual_row][actual_col].hitbox)


    
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

    def check_mouse_release(self, button: int=0)->bool:
        '''checks if mouse button (0 for left, 1 for middle, 2 for right) was released 
        useful for avoiding mouse holding shenanigans'''
        current_mouse_state=pygame.mouse.get_pressed()
        if self.previous_mouse_state[button] and not current_mouse_state[button]:
            self.previous_mouse_state=current_mouse_state
            return True
        
        self.previous_mouse_state=current_mouse_state
        return False
    
    
    def check_user_click(self, row, column, mouse_position, hitbox):
        if hitbox.hitbox.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            self.click += 1
            self.start_game = True
            
            if self.click == 1:
# do some stuff

                self.bomb_positions = self.get_bomb_positions_list(row, column)
                self.set_board_values()

            if (row, column) in self.bomb_positions:
                self.game_over = True
                print("AIE, raté ! Il y avait une bombe , tu as perdu")

            else:
                self.reveal_square(row, column)
        
        elif hitbox.hitbox.collidepoint(mouse_position) and hitbox.element==None and self.check_mouse_release(2):
            self.start_game = True
            hitbox.element= "F"
            print(f"element changed to {hitbox.element}")
            self.board[row][column].is_element = True
            self.draw_element(row, column)

        elif hitbox.hitbox.collidepoint(mouse_position) and hitbox.element=="F" and self.check_mouse_release(2):
            hitbox.element="?"
            print(f"element changed to {hitbox.element}")
            self.draw_element(row, column)

        elif hitbox.hitbox.collidepoint(mouse_position) and hitbox.element=="?" and self.check_mouse_release(2):
            hitbox.element=None
            print(f"element changed to {hitbox.element}")
            # self.draw_element(row, column)


           

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
        self.check_for_victory()
        if not self.is_victory and not self.game_over:
            self.flag_count = 0
            self.interrogation_count = 0
            for row in range(self.rows):
                for column in range(self.columns):
                    hitbox = self.board[row][column]
                    self.check_user_click(row, column, mouse_position, hitbox)
                    
                    if self.board[row][column].revealed and self.board[row][column].hitbox not in self.revealed_square:
                        position = (row, column)
                        self.revealed_square.append(self.board[row][column].hitbox)
                    elif self.board[row][column].element == "F":
                        self.flag_count += 1
                    elif self.board[row][column].element == "?":
                        self.interrogation_count += 1
        elif self.game_over:
            self.reveal_all_board()
        else:
            print("fin de partie")

    def check_for_victory(self):
        square_to_reveal = self.rows * self.columns - len(self.bomb_positions)
        print(len(self.revealed_square))
        if len(self.revealed_square) == square_to_reveal:
            self.is_victory = True
            print(f"timer exact en fin de partie {self.exact_current_timer}")
            print(f"timer en fin de partie {self.current_timer}")
            self.game_info.game_time = self.exact_current_timer
        else:
            self.is_victory = False

    def reveal_all_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column].value in (1,2,3,4,5,6,7,8):
                    self.draw_revealed_square_with_value(row, column)
                elif self.board[row][column].value == 0:
                    self.createSquare(GHOST_WHITE,
                        self.board[row][column].hitbox.topleft[0],
                        self.board[row][column].hitbox.topleft[1])
                else:
                    self.createSquare(NOT_SO_GHOST_WHITE,
                        self.board[row][column].hitbox.topleft[0],
                        self.board[row][column].hitbox.topleft[1])
                    self.screen.blit(self.game_info.mine_img, self.board[row][column].hitbox)
                    
        self.draw_grid_border()



