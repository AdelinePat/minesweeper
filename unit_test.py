from view.__settings__ import TOP3_PATH
import json
timer = 5038

with open(TOP3_PATH, 'r', encoding="UTF-8") as file:
    top3_dict = json.load(file)

for index, key in enumerate(top3_dict):
    if top3_dict[key] > timer:
        print(index)
    else:
        print(False)
# if timer in top3_dict.values():
#     print('yata')
            
        # if self.game_controller.game_info.game_time