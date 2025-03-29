from view.winner_menu import Winner
from view.settings_menu import SettingsMenu
from model.game_board import GameBoard
import json
from view.__settings__ import TOP3_PATH
from controller.game_controller import GameController
import pygame
import json
import uuid  
from datetime import datetime 


class MenuController():
    def __init__(self):
        self.game_controller = GameController()
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False
        self.button_return = False
        self.winner = ""
        self.winner_screen = Winner('Bravo vous avez gagné', self.game_controller)
        self.settings_screen = SettingsMenu(self.game_controller)
                # self.in_game_screen = GameBoard('grille de jeu', self.game_controller.game_info)
        self.in_game_screen = GameBoard('grille de jeu', self.game_controller.game_info)
        
        self.resolution = self.settings_screen.resolutions[0]

        ## Displatch those 4 infos into game_info or elsewhere
        self.player_name = " Adelina"
        self.player_time = None
        self.top_players = []
        self.player_id = str(uuid.uuid4())

    def screen_access(self):
        """Controls screen transitions based on the flags."""

            # match self.game_controller.game_info.difficulty:
            #     case 0:
            #         self.game_controller.game_info.grid_rows = 8
            #         self.game_controller.game_info.grid_columns = 8                   
            #     case 1:
            #         self.game_controller.game_info.grid_rows = 15
            #         self.game_controller.game_info.grid_columns = 15

        if self.is_screen_in_game:
            self.is_screen_main = False
            match self.game_controller.game_info.difficulty:
                case 0:
                    self.game_controller.game_info.grid_rows = 8
                    self.game_controller.game_info.grid_columns = 8                   
                case 1:
                    self.game_controller.game_info.grid_rows = 12
                    self.game_controller.game_info.grid_columns = 12
                case 2:
                    self.game_controller.game_info.grid_rows = 15
                    self.game_controller.game_info.grid_columns = 15

            self.in_game_screen.draw_in_game_screen()
            # pygame.display.update()
            
            # self.controller.is_screen_main = False
            # self.in_settings_screen = True

            if self.in_game_screen.button_return:
                self.in_game_screen.reset_game_info()
                self.is_screen_in_game = False
                self.is_screen_main = True
            elif self.in_game_screen.is_victory:
                self.in_game_screen.reset_game_info()
                self.is_screen_in_game = False
                self.is_screen_win = True
                

        elif self.is_screen_settings:
            self.is_screen_main = False
            self.settings_screen.draw_window_settings(self)
            # pygame.display.update()
            
            # self.controller.is_screen_main = False
            # self.in_settings_screen = True

            if self.settings_screen.button_return:
                self.is_screen_settings = False
                self.is_screen_main = True

        elif self.is_screen_win == True:
            self.is_screen_main = False
            winner_better_than = self.check_timer_top_3_players()

            if winner_better_than == None:
                self.winner_screen.draw_window_winner_not_top_3(self)
            else:
                # create condition for which screen to display
                self.winner_screen.draw_winner_top_3(self)
                print(self.game_controller.game_info.player_name)
            # self.winner_screen.draw_window_winner_not_top_3(self)
            if self.winner_screen.button_return == True:
                self.is_screen_win = False
                self.is_screen_main = True
    
    def set_settings(self, choice):
        '''TODO: display settings screen + back-end for settings choice'''

        if choice == True:
            print('YEAH LET\'S PLAY')
            print("This is the game screen.")
        elif self.is_screen_settings:
            self.is_screen_main = False
            
            self.settings_screen.draw_window_settings(self)
            if self.settings_screen.button_return :
                self.is_screen_settings = False
                self.is_screen_main = True
            # self.settings_screen.update()
            print("This is the settings menu.")
        elif self.is_screen_record:
            print("This is the top 3 players screen.")
        elif self.is_screen_main:
            print("This is the main menu.")

    def start_game(self):
        """Placeholder for starting the game."""
        if self.is_screen_in_game:
            print("This is the game screen.")
        pass

    def set_settings(self):
        """Handle settings screen access."""
        if self.is_screen_settings:
            print("This is the settings menu.")
        pass

    

    def go_to_main_menu(self):
        """Switch to the main menu."""
        self.is_screen_main = True
        self.is_screen_settings = False
        self.is_screen_in_game = False
        print("Going back to the main menu.")

    def go_to_settings(self):
        """Switch to the settings screen."""
        self.is_screen_main = False
        self.is_screen_settings = True
        self.screen_access()
        print("Switching to the settings menu.")

    def check_timer_top_3_players(self): # check iof save_new_top 3 and all bellow doesn't already do the job
        with open(TOP3_PATH, 'r', encoding="UTF-8") as file:
            top3_dict = json.load(file)

        for index, key in enumerate(top3_dict):
            if self.game_controller.game_info.game_time < top3_dict[key]:
                print(key)
                return key
            else:
                return None
            
    def save_new_top_3(self):
        with open(TOP3_PATH, 'r', encoding="UTF-8") as file:
            top3_dict = json.load(file)

        for index, key in enumerate(top3_dict):
            if self.game_controller.game_info.game_time < top3_dict[key]:
                print(key)
                return key
            else:
                return None

    def load_top_players(self, file_path='view/wall_of_fame.json'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, list):  
                    self.top_players = data
                else:  
                    self.top_players = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.top_players = []

    def save_top_players(self, file_path='view/wall_of_fame.json'):
        """ Saves the leaderboard to a file """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.top_players, file, indent=4, ensure_ascii=False)

    def update_top_players(self):
        """ Adds the player's result and keeps only the top 3 fastest times """
        
        new_entry = {
            "id": self.player_id,
            "name": self.player_name,
            "time": self.player_time, 
            "timestamp": datetime.now().isoformat()  
        }

        # If there are fewer than 3 players in the top list, add the new player
        if len(self.top_players) < 3:
            self.top_players.append(new_entry)
        else:
            # If the player's time is better than the slowest in the top 3, replace it
            self.top_players.append(new_entry)
            self.top_players.sort(key=lambda x: x["time"])  
            self.top_players = self.top_players[:3]  

    def process_winner(self, file_path='view/wall_of_fame.json'):
        """ Processes the winner: loads, updates, and saves the leaderboard """
        self.load_top_players(file_path)
        self.update_top_players()
        self.save_top_players(file_path)
