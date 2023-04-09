__all__ = ["Text"]

from pygame.font import Font, SysFont
from pygame.surface import Surface
from pygame.rect import Rect

from ..colour import Colour

class Text:
    __slots__ = ("font", "surface", "location")
    font: Font
    surface: Surface
    location: Rect

    def __init__(self, text: str, size: int, location: Rect) -> None:
        self.font = SysFont("", size)
        self.surface = self.font.render(text, False, Colour.White)
        self.location = location

    def change_text(self, text: str):
        self.surface = self.font.render(text, False, Colour.White)

    def draw(self, surface: Surface):
        self.surface.blit(surface, self.location)