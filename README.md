# minesweeper file documentation

# Minesweeper

# Financial Management Tool

![preview main](minsweeper.png)

**Project Description**

The goal of this project is to create a financial management tool that allows users to track their bank accounts. Through a user-friendly graphical interface, the user can add, view, and search for transactions (deposits, withdrawals, transfers), all while benefiting from enhanced security to protect sensitive data.

The system relies on a database that stores all the necessary information for managing accounts, such as the transactions made, registered users, and their personal information.

---

## Main Features

1. **Transaction Management** :

   - The user can perform transactions such as deposits, withdrawals, or money transfers.
   - Each transaction contains a unique reference, a description, an amount, a date, and a type (withdrawal, deposit, or transfer)

2. **Security** :

   - A login module protects access to the application.
   - Registration of a new user with the necessary information (last name, first name, email, secure password).
   - The password is secured through a hashing system and must meet certain requirements (uppercase letters, lowercase letters, numbers,  
     special character).

3. **Transaction History** :

   - Displaying the complete transaction history of the user.
   - Advanced search of transactions based on various criteria: date, category, type, amount, etc.
   - The ability to filter transactions between two dates.

4. **Global financial overview.** :

   - Display of the current balance and monthly expenses.
   - Charts illustrating expenses by category and by month.
   - Alerts for overdrafts or other important financial events.

5. **Bank Account Management** (Optional):
   - Advanced functionality to allow a banker to manage their clients' accounts and perform transactions on their behalf.

---

## Technologies Used

- **Python** : Main Programming Language.
- **Pygame** : Library for creating games and multimedia applications..

## Prerequisites

Before running this project, you need to install the following libraries and tools:

1. **Python 3.x**
2. **MySQL Server** : To host the database.
3. **The following Python libraries:** :
   - `pygame`


You can install the necessary libraries using: `pip` :

```bash
pip install pygame
```

---

## Installation

1.  Clone this project to your local machine.
    ```bash
    git clone https://github.com/AdelinePat/minesweeper.git
    ```
2.  Access the project directory:

    ```bash
    git cd minesweeper
    ```

3.  Make sure pygame is installed on your machine.

4.  Create the `.env ` file to install the libraries

---

## Usage

1.  Running the Application:

```bash
python main.py
```

2.  You will be prompted to log in with your credentials or create an account if you don't have one.

3.  After logging in, you will be able to make transactions, view the transaction history, and check your finances..

## File Structure

📂 assets  
│ 📂 font  
│ 📂 icon    
| 📂 img  
│ 📂 img_cell    
|
📂 controller  
│ 📄 game_controller.py  
│ 📄 menu_controller.py   
│
📂 model  
│ 📄 game_board.py  
│ 📄 game_info.py  
│ 📄 square.py  
│ 📄 write_transactionquery.py  
│
📂 test  
│ 📄 test.py  
│ 📄 test3.py  
│ 📄 winner_buton.py  
│ 📄 winner_top_buton.py  
│
📂 view  
│ 📄 **settings**.py  
│ 📄 in_game_menu.py  
│ 📄 interface.py  
│ 📄 main_menu.py  
│ 📄 menu.py  
│ 📄 settings_menu.py  
│ 📄 winner_menu.py  
│ 📄 winner.py  
│ 📄 winner.py   
│
📄 .gitignore  
📄 main.py  
📄 README.md

---

**BDatabase**

The project uses a MySQL database to store user information, bank accounts, and transactions. Below is the structure of the tables:

1.**Users** : Contains user information (last name, first name, email, password). 2.**Bank_account** : Contains information about bank accounts linked to each user. 3.**transactions** : Contains information about transactions made between bank accounts..

The SQL script to initialize the database and insert sample data is included in the project. You can run it on your MySQL server to create the structure and insert the initial data.

---

# Contributing

This project was made by:

