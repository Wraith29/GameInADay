from pygame.rect import Rect
from pygame import mouse as Mouse
from pygame import draw
from pygame.surface import Surface
from .text import Text
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

        if center:
            self.location.center = (self.location.x, self.location.y)

    def is_within_button(self, pos: tuple[int, int]) -> bool:
        return self.location.contains(Rect(pos[0], pos[1], 0, 0))

    def draw(self, window: Surface):
        mouse_pos = Mouse.get_pos()
        if self.is_within_button(mouse_pos):
            self.colour = Colour.darken(self.colour, 80)
        else:
            self.colour = Colour.lighten(self.colour, 80)
        
        draw.rect(window, self.colour, self.location)
        self.text.draw(window)

        '''
        this class needs callable and a method to check if its being clicked on
        the text size is hardcoded but that should be fine for this
        '''