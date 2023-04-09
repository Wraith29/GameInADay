__all__ = ["SpiralBulletGenerator"]

import math
from pygame.math import Vector2
from ..bullet_controller import BulletController
from .bullet_generator import BulletGenerator
from ..player import Player
from ..bullet import Bullet


def bullet_modifier(vector: Vector2, frame_time: float) -> Vector2:
    sin = math.sin(5 * frame_time)
    cos = math.cos(5 * frame_time)

    x = vector.x
    y = vector.y
    vector.x = (cos * x) - (sin * y)
    vector.y = (sin * x) + (cos * y)

    return vector.normalize() * 1.5


class SpiralBulletGenerator(BulletGenerator):
    def __init__(self, cooldown_time: int = 1):
        BulletGenerator.__init__(self)
        self.cooldown = cooldown_time

    def update(
                self,
                frame_time: float,
                position: Vector2,
                bullet_controller: BulletController,
                player: Player,
                **kwargs
              ) -> None:
        self.total_time -= frame_time

        if self.total_time < 0:
            bullet_controller.add_bullet(Bullet(position, Vector2(1, 0)))
            bullet_controller.add_bullet(Bullet(position, Vector2(-1, 0)))
            bullet_controller.add_bullet(Bullet(position, Vector2(0, 1)))
            bullet_controller.add_bullet(Bullet(position, Vector2(0, -1)))

            self.total_time += self.cooldown
