from view.__settings__ import TOP3_PATH
from datetime import datetime
import json

class Data():
    def __init__(self, controller):
        self.controller = controller
        self.top_players = []

    def load_top3_dict(self):
        with open(TOP3_PATH, 'r', encoding="UTF-8") as file:
            top3_dict = json.load(file)
        return top3_dict

    def load_top_players_names_only(self):
        try:
            top3_dict = self.load_top3_dict()
            if isinstance(top3_dict, dict):  # list of dictionnary
                for key in top3_dict:
                    player_name = key.split()[0]
                    self.top_players.append(key)
            else:  
                self.top_players = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.top_players = []

    def save_top_players(self, dict_to_dump):
        """ Saves the leaderboard to a file """
        with open(TOP3_PATH, 'w', encoding='utf-8') as file:
            json.dump(dict_to_dump, file, indent=4, ensure_ascii=False)

    def pop_last_player_from_top_3(self, top3_dict):
        timer_list = []
        for key in top3_dict:
            timer_list.append(top3_dict[key])

        for key in top3_dict:
            if top3_dict[key] == max(timer_list):
                key_to_pop = key
        top3_dict.pop(key_to_pop)

        return top3_dict

    def sort_top3_before_saving(self, top3_dict):
        new_dict = {}
        for key, value in sorted(top3_dict.items(), key=lambda item : item[1]):
            new_dict[key] = value
        return new_dict

    def update_top_players(self):
        """ Adds the player's result and keeps only the top 3 fastest times """
        top3_dict = self.load_top3_dict()
        new_player_name = self.controller.player_name + f' {datetime.now().isoformat()}'
        top3_dict[new_player_name] = self.controller.game_time
        if len(top3_dict) == 3:
            top3_dict = self.pop_last_player_from_top_3(top3_dict)
        top3_dict_sorted = self.sort_top3_before_saving(top3_dict)
        self.save_top_players(top3_dict_sorted)

    def process_winner(self):
        """ Processes the winner: loads, updates, and saves the leaderboard """
        self.load_top_players_names_only()
        self.update_top_players()
