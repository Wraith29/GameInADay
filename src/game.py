__all__ = ["Game"]

import pygame
from pygame.surface import Surface
from .consts import WINDOW_WIDTH, WINDOW_HEIGHT


class Game:
    __slots__ = ("window")
    window: Surface

    def __init__(self) -> None:
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Our really cool game!")

    def run(self) -> None:
        ...
