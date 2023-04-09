__all__ = ["Game"]

import pygame
from pygame.locals import K_ESCAPE
from pygame.surface import Surface
from pygame.time import Clock
from .map import Map
from .colour import Colour

from .consts import WINDOW_WIDTH, WINDOW_HEIGHT


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

    def run(self) -> None:
        while True:
            self.window.fill(Colour.White)
            
            frame_time = self.clock.tick()/1000
            events = pygame.event.get()
            for event in events:
                match event.type:
                    case pygame.KEYDOWN:
                        if pygame.key.get_pressed()[K_ESCAPE]:
                            quit()
                            
                    case pygame.QUIT:
                        quit()
                    

            self.game_map.update(frame_time)

            self.game_map.draw(self.window)

            pygame.display.flip()
