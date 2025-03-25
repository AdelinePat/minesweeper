class MenuController:
    def __init__(self):
        # Dictionary to store different screens
        self.screens = {
            "main": "Main Menu",
            "game": "Starting the game...",
            "settings": "Displaying settings...",
            "record": "Showing leaderboard..."
        }
        self.current_screen = "main"  # Default screen

    def change_screen(self, screen_name):
        """Switch the active screen and display a message."""
        if screen_name in self.screens:
            self.current_screen = screen_name
            print(f"Screen changed: {self.screens[screen_name]}")
        else:
            print(f"Error: Screen '{screen_name}' does not exist!")

    def screen_access(self):
        """Display a message based on the current screen."""
        print(self.screens.get(self.current_screen, "Unknown screen"))

    def start_game(self):
        """Switch to the game screen."""
        self.change_screen("game")

    def set_settings(self):
        """Switch to the settings screen."""
        self.change_screen("settings")

    def show_leaderboard(self):
        """Display the leaderboard."""
        self.change_screen("record")
