__all__ = ["BulletGenerator"]

from abc import ABC
from pygame.math import Vector2
from ..bullet_controller import BulletController


class BulletGenerator(ABC):
    __slots__ = ("cooldown", "total_time")

    total_time: float
    cooldown: float

    def __init__(self) -> None:
        self.total_time = 0
        self.cooldown = 0

    def update(self, frame_time: float, position: Vector2, bullet_controller: BulletController, **kwargs) -> None:
        """Virtual Method"""
        raise NotImplementedError("Virtual Method")
