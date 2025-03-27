import pygame, sys
from view.__settings__ import TITLE_FONT, CELESTE
from view.menu import Menu

pygame.init()

# Инициализация главного меню
screen_main_menu = Menu('Minesweeper - Main menu')

while True:
    # Отрисовка заголовка игры
    my_title = screen_main_menu.draw_text(
        'Minesweeper',
        TITLE_FONT,
        screen_main_menu.height // 9,
        screen_main_menu.title_center,
        color=CELESTE
    )

    # Кнопки меню
    button_play = screen_main_menu.draw_full_button(
        'Jouer',
        (screen_main_menu.screen_center[0], screen_main_menu.screen_center[1] - screen_main_menu.height // 8 * 1.5)
    )

    button_settings = screen_main_menu.draw_full_button(
        'Paramètres',
        (screen_main_menu.screen_center[0], screen_main_menu.screen_center[1] - screen_main_menu.height // 8 * 0.5)
    )

    button_record = screen_main_menu.draw_full_button(
        'Palmarès',
        (screen_main_menu.screen_center[0], screen_main_menu.screen_center[1] + screen_main_menu.height // 8 * 0.5)
    )

    small_button = screen_main_menu.small_button(
        'POO PI POO PI POOOOO',
        (screen_main_menu.screen_center[0], screen_main_menu.screen_center[1] + screen_main_menu.height // 8 * 1.5)
    )

    # Получение позиции курсора мыши
    mouse_position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка, если нажата кнопка "Jouer"
            if button_play.collidepoint(mouse_position):
                print("Запуск игры")
                # Добавьте логику для перехода к игре

            # Проверка, если нажата кнопка "Paramètres"
            if button_settings.collidepoint(mouse_position):
                print("Открытие настроек")
                # Добавьте логику для открытия настроек

            # Проверка, если нажата кнопка "Palmarès"
            if button_record.collidepoint(mouse_position):
                print("Просмотр рекордов")
                # Добавьте логику для отображения рекордов

            # Проверка, если нажата маленькая кнопка "POO PI POO PI POOOOO"
            if small_button.collidepoint(mouse_position):
                print("Нажата кнопка POO PI POO PI POOOOO")

        if event.type == pygame.KEYDOWN:
            print("Клавиша была нажата")

    # Обновление экрана
    screen_main_menu.update()

pygame.quit()