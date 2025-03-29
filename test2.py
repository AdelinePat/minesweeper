from view.main_menu import MainMenu
from view.settings_menu import SettingsMenu
from controller.menu_controller import MenuController
import pygame

menu_controller = MenuController()
main_menu = MainMenu('Minesweeper')
settings_menu = SettingsMenu(menu_controller)
main_menu.main_loop()