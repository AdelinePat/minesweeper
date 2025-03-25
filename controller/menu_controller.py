class MenuController():
    def __init__(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False

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
