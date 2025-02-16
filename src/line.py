from typing import List

import pygame

from src.stations import TrainStation


class Line:
    def __init__(self, name: str, stations: List[TrainStation], color=(0, 0, 0)):
        self.name = name
        self.stations = stations
        self.color = color

    def get_points(self):
        return [station.get_position() for station in self.stations]

    def draw(self, screen):
        pygame.draw.lines(screen, self.color, False, self.get_points(), 5)
