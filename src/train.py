import pygame


# Define train class
class Train:
    def __init__(self, line, color, speed):
        self.line = line
        self.color = color
        self.speed = speed
        self.current_index = 0
        self.x, self.y = self.line.get_points()[self.current_index]

    def update(self):
        points = self.line.get_points()
        if self.current_index < len(points) - 1:
            next_x, next_y = points[self.current_index + 1]
            dx, dy = next_x - self.x, next_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > self.speed:
                self.x += self.speed * dx / distance
                self.y += self.speed * dy / distance
            else:
                self.x, self.y = next_x, next_y
                self.current_index += 1
        else:
            self.current_index = 0  # Loop back to the start
            self.x, self.y = points[self.current_index]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)