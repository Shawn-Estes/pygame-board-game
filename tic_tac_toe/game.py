import pygame
from tic_tac_toe.board import Board


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.board = Board(self.screen)
        self.running = False
        self.player1 = True
        self.win = False
        self.moves = 0

    def start(self):
        self.running = True
        self.player1 = True
        self.win = False
        self.moves = 0

        self.game_loop()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.board.place_token(self.player1):
                        self.player1 = not self.player1
                        self.win = self.board.check_win()
                        self.moves += 1

            self.screen.fill("white")

            # RENDER YOUR GAME HERE
            self.board.print_board()

            if self.win:
                self.running = False
            elif not self.win and self.moves == 9:
                self.running = False

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)

        if self.moves != 9 and not self.win:
            return
        self.end_screen()

    def end_screen(self):
        self.running = True

        winner = "Draw!"

        if self.player1 and self.win:
            winner = "O Wins!"
        elif not self.player1 and self.win:
            winner = "X Wins!"

        font = pygame.font.SysFont("Impact", 75)
        text = font.render(winner, True, (50, 50, 50))
        center_x = (self.screen.get_width() / 2) - (text.get_width() / 2)
        center_y = (self.screen.get_height() / 2) - (text.get_height() / 2)

        while self.running:
            self.screen.blit(text, (center_x, center_y - 210))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            self.clock.tick(60)
