from view.victory_menu import VictoryMenu
from view.settings_menu import SettingsMenu
from view.roll_of_fame import RollOfFame
from model.data_access import Data
from model.game_grid import GameGrid
from controller.game_controller import GameController

class MenuController():
    def __init__(self):
        self.game_controller = GameController()
        self.data_access = Data(self)
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False
        self.button_return = False
        self.winner = ""
        self.winner_screen = VictoryMenu('Bravo vous avez gagné', self.game_controller)
        self.settings_screen = SettingsMenu(self.game_controller)
        self.roll_of_fame_screen = RollOfFame(self)
        self.in_game_screen = GameGrid('grille de jeu', self.game_controller.game_info)
        
        self.resolution = self.settings_screen.resolutions[0]

        ## Displatch those 4 infos into game_info or elsewhere
        # self.player_name = " Adelina"
        # self.player_time = None
        # self.top_players = []
        # self.player_id = str(uuid.uuid4())

    def manage_game_screen(self):
        if self.in_game_screen.button_return:
                self.in_game_screen.reset_game_info()
                self.go_to_main_menu()
        elif self.in_game_screen.is_victory:
                self.in_game_screen.reset_game_info()
                self.go_to_victory_menu()

    def manage_winner_screen(self, winner_better_than):
        if not winner_better_than:
            self.winner_screen.draw_window_winner_not_top_3(self)
        else:
            self.winner_screen.draw_winner_top_3(self)
            print(self.game_controller.game_info.player_name)

    def screen_access(self):
        """Controls screen transitions based on the flags."""
        if self.is_screen_in_game:
            self.is_screen_main = False
            self.game_controller.game_info.set_grid()
            self.in_game_screen.draw_in_game_screen()
            self.manage_game_screen()

        elif self.is_screen_settings:
            self.is_screen_main = False
            self.settings_screen.draw_window_settings(self)
            if self.settings_screen.button_return:
                self.go_to_main_menu()

        elif self.is_screen_win == True:
            self.is_screen_main = False
            winner_better_than = self.check_timer_top_3_players()
            self.manage_winner_screen(winner_better_than)
            if self.winner_screen.button_return == True:
                if self.game_controller.game_info.player_name != None:
                    self.data_access.process_winner()
                self.go_to_main_menu()

        elif self.is_screen_record:
            self.is_screen_main = False
            self.roll_of_fame_screen.draw_wall_of_fame_menu()

            if self.roll_of_fame_screen.button_return:
                self.go_to_main_menu()

    def start_game(self):
        """Placeholder for starting the game."""
        if self.is_screen_in_game:
            print("This is the game screen.")
        pass

    def go_to_victory_menu(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = False
        self.is_screen_win = True
        self.is_screen_in_game = False

    def go_to_main_menu(self):
        """Switch to the main menu."""
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False
        print("Going back to the main menu.")


    def check_timer_top_3_players(self):
        top3_dict = self.data_access.load_top3_dict()
        if len(top3_dict) < 3:
            is_top_3 = True
        else:
            for key in top3_dict:
                if self.game_controller.game_info.game_time < top3_dict[key]:
                    is_top_3 = True
                else:
                    is_top_3 = False
        
        return is_top_3

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
