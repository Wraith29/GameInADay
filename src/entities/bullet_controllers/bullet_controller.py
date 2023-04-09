__all__ = ["BulletController"]

from abc import ABC
from pygame.sprite import Group as SpriteGroup
from pygame.surface import Surface
from ..bullet import Bullet


class BulletController(ABC):
    __slots__ = ("bullet_group")

    bullet_group: SpriteGroup

    def __init__(self) -> None:
        self.bullet_group = SpriteGroup()

    def update(self, frame_time: float, **kwargs) -> None:
        raise NotImplementedError("Virutal Method Accessed")

    def draw(self, window: Surface) -> None:
        raise NotImplementedError("Virtual Method Accessed")

    def add_bullet(self, bullet: Bullet) -> None:
        raise NotImplementedError("Virtual Method Accessed")

    def remove_bullet(self, bullet: Bullet) -> None:
        raise NotImplementedError("Virtual Method Accessed")
