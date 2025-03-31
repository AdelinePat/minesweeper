from view.menu import Menu
from view.__settings__ import TITLE_FONT, CELESTE

class RollOfFame(Menu):
    def __init__(self, controller, caption="Palmarès"):
        super().__init__(caption)
        self.caption
        self.controller = controller
        self.data_acces = self.controller.data_access
        self.game_controller = self.controller.game_controller
        self.divided_by = -1.5

    def draw_wall_of_fame_menu(self):
        self.set_caption(self.caption)
        if self.controller.resolution != self.resolution:
            self.controller.resolution = self.controller.settings_screen.resolution
            self.get_resolution(self.controller.resolution) 
            self.get_actual_menu_window()
            
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
                player_name = player_record[0].split()[0] + " (" + player_record[0].split()[1] + ")"
                record = player_record[1]
                seconds = (record//100) % 60
                rest = record%100
                minutes = (record//100) // 60
                if minutes != 0:
                    text_to_display = f"{player_name} : {minutes:02d}min {seconds:02d}s {rest}"
                else:
                    text_to_display = f"{player_name} : {seconds:02d}s {rest}"
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

        self.button_return = self.medium_button(
            'Retour',
            (self.screen_center[0],
            self.screen_center[1] + self.height // 8 * 1.5)
        )

        return self.button_return
