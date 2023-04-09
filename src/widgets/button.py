from pygame.rect import Rect
from text import Text
from ..colour import Colour


_all_ = ["button"]

class Button:
    __slots__ = ("text", "location", "colour", "center")
    text: Text
    location: Rect
    colour: tuple[int, int, int]
    center: bool

    def __init__(self, 
                 text: str,
                 location: Rect,
                 colour: tuple[int, int, int],
                 center: bool
                 ) -> None:
        self.text = Text(text, 20, location, Colour.darken(Colour.White), True)
        self.location = location
        self.colour = colour
        self.center = center

