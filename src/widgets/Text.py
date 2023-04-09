__all__ = ["Text"]

from pygame.font import Font, SysFont
from pygame.surface import Surface
from pygame.rect import Rect

from ..colour import Colour

class Text:
    __slots__ = ("font", "surface", "location", "colour", "center")
    font: Font
    surface: Surface
    location: Rect
    colour: tuple[int, int, int]
    center: bool

    def __init__(self, text: str, size: int, location: Rect, colour: tuple[int, int, int], center: bool = False) -> None:
        self.font = SysFont("", size)
        self.location = location
        self.colour = colour
        self.center = center
        self.set_text(text)

    def set_text(self, text: str) -> None:
        temp_rect = self.location
        self.surface = self.font.render(text, True, self.colour)
        self.location = self.surface.get_rect()
        self.location.center = (temp_rect.x, temp_rect.y)

    def draw(self, surface: Surface) -> None:
        surface.blit(self.surface, self.location)