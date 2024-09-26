import pygame
from connect4.board import Board


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = False
        self.player1 = True
        self.board = Board(self.screen)
        self.win = False

    def start(self):
        self.running = True
        self.player1 = True
        self.win = False

        self.game_loop()

    def game_loop(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.board.place_token(self.player1):
                        if self.board.check_win():
                            self.running = False
                            self.win = True
                            break
                        self.player1 = not self.player1

            if not self.running:
                break
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

            # RENDER YOUR GAME HERE
            self.board.print_board()

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)

        if self.win:
            self.win_screen()

    def win_screen(self):
        running = True
        self.board.print_board()

        winner = "Player 1 Wins!" if self.player1 else "Player 2 Wins!"

        font = pygame.font.SysFont("Impact", 75)
        text = font.render(winner, True, (255, 255, 255))
        center_x = (self.screen.get_width() / 2) - (text.get_width() / 2)
        center_y = (self.screen.get_height() / 2) - (text.get_height() / 2)

        while running:
            self.screen.blit(text, (center_x, center_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(60)
