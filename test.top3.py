import json
from controller.menu_controller import MenuController  


menu = MenuController()


menu.player_name = "Alisia"
menu.player_score = 50


menu.load_top_players('wall_of_fame.json')
print("Après le chargement :", menu.top_players)

menu.update_top_players()
print("Après la mise à jour :", menu.top_players)

menu.save_top_players('wall_of_fame.json')
print("Les meilleurs joueurs ont été sauvegardés.")
