from view.winner_menu import Winner
from view.settings_menu import SettingsMenu
from view.wall_of_fame_menu import RollOfFame
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
        self.roll_of_fame_screen = RollOfFame(self)
                # self.in_game_screen = GameBoard('grille de jeu', self.game_controller.game_info)
        self.in_game_screen = GameBoard('grille de jeu', self.game_controller.game_info)
        
        self.resolution = self.settings_screen.resolutions[0]

        ## Displatch those 4 infos into game_info or elsewhere
        self.player_name = " Adelina"
        self.player_time = None
        self.top_players = []
        self.player_id = str(uuid.uuid4())

    def set_grid(self):
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


    def screen_access(self):
        """Controls screen transitions based on the flags."""
        if self.is_screen_in_game:
            self.is_screen_main = False
            self.set_grid()
            self.in_game_screen.draw_in_game_screen()
            # pygame.display.update()
            
            # self.controller.is_screen_main = False
            # self.in_settings_screen = True

            if self.in_game_screen.button_return:
                self.in_game_screen.reset_game_info()
                self.go_to_main_menu()
                # self.is_screen_in_game = False
                # self.is_screen_main = True
            elif self.in_game_screen.is_victory:
                self.in_game_screen.reset_game_info()
                # self.is_screen_in_game = False
                # self.is_screen_win = True
                self.go_to_victory_menu()
            
                

        elif self.is_screen_settings:
            self.is_screen_main = False
            self.settings_screen.draw_window_settings(self)
            # pygame.display.update()
            
            # self.controller.is_screen_main = False
            # self.in_settings_screen = True

            if self.settings_screen.button_return:
                # self.is_screen_settings = False
                # self.is_screen_main = True
                self.go_to_main_menu()

        elif self.is_screen_win == True:
            self.is_screen_main = False
            winner_better_than = self.check_timer_top_3_players()
            if winner_better_than == None:
                self.winner_screen.draw_window_winner_not_top_3(self)
            else:
                self.winner_screen.draw_winner_top_3(self)
                print(self.game_controller.game_info.player_name)
            if self.winner_screen.button_return == True:
                if self.game_controller.game_info.player_name != None:
                    self.process_winner()
                
                self.go_to_main_menu()

        elif self.is_screen_record:
            self.is_screen_main = False
            self.roll_of_fame_screen.draw_wall_of_fame_menu()

            if self.roll_of_fame_screen.button_return:
                self.go_to_main_menu()

                # self.is_screen_win = False
                # self.is_screen_main = True
    
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
    
    def go_to_victory_menu(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = False
        self.is_screen_win = True
        self.is_screen_in_game = False

    def go_to_top_3(self):
        self.is_screen_settings = False
        self.is_screen_record = True
        self.is_screen_main = False
        self.is_screen_win = False
        self.is_screen_in_game = False

    def go_to_game(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = False
        self.is_screen_win = False
        self.is_screen_in_game = True

    def go_to_main_menu(self):
        """Switch to the main menu."""
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False
        print("Going back to the main menu.")

    # def go_to_settings(self):
    #     """Switch to the settings screen."""
    #     self.is_screen_settings = True
    #     self.is_screen_record = False
    #     self.is_screen_main = False
    #     self.is_screen_win = False
    #     self.is_screen_in_game = False
    #     print("Switching to the settings menu.")

    # def load_top3_dict(self):
    #     with open(TOP3_PATH, 'r', encoding="UTF-8") as file:
    #         top3_dict = json.load(file)
    #     return top3_dict

    def check_timer_top_3_players(self): # check iof save_new_top 3 and all bellow doesn't already do the job
        top3_dict = self.load_top3_dict()
        for index, key in enumerate(top3_dict):
            if self.game_controller.game_info.game_time < top3_dict[key]:
                # print(key)
                return key
            else:
                return None

    # def load_top_players_names_only(self):
    #     try:
    #         top3_dict = self.load_top3_dict()
    #         if isinstance(top3_dict, dict):  # list of dictionnary
    #             for key in top3_dict:
    #                 player_name = key.split()[0]
    #                 self.top_players.append(key)
    #             # self.top_players = data
    #         else:  
    #             self.top_players = []
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         self.top_players = []

    # def save_top_players(self, dict_to_dump):
    #     """ Saves the leaderboard to a file """
    #     with open(TOP3_PATH, 'w', encoding='utf-8') as file:
    #         json.dump(dict_to_dump, file, indent=4, ensure_ascii=False)

    # def pop_last_player_from_top_3(self, top3_dict):
    #     timer_list = []
    #     for key in top3_dict:
    #         timer_list.append(top3_dict[key])

    #     for key in top3_dict:
    #         if top3_dict[key] == max(timer_list):
    #             key_to_pop = key
    #     top3_dict.pop(key_to_pop)

    #     return top3_dict

    # def sort_top3_before_saving(self, top3_dict):
    #     new_dict = {}
    #     for key, value in sorted(top3_dict.items(), key=lambda item : item[1]):
    #         new_dict[key] = value
    #     return new_dict

    # def update_top_players(self):
    #     """ Adds the player's result and keeps only the top 3 fastest times """
    #     top3_dict = self.load_top3_dict()
    #     new_player_name = self.game_controller.game_info.player_name + f' {datetime.now().isoformat()}'
    #     top3_dict[new_player_name] = self.game_controller.game_info.game_time
    #     top3_dict = self.pop_last_player_from_top_3(top3_dict)
    #     top3_dict_sorted = self.sort_top3_before_saving(top3_dict)
    #     self.save_top_players(top3_dict_sorted)

    #     # new_entry = {
    #     #     "id": self.player_id,
    #     #     "name": self.player_name,
    #     #     "time": self.player_time, 
    #     #     "timestamp": datetime.now().isoformat()  
    #     # }

    #     # # If there are fewer than 3 players in the top list, add the new player
    #     # if len(self.top_players) < 3:
    #     #     self.top_players.append(new_entry)
    #     # else:
    #     #     # If the player's time is better than the slowest in the top 3, replace it
    #     #     self.top_players.append(new_entry)
    #     #     self.top_players.sort(key=lambda x: x["time"])  
    #     #     self.top_players = self.top_players[:3]  


    # def process_winner(self):
    #     """ Processes the winner: loads, updates, and saves the leaderboard """
    #     self.load_top_players_names_only()
    #     self.update_top_players()
