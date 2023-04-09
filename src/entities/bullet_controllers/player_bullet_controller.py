__all__ = ["PlayerBulletController"]

from pygame.surface import Surface
from pygame.sprite import Group as SpriteGroup, spritecollide

from src.playarea import PlayArea
from ..bullet import Bullet
from .bullet_controller import BulletController


class PlayerBulletController(BulletController):
    __slots__ = ("bullet_group")
    bullet_group: SpriteGroup

    def __init__(self) -> None:
        self.bullet_group = SpriteGroup()

    def update(self, frame_time: float, enemy_group: SpriteGroup, play_area: PlayArea, **kwargs) -> None:
        for bullet in self.bullet_group:
            collisions = spritecollide(bullet, enemy_group, True)
            play_area.add_temp_multiplier(15 * len(collisions), 1)
        self.bullet_group.update(frame_time, **kwargs)

    def draw(self, window: Surface) -> None:
        self.bullet_group.draw(window)

    def add_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.add(bullet)

    def remove_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.remove(bullet)
