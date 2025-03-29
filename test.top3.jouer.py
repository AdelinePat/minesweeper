import json
from datetime import datetime

from controller.menu_controller import MenuController


menu = MenuController()


menu.player_name = "Maria"
menu.player_time = 130


menu.load_top_players('view/wall_of_fame.json')


menu.update_top_players()

menu.save_top_players('view/wall_of_fame.json')

top_players = menu.top_players


print("Current Top 3 Players:")
for player in top_players:
    print(f"Name: {player['name']}, Time: {player['time']} seconds")