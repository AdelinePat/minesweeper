from view.victory_menu import VictoryMenu
from view.settings_menu import SettingsMenu
from view.roll_of_fame import RollOfFame
from model.data_access import Data
from model.game_grid import GameGrid
from model.game_info import GameInfo

class MenuController():
    def __init__(self):
        self.game_controller = GameInfo()
        self.data_access = Data(self.game_controller)
        self.victory_screen = VictoryMenu('Bravo vous avez gagné', self.game_controller)
        self.settings_screen = SettingsMenu(self.game_controller)
        self.roll_of_fame_screen = RollOfFame(self)
        self.in_game_screen = GameGrid('grille de jeu', self.game_controller)

        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_victory = False
        self.is_screen_in_game = False
        self.button_return = False

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

    def manage_victory_screen(self, winner_better_than):
        if not winner_better_than:
            self.victory_screen.draw_window_winner_not_top_3(self)
        else:
            self.victory_screen.draw_winner_top_3(self)
            print(self.game_controller.player_name)

    def screen_access(self):
        """Controls screen transitions based on the flags."""
        if self.is_screen_in_game:
            self.is_screen_main = False
            self.game_controller.set_grid()
            self.in_game_screen.draw_in_game_screen()
            self.manage_game_screen()

        elif self.is_screen_settings:
            self.is_screen_main = False
            self.settings_screen.draw_window_settings(self)
            if self.settings_screen.button_return:
                self.go_to_main_menu()

        elif self.is_screen_victory == True:
            self.is_screen_main = False
            winner_better_than = self.check_timer_top_3_players()
            self.manage_victory_screen(winner_better_than)
            if self.victory_screen.button_return == True:
                if self.game_controller.player_name != None:
                    self.data_access.process_winner()
                self.go_to_main_menu()

        elif self.is_screen_record:
            self.is_screen_main = False
            self.roll_of_fame_screen.draw_wall_of_fame_menu()

            if self.roll_of_fame_screen.button_return:
                self.go_to_main_menu()

    def go_to_victory_menu(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = False
        self.is_screen_victory = True
        self.is_screen_in_game = False

    def go_to_main_menu(self):
        """Switch to the main menu."""
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_victory = False
        self.is_screen_in_game = False
        print("Going back to the main menu.")


    def check_timer_top_3_players(self):
        top3_dict = self.data_access.load_top3_dict()
        if len(top3_dict) < 3:
            is_top_3 = True
        else:
            for key in top3_dict:
                if self.game_controller.game_time < top3_dict[key]:
                    is_top_3 = True
                else:
                    is_top_3 = False
        
        return is_top_3