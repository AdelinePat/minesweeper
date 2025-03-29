from view.menu import Menu
from view.__settings__ import TITLE_FONT, CELESTE

class RollOfFame(Menu):
    def __init__(self, controller):
        super().__init__('Palmarès')
        self.controller = controller
        self.data_acces = self.controller.data_access
        self.game_controller = self.controller.game_controller
        self.divided_by = -1.5

    def draw_wall_of_fame_menu(self):
        self.reset_background_screen()
        self.draw_menu_window()

        my_title = self.draw_text('Palmarès',
                                       TITLE_FONT,
                                       self.height//9,
                                       self.title_center,
                                       color=CELESTE)

    
        player_dict = self.data_acces.load_top3_dict()
        
        if len(player_dict) != 0:
        # Draw buttons with player names and times
            record_list = []
            for player_record in player_dict.items():
                player_name = player_record[0].split()[0]
                record = player_record[1]
                text_to_display = f"{player_name} : {(record/100)}s"
                record_list.append(text_to_display)
                
            y = self.screen_center[1]
            
            for player_record_text in record_list:
                y_factor = self.height//8*self.divided_by
                self.draw_full_button(player_record_text,
                                (self.screen_center[0],
                                y + y_factor))
                self.divided_by += 1
            self.divided_by = -1.5
        else:
            text = f"Il n'y a pas encore eu de gagnants"
            self.draw_full_button(text, (self.screen_center[0],
                                self.screen_center[1] - self.height//8 * 0.5) )

        self.button_return = self.draw_full_button('Retour',
                                                        (self.screen_center[0],
                                                         self.screen_center[1] + self.height//8*1.5))

        return self.button_return