- [Eltigani Abdallah](https://github.com/eltigani-abdallah)
- [Adeline Patenne](https://github.com/AdelinePat/)
- [Florence Navet](https://github.com/florence-navet)
- [Yulia Sherstiuk](https://github.com/yuliia-sherstiuk)

### Licence

This project is licensed under the MIT License.

---

<!-- ![preview main](budget_buddy.png) -->






































# Controller
## Game_controller.py
IMPORTS: Game_info from model/game_info.py

INHERITS:



ATTRIBUTES: 

game_info:

OBJECT: a GameInfo object.

a class that stores game info from model.game_info



## menu_controller.py
IMPORTS:

INHERITS: 

a class that takes menu input and calls the necessary methods and functions to change menus.

ATTRIBUTES:

is_screen_settings:

BOOL: 

is_screen_main:

BOOL: 

is_screen_win:

BOOL:

is_screen_in_game:

BOOL:

### Methods
screen_access():

takes input of menu item clicked and calls a method to change to the next screen.
as of writing, this is a placeholder that prints text to the terminal.

start_game():

enters into the main game screen and starts the gameplay loop.
currently a placeholder.

set_settings():

enters the settings screen to change settings like language, screen resolution, etc.
currently a placeholder.

get_top_players():

enters a screen that displays the leaderboards, which is a list of the top three players, ordered by the time taken to win the game.
currently a placeholder

# model
## game_info.py
IMPORTS: height and width from view/`__settings__`.py

INHERITS: 

a class that passes settings to other classes to apply them

ATTRIBUTES: 

difficulty: 

INT: the difficulty of the game. more difficulties will be added over time

VALID VALUES: 0, 1

language:

STR: the language of the game. currently can take French FR and english EN

VALID VALUES: "fr", "en"

resolution:

TUPLE (INT, INT): the game resolution. can be adjusted from view/`__settings__`.py at the variables "width" and "height"

VALID VALUES: any int tuple, but change them in view/`__settings__`.py at the variables for consistency

grid_size:
/////////////////

mines_number:
/////////////////////

flag_number:
//////////////////////

interrogation_point_number:
//////////////////////////

mines_positions:

LIST(TUPLE):

time_start:
//////////////////////////

time_end: 
//////////////////////////




# view

## `__settings__`.py
IMPORTS: Theme from the pygame_menu library, a library for easily creating menus in pygame.

A file that contains settings that will be used throughout the game. also includes colors.

width (INT): screen width 

height (INT): screen height

RESOLUTION (TUPLE(INT)): a tuple of screen width and screen height

FPS (INT): Frames Per Second. the speed at which the game will run

: colors are obvious enough, but they're tuples of RGB values :

TITLE_FONT(STR): the path for the title font, jockeyOne-Regular

TEXT_FONT(STR): the path for the text font, Jersey10-Regular

CUSTOM_THEME(OBJECT): a pygame Theme object that defines the general theme of the game

## interface.py
IMPORTS: pygame, a python library for games and multimedia applications,

IMPORTS: RESOLUTION, INDIGO DYE, TITLE_FONT, TEXT_FONT from view/`__settings__`.py

Class Interface():

INHERITS: 

a class that manages the interface shown to the player.

ATTRIBUTES: 

caption(STR): 

the caption at the windows navigation bar.

VALID VALUES: any string of text

width(INT): 

screen width. takes the width from view/`__settings__`.py by default

VALID VALUES: any INT

height(INT): 

screen height. takes the height from view/`__settings__`.py by default

VALID VALUES: any INT

background_color(TUPLE(INT,INT,INT)):

the color for the game background.

VALID VALUES: TUPLE of 3 INT values where each value is between 0 and 255, any color in RGB basically

resolution(TUPLE(INT,INT)):

the game resolution. will take the resolution from view/`__settings__`.py by default

VALID VALUES: TUPLE of 2 INT values

screen(SURFACE): 

a pygame surface object that also sets the display resolution to the resolutions in view/`__settings__`.py by default

VALID VALUES: pygame.display.set_mode((INT,INT))

clock(OBJECT):

a pygame.time.Clock object, is used to maintain game speed

VALID VALUES: pygame.time.Clock objects

screen_center(TUPLE(INT,INT)):

the center of the screen.


title_center(TUPLE(INT,INT)):

the center of the title, useful for moving text

### Methods

update():

updates the screen using pygame.display.flip() and controls game speed using self.clock.tick(self.fps).


create_text_rect(text, font, font_size, position, color):

will load the font, render text using .render, passing text and color from the parameters into .render(), then turns said text into a rectangle using get_rect, setting the position from the parameter as the center.

RETURNS: dialog and the dialog rectangle




blit_text_from_rect(dialog, dialog_rect):

blits (which is basically putting multimedia on the screen) the dialog and dialog_rect passed in as parameters

RETURNS: None


draw_text(text, font, font_size, position, color):

loads font using pygame.font.Font, passing in font and font_size as parameters, then creates a pygame rect with the center being the position passed in the parameters above, then blits the text on the screen.

RETURNS dialog rectangle created above (dialog_rect)


## main_menu.py

IMPORTS: pygame, sys, Menu from view/menu, MenuController from controller/menu_controller, GameController from controller/game_controller, TITLE_FONT(font) and CELESTE(color) form view/`__settings`.py

a class that creates the main menu and the game window.

ATTRIBUTES:

menu(OBJECT): an object of Menu with the window caption passed in as an attribute

controller(OBJECT): a MenuController object

game_controller(OBJECT): a GameController object

### methods

main_loop():

the loop that creates the window, the titles and the buttons necessary to run the game.


## menu.py

IMPORTS: Interface from view/interface, multiple colors and TEXT_FONT from view/`__settings__`.py, pygame

Menu(caption, identification=0)

a class that creates windows (front end elements and not OS windows), large buttons, and small buttons

ATTRIBUTES:

identification(INT): placeholder

win_bg_color(TUPLE(INT,INT,INT)): background color for the window

win_width, win_height(INT): width and height of the small window where text will show up

### methods

draw_menu_window():

draws the white square in the middle of the screen and gives it a cerulean colored border

RETURNS: None


draw_full_button(button_text, center, background=GHOST_WHITE, background_hovered=AGRESSIVE_PINK, color=INDIGO_DYE, color_hover=GHOST_WHITE):

draws the full button on the screen, "full button" means the button where there is a ribbon that spans the width of the mini window in the middle of the screen.

also checks if the button is hovered by the mouse and if it is clicked or not

RETURNS: something useful I guess

small_button( button_text, center, background=CYAN, background_hovered=AGRESSIVE_PINK, color=INDIGO_DYE, color_hover=GHOST_WHITE):

same as the previous method except that the button itself is a pill shaped button.

RETURNS: small_button







