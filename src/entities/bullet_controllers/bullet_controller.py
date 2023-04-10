__all__ = ["BulletController"]

from abc import ABC
from pygame.sprite import Group as SpriteGroup
from pygame.surface import Surface
from ..bullets.bullet import Bullet


class BulletController(ABC):
    __slots__ = ("bullet_group")

    bullet_group: SpriteGroup

    def __init__(self) -> None:
        self.bullet_group = SpriteGroup()

    def update(self, frame_time: float, **kwargs) -> None:
        self.bullet_group.update()

    def draw(self, window: Surface) -> None:
        self.bullet_group.draw(window)

    def add_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.add(bullet)

    def remove_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.remove(bullet)
