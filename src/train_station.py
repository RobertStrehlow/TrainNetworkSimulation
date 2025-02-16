import pygame


class TrainStation:
    def __init__(self, name, x, y, bold=False):
        self.name = name
        self.x = x
        self.y = y
        self.bold = bold

    def get_position(self):
        return self.x, self.y

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 8)
        font = pygame.font.SysFont(None, 20, bold=self.bold)
        text = font.render(self.name, True, (0, 0, 0))
        screen.blit(text, (self.x + 10, self.y - 10))
