import json
from datetime import datetime

from controller.menu_controller import MenuController


menu = MenuController()


menu.player_name = "Adelina"
menu.player_time = 113 


menu.load_top_players('view/wall_of_fame.json')


menu.update_top_players()

menu.save_top_players('view/wall_of_fame.json')

top_players = menu.top_players
is_in_top_3 = any(player["name"] == "Alisia" for player in top_players)

if is_in_top_3:
    print("Alisia is in the top 3!")
else:
    print("Alisia did not make it to the top 3.")


print("Current Top 3 Players:")
for player in top_players:
    print(f"Name: {player['name']}, Time: {player['time']} seconds")