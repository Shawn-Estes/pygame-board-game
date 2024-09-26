import pygame
from connect4.tokens import Tokens


class Board:

    def __init__(self, screen):
        self.screen = screen
        self.board = []
        self.previous_token = []
        self.WIDTH = 7
        self.HEIGHT = 6
        self.SIZE = 35
        self.OFFSET = 20 + self.SIZE * 2

        for i in range(self.WIDTH):
            temp = []
            for j in range(self.HEIGHT):
                temp.append(Tokens.EMPTY)
            self.board.append(temp)

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                token = self.board[i][j]
                center = [self.SIZE + 10 + i * self.OFFSET, self.SIZE + 10 + j * self.OFFSET]

                if token == Tokens.EMPTY:
                    pygame.draw.circle(self.screen, "gray", center, self.SIZE)
                elif token == Tokens.PLAYER_1:
                    pygame.draw.circle(self.screen, "red", center, self.SIZE)
                elif token == Tokens.PLAYER_2:
                    pygame.draw.circle(self.screen, "yellow", center, self.SIZE)

    def get_column_clicked(self):
        mouse_pos = pygame.mouse.get_pos()

        previous_column = 0
        for i in range(self.WIDTH):
            new_column = previous_column + self.OFFSET
            if previous_column <= mouse_pos[0] <= new_column:
                return i
            previous_column = new_column

        raise Exception("You can't click there")

    def place_token(self, player1):
        column = self.get_column_clicked()
        if self.board[column][0] != Tokens.EMPTY:
            return False
        token = Tokens.PLAYER_1 if player1 else Tokens.PLAYER_2

        self.board[column][0] = token
        self.previous_token = [column, 0, token]
        for i in range(self.HEIGHT - 1):
            if self.board[column][i + 1] == Tokens.EMPTY:
                self.board[column][i] = Tokens.EMPTY
                self.board[column][i + 1] = token
                self.previous_token = [column, i + 1, token]

        return True

    def check_vertical(self):
        for i in range(4):
            try:
                if self.previous_token[2] != self.board[self.previous_token[0]][self.previous_token[1] + i]:
                    return False
            except IndexError:
                return False
        return True

    def check_horizontal(self):
        left = True
        right = True
        for i in range(4):
            try:
                if self.previous_token[2] != self.board[self.previous_token[0] - i][self.previous_token[1]]:
                    left = False
            except IndexError:
                left = False
            try:
                if self.previous_token[2] != self.board[self.previous_token[0] + i][self.previous_token[1]]:
                    right = False
            except IndexError:
                right = False

            if not right and not left:
                return False
        return True

    def check_diagonal(self):
        top_left = True
        bottom_left = True
        top_right = True
        bottom_right = True
        for i in range(4):
            try:
                if self.previous_token[2] != self.board[self.previous_token[0] - i][self.previous_token[1] - i]:
                    top_left = False
            except IndexError:
                top_left = False
            try:
                if self.previous_token[2] != self.board[self.previous_token[0] - i][self.previous_token[1] + i]:
                    bottom_left = False
            except IndexError:
                bottom_left = False
            try:
                if self.previous_token[2] != self.board[self.previous_token[0] + i][self.previous_token[1] - i]:
                    top_right = False
            except IndexError:
                top_right = False
            try:
                if self.previous_token[2] != self.board[self.previous_token[0] + i][self.previous_token[1] + i]:
                    bottom_right = False
            except IndexError:
                bottom_right = False

            if not bottom_left and not top_left and not bottom_right and not top_right:
                return False
        return True

    def check_win(self):
        return self.check_vertical() or self.check_horizontal() or self.check_diagonal()
