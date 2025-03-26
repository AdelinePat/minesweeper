from view.settings import Settings

class MenuController():
    def __init__(self):
        self.is_screen_settings = False
        self.is_screen_record = False
        self.is_screen_main = True
        self.is_screen_win = False
        self.is_screen_in_game = False


    def screen_access(self):
        """Controls screen transitions based on the flags."""
        if self.is_screen_in_game:

            print("This is the game screen.")
        elif self.is_screen_settings:
            # self.is_screen_main = False
            self.settings_screen = Settings()
            self.settings_screen.draw_settings_screen()
            # self.settings_screen.update()

            print("This is the settings menu.")
        elif self.is_screen_record:
            print("This is the top 3 players screen.")
        elif self.is_screen_main:
            print("This is the main menu.")

    def start_game(self):
        """Placeholder for starting the game."""
        if self.is_screen_in_game:
            print("This is the game screen.")
        pass

    def set_settings(self):
        """Handle settings screen access."""
        if self.is_screen_settings:
            print("This is the settings menu.")
        pass

    def go_to_main_menu(self):
        """Switch to the main menu."""
        self.is_screen_main = True
        self.is_screen_settings = False
        self.is_screen_in_game = False
        print("Going back to the main menu.")

    def go_to_settings(self):
        """Switch to the settings screen."""
        self.is_screen_main = False
        self.is_screen_settings = True
        print("Switching to the settings menu.")

