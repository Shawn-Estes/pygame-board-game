import pygame
import connect4
import tic_tac_toe
from button import Button

# pygame setup
pygame.init()
screen = pygame.display.set_mode((630, 540))
pygame.display.set_caption("Final Project")
clock = pygame.time.Clock()

main_font = pygame.font.SysFont("Impact", 50)
main_text = main_font.render("Board Game Bonanza", True, "Black")
center_x = (screen.get_width() / 2) - (main_text.get_width() / 2)
center_y = (screen.get_height() / 2) - (main_text.get_height() / 2)

connect4_button = Button(screen, "Connect 4", 50, 50)
connect4_button.onclick = lambda: connect4.Game(screen, clock).start()

tic_button = Button(screen, "Tic-Tac-Toe", -50, 50)
tic_button.onclick = lambda: tic_tac_toe.Game(screen, clock).start()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            connect4_button.check_click()
            tic_button.check_click()

    screen.fill("white")

    # RENDER YOUR GAME HERE
    connect4_button.render()
    tic_button.render()
    screen.blit(main_text, (center_x, center_y - 200))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
