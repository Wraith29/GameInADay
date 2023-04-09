__all__ = ["PlayArea"]

from pygame import Rect
from dataclasses import dataclass


@dataclass(slots=True)
class Multiplier:
    multiplier: float
    time: float  # Is this in seconds or ms?


class PlayArea:
    __slots__ = ("width", "height", "_multiplier", "_temp_multipliers", "_rect")
    width: float
    height: float
    _multiplier: float
    _temp_multipliers: list[Multiplier]
    _rect: Rect
    starting_width: float
    starting_height: float

    def __init__(self, width: float, height: float, multiplier: float = 1.0) -> None:
        self.width = width
        self.height = height

        self._multiplier = multiplier
        self._temp_multipliers = []

        self.width = width
        self.height = height

        self._rect = Rect((1600 - self.width) / 2, (900 - self.height) / 2, self.width, self.height)

    def update(self, frame_time: float) -> None:
        for temp_multiplier in self._temp_multipliers:
            temp_multiplier.time -= frame_time
            if temp_multiplier.time <= 0:
                self._temp_multipliers.remove(temp_multiplier)

        self.width = min(1600.0, self.width - (frame_time * (16 / 25)) * self.multiplier)
        self.height = min(900.0, self.height - (frame_time * (9 / 25)) * self.multiplier)

        self._rect = Rect((1600 - self.width) / 2, (900 - self.height) / 2, self.width, self.height)

    def add_temp_multiplier(self, multiplier: float, time: float) -> None:
        self._temp_multipliers.append(Multiplier(multiplier, time))

    @property
    def multiplier(self) -> float:
        calc = self._multiplier
        for temp_multiplier in self._temp_multipliers:
            calc += temp_multiplier.multiplier

        return calc * 10

    @property
    def rect(self) -> Rect:
        return self._rect
