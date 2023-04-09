from pygame.rect import Rect
from pygame import mouse as Mouse
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

    def is_within_button(self, pos: tuple[int, int]) -> bool:
        return self.location.contains(Rect(pos[0], pos[1], 0, 0))

    def draw(self):
        mouse_pos = Mouse.get_pos()
        if self.is_within_button(mouse_pos):
            self.colour = Colour.darken(self.colour, 80)
        else:
            self.colour = Colour.lighten(self.colour, 80)
