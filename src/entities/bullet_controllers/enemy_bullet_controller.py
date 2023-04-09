__all__ = ["EnemyBulletController"]

from pygame.surface import Surface
from pygame.sprite import Group as SpriteGroup, spritecollide
from ..bullet import Bullet
from .bullet_controller import BulletController
from ..player import Player
from src.play_area import PlayArea


class EnemyBulletController(BulletController):
    __slots__ = ("bullet_group")
    bullet_group: SpriteGroup

    def __init__(self) -> None:
        self.bullet_group = SpriteGroup()

    def update(self, frame_time: float, player: Player, play_area: PlayArea, **kwargs) -> None:
        collisions = spritecollide(player, self.bullet_group, True)
        play_area.add_temp_multiplier(1, 1 * len(collisions))

        self.bullet_group.update(frame_time, **kwargs)

    def draw(self, window: Surface) -> None:
        self.bullet_group.draw(window)

    def add_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.add(bullet)

    def remove_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.remove(bullet)
