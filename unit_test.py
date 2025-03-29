from view.__settings__ import TOP3_PATH
import json
from datetime import datetime
import time
timer = 7038
player_name = 'Blblbl'
def load_dict():
    with open(TOP3_PATH, 'r', encoding="UTF-8") as file:
        top3_dict = json.load(file)
    return top3_dict

   

def check_top3():
    top3_dict = load_dict

    for index, key in enumerate(top3_dict):
        if timer < top3_dict[key]:
            print(key)
        else:
            print(False)

top3_dict = load_dict()
# print(top3_dict)
new_key = player_name + f' {datetime.now().isoformat()}'
top3_dict[new_key] = timer
timer_list = []
for key in top3_dict:
    timer_list.append(top3_dict[key])
for key in top3_dict:
    if top3_dict[key] == max(timer_list):
        key_to_pop = key
# print(top3_dict)
top3_dict.pop(key_to_pop)

new_dict = {}
for key, value in sorted(top3_dict.items(), key=lambda item : item[1]):
    print(key, value, end="\n\n")
    new_dict[key] = value

top3_dict.update(new_dict)
print(new_dict)
# print(top3_dict)

            
        # if self.game_controller.game_info.game_time
# top_players = []

# with open(TOP3_PATH, 'r', encoding='utf-8') as file:
#     top3_dict = json.load(file)
#     if isinstance(top3_dict, dict):  # list of dictionnary
#         for key in top3_dict:
#             player_name = key.split()[0]
#             top_players.append(player_name)
#         # self.top_players = data
#     else:  
#         top_players = []


# print(top_players)
