class MenuController():
    def __init__(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False

        self.player_name = " Yulii"
        self.player_score = 0
        self.top_players = []

    def screen_access(self):
        if self.is_screen_in_game == True:
            print("ceci est un super jeu")
        elif self.is_screen_settings == True:
            print("Ceci est le menu des paramètres")
        elif self.is_screen_record == True:
            print("Un super top 3!!")

  
    def start_game(self): # return to the game screen
        '''TODO: start the game screen'''
        if self.is_screen_in_game == True:
            print("ceci est un super jeu")
        
        pass
    
    def set_settings(self, choice):
        '''TODO: display settings screen + back-end for settings choice'''
        if choice == True:
            print('YEAH LET\'S PLAY')
        pass

    def get_top_players(self, choice):
        '''TODO: display top 3 players + back-end for getting right data'''
        if choice == True:
            print("un super top trois")
        pass





    def return_menu_principal(self):
        self.is_screen_main = True  
        self.is_screen_settings = False  
        self.is_screen_record = False  
        self.is_screen_win = False  
        self.is_screen_in_game = False  
        print("Retour au menu principal") 



    def check_top_players(self):
        '''Vérifier si le joueur actuel est dans le top 3'''
        if self.player_name and self.player_score:
            self.top_players.append({"name": self.player_name, "score": self.player_score})
            self.top_players = sorted(self.top_players, key=lambda x: x["score"], reverse=True)
            self.top_players = self.top_players[:3]
            if any(player["name"] == self.player_name for player in self.top_players):
                print(f"{self.player_name} est dans le top 3 !")

