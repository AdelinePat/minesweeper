from view.menu import Menu
import pygame
import sys
from view.__settings__ import NOT_SO_GHOST_WHITE, GHOST_WHITE, CERULEAN


actual_screen = Menu('Grille de jeu')

# pygame.display.get_surface().fill((NOT_SO_GHOST_WHITE))  # background

class Board():
    # alphabet = string.ascii_uppercase
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid_node_width = 20  
        self.grid_node_height = 20


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

        self.board = self.update_board()



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


    def update_board(self):
        y = self.grid_top_left[0]
        x = self.grid_top_left[1]
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
            x = self.grid_top_left[1]
            y += self.grid_node_height
            # print(board)
        return board
            
                # elif other_index 
                # else:
                #     self.createSquare(NOT_SO_GHOST_WHITE, x, y)
            
    def go_through_board(self):
        mouse_position = pygame.mouse.get_pos()
        for row in range(self.rows):
            for column in range(self.columns):
                hitbox = self.board[row][column]
                if hitbox[0].collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
                    hitbox[1] = 2
                    hitbox[0] = self.createSquare('red',
                                                  hitbox[0].topleft[0],
                                                  hitbox[0].topleft[1])
                    print(hitbox[0].topleft)
                    print(hitbox[1])

        
        # hovered = board.collidepoint(mouse_position)

        # if hovered and pygame.mouse.get_pressed()[0]:
        #     pass
        # else:
        #     pass
            


    def visualizeGrid(self):
        y = 0  # we start at the top of the screen
        for row in range(self.columns):
            x = 0 # for every row we start at the left of the screen again
            for item in range(self.rows):
                # if item == None:
                if item % 2 == 0 and row % 2== 0:
                    self.createSquare(x, y, NOT_SO_GHOST_WHITE)
                else:
                    self.createSquare(x, y, GHOST_WHITE)

                x += self.grid_node_width # for ever item/number in that row we move one "step" to the right
            y += self.grid_node_height   # for every new row we move one "step" downwards
        pygame.display.update()

# we use the sizes to draw as well as to do our "steps" in the loops. 
matrix = Board(5,5)
# matrix_grid = matrix.create_board()






# visualizeGrid()  # call the function    
while True:
    actual_screen.update()
    board = matrix.update_board()
    matrix.go_through_board()
    # matrix.visualizeGrid()  # call the function    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
        
            print("A key has been pressed")

    
    
      # keeps the window open so you can see the result.