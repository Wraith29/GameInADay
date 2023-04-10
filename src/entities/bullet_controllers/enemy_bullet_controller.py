__all__ = ["EnemyBulletController"]


from pygame.surface import Surface
from pygame.sprite import Group as SpriteGroup, spritecollide
from ..bullets.bullet import Bullet
from .bullet_controller import BulletController
from ..player import Player
from src.playarea import PlayArea
from ...consts import ENEMY_HIT_MULTIPLIER


class EnemyBulletController(BulletController):
    __slots__ = ("bullet_group")
    bullet_group: SpriteGroup

    def __init__(self) -> None:
        self.bullet_group = SpriteGroup()

    def update(self, frame_time: float, player: Player, play_area: PlayArea, **kwargs) -> None:
        collisions = spritecollide(player, self.bullet_group, True)
        if len(collisions) > 0:
            play_area.add_temp_multiplier(ENEMY_HIT_MULTIPLIER * len(collisions), 0.5)

        self.bullet_group.update(frame_time, bullet_controller = self, **kwargs)

    def draw(self, window: Surface) -> None:
        self.bullet_group.draw(window)

    def add_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.add(bullet)

    def remove_bullet(self, bullet: Bullet) -> None:
        self.bullet_group.remove(bullet)
