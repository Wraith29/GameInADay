__all__ = ["BulletGenerator"]

from abc import ABC
from pygame.math import Vector2
from ..bullet_controllers.bullet_controller import BulletController
from ..bullets.simple_bullet import SimpleBullet


class BulletGenerator(ABC):
    __slots__ = ("cooldown", "total_time", "bullet_type")

    total_time: float
    cooldown: float
    bullet_type: type

    def __init__(self, cooldown: float | int, bullet_type: type = SimpleBullet) -> None:
        self.total_time = 0
        self.cooldown = cooldown
        self.bullet_type = SimpleBullet

    def update(self, frame_time: float, position: Vector2, bullet_controller: BulletController, **kwargs) -> None:
        """Virtual Method"""
        raise NotImplementedError("Virtual Method Accessed")
