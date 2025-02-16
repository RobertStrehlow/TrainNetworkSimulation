import pygame


# Define train class
class Train:
    def __init__(self, line, color, speed, station_current_idx, direction=True):
        self.line = line
        self.color = color
        self.speed = speed
        self.station_current_idx = station_current_idx
        self.direction = direction
        self.x, self.y = self.line.get_points()[self.station_current_idx]

    def update(self):
        points = self.line.get_points()
        if self.direction and self.station_current_idx < len(points) - 1:
            next_x, next_y = points[self.station_current_idx + 1]
            self._calculate_position(next_x, next_y)
        elif not self.direction and self.station_current_idx > 0:
            next_x, next_y = points[self.station_current_idx - 1]
            self._calculate_position(next_x, next_y)
        else:
            self.direction = not self.direction
            return

    def _calculate_position(self, next_x, next_y):
        dx, dy = next_x - self.x, next_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance > self.speed:
            self.x += self.speed * dx / distance
            self.y += self.speed * dy / distance
        else:
            self.x, self.y = next_x, next_y
            self.station_current_idx += 1 if self.direction else -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        font = pygame.font.SysFont(None, 20)
        text = font.render(self.line.name, True, (0, 0, 0))
        screen.blit(text, (self.x + 10, self.y - 10))
