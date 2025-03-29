import pygame
from view.wall_of_fame_menu import Wall_of_fame_menu

pygame.init()

main_menu = Wall_of_fame_menu()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_menu.draw_wall_of_fame_menu()

  
    pygame.display.flip()

pygame.quit()


