__all__ = ["Game"]

import pygame
from pygame.locals import K_ESCAPE
from pygame.surface import Surface
from pygame.time import Clock
from .map import Map
from .colour import Colour

from .consts import WINDOW_WIDTH, WINDOW_HEIGHT, FPS


class Game:
    __slots__ = ("window", "clock", "frame_time", "game_map")
    frame_time: int
    window: Surface
    clock: Clock
    game_map: Map

    def __init__(self) -> None:
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = Clock()

        pygame.display.set_caption("Our really game!")

        self.game_map = Map()

    def checkEvents(self) -> None:
        events = pygame.event.get()
        for event in events:
            match event.type:
                case pygame.KEYDOWN:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        quit()
                        
                case pygame.QUIT:
                    quit()

    def run(self) -> None:
        while True:
            self.window.fill(Colour.Black)
            frame_time = self.clock.tick()/1000

            if self.game_map.has_player_died():
                print("player died")
                return

            self.checkEvents()

            self.game_map.update(frame_time)

            self.game_map.draw(self.window)

            pygame.display.flip()

    def display_end_screen(self) -> None:
        while True:
            self.window.fill(Colour.Black)

            self.checkEvents()

            pygame.display.flip()
