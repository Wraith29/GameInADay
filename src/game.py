__all__ = ["Game"]

import pygame
from pygame.locals import K_ESCAPE
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.time import Clock

from .map import Map
from .colour import Colour
from .consts import WINDOW_WIDTH, WINDOW_HEIGHT
from .widgets.Text import Text


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

    def handle_events(self) -> None:
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

            self.handle_events()

            self.game_map.update(frame_time)
            self.game_map.draw(self.window)

            pygame.display.flip()

    def display_end_screen(self) -> None:
        text_rect = Rect(0, 0, 0, 0)
        text_rect.center = (int(WINDOW_WIDTH/2), int(WINDOW_HEIGHT/2))
        end_text = Text("Game End", 150, text_rect, Colour.Pink, True)

        text_hide = Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        text_hide.fill(Colour.Black)

        end_time = pygame.time.get_ticks()

        fade_start_delay = 1500
        while True:
            self.window.fill(Colour.Black)

            self.handle_events()

            end_text.draw(self.window)

            time_since_end = pygame.time.get_ticks() - end_time
            if time_since_end > fade_start_delay:
                fade_value = time_since_end - fade_start_delay
                text_hide.set_alpha(int(255 - (fade_value/10)))

            self.window.blit(text_hide, Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))


            pygame.display.flip()
