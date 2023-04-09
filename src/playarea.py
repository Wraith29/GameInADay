from pygame import Rect


class PlayArea:
    def __init__(self, pWidth: int, pHeight: int, pMultiplier: float = 1.0) -> None:
        self.width = pWidth
        self.height = pHeight

        self._multiplier = pMultiplier
        self._temp_multipliers = []
        self.width = 1600
        self.height = 900

        self._rect = Rect((1600 - self.width) / 2, (900 - self.height) / 2, self.width, self.height)

    def update(self, frame_time: float) -> None:
        value = frame_time * self.multiplier * 10

        for temp_multiplier in self._temp_multipliers:
            temp_multiplier["time"] -= frame_time
            if temp_multiplier["time"] <= 0:
                self._temp_multipliers.remove(temp_multiplier)

        self.width = self.width - value * (16 / 25) * 1.5
        self.height = self.height - value * (9 / 25) * 1.5

        self._rect = Rect((1600 - self.width) / 2, (900 - self.height) / 2, self.width, self.height)

    def add_temp_multiplier(self, pMultiplier, pTime):
        self._temp_multipliers.append({"multiplier": pMultiplier, "time": pTime})

    @property
    def multiplier(self) -> float:
        calc = self._multiplier
        for temp_multiplier in self._temp_multipliers:
            calc += temp_multiplier["multiplier"]

        return calc

    @property
    def rect(self) -> Rect:
        return self._rect
