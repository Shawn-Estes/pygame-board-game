import pygame


class Button:
    def __init__(self, screen, text, pos, font_size, color="black", onclick=None):
        self.screen = screen
        self.font = pygame.font.SysFont("Impact", font_size)
        self.text = self.font.render(text, True, color)
        self.hover_text = self.font.render(text, True, (55, 55, 55))
        center_x = (screen.get_width() / 2) - (self.text.get_width() / 2)
        center_y = (screen.get_height() / 2) - (self.text.get_height() / 2)
        self.pos = (center_x, center_y + pos)

        self.onclick = onclick

    def render(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.text.get_rect().move(self.pos).collidepoint(mouse_pos):
            self.screen.blit(self.hover_text, self.pos)
            return
        self.screen.blit(self.text, self.pos)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.text.get_rect().move(self.pos).collidepoint(mouse_pos):
            self.onclick()
