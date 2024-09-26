import pygame
from tic_tac_toe.tokens import Token


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.DIST = 100
        self.WIDTH = 10
        self.board = []
        self.previous = []

        for i in range(3):
            self.board.append([Token.EMPTY, Token.EMPTY, Token.EMPTY])

    def print_board(self):
        center = list(self.screen.get_rect().center)
        bg_offset = self.DIST * 1.5
        sm_offset = self.DIST / 2
        self.line([center[0] - sm_offset, center[1] - bg_offset], [center[0] - sm_offset, center[1] + bg_offset])
        self.line([center[0] + sm_offset, center[1] - bg_offset], [center[0] + sm_offset, center[1] + bg_offset])

        self.line([center[0] - bg_offset, center[1] - sm_offset], [center[0] + bg_offset, center[1] - sm_offset])
        self.line([center[0] - bg_offset, center[1] + sm_offset], [center[0] + bg_offset, center[1] + sm_offset])

        for y_index, row in enumerate(self.board, -1):
            for x_index, token in enumerate(row, -1):
                pos = [center[0] + (self.DIST * x_index), center[1] + (self.DIST * y_index)]
                if token == Token.O:
                    pygame.draw.circle(self.screen, "blue", pos, self.DIST / 3, 5)
                elif token == Token.X:
                    self.draw_x(pos)

    def get_clicked_pos(self):
        pos = [None, None]
        mouse_pos = pygame.mouse.get_pos()
        center = list(self.screen.get_rect().center)

        previous_column = center[0] - (self.DIST * 1.5)
        for i in range(3):
            new_column = previous_column + self.DIST
            if previous_column <= mouse_pos[0] <= new_column:
                pos[1] = i
                break
            previous_column = new_column

        previous_column = center[1] - (self.DIST * 1.5)
        for i in range(3):
            new_column = previous_column + self.DIST
            if previous_column <= mouse_pos[1] <= new_column:
                pos[0] = i
                break
            previous_column = new_column

        return pos

    def place_token(self, player1):
        pos = self.get_clicked_pos()

        if pos[0] is None or pos[1] is None:
            return False
        if self.board[pos[0]][pos[1]] != Token.EMPTY:
            return False

        token = Token.X if player1 else Token.O
        self.board[pos[0]][pos[1]] = token
        self.previous = [pos[0], pos[1], token]
        return True

    def check_horizontal(self):
        for row in self.board:
            if (row[0] == row[1] == row[2]) and row[0] != Token.EMPTY:
                return True
        return False

    def check_vertical(self):
        for i in range(3):
            if (self.board[0][i] == self.board[1][i] == self.board[2][i]) and self.board[0][i] != Token.EMPTY:
                return True
        return False

    def check_diagonal(self):
        top_bottom = (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != Token.EMPTY
        bottom_top = (self.board[2][0] == self.board[1][1] == self.board[0][2]) and self.board[2][0] != Token.EMPTY

        return top_bottom or bottom_top

    def check_win(self):
        return self.check_vertical() or self.check_horizontal() or self.check_diagonal()

    def line(self, start_pos, end_pos, color="black", width=10):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)

    def draw_x(self, pos):
        offset = self.DIST / 3
        self.line([pos[0] - offset, pos[1] + offset], [pos[0] + offset, pos[1] - offset], color="red", width=5)
        self.line([pos[0] - offset, pos[1] - offset], [pos[0] + offset, pos[1] + offset], color="red", width=5)
