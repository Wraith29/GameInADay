__all__ = ["SpiralBulletGenerator"]

import math
from copy import deepcopy
from pygame.math import Vector2
from ..bullet_controllers.bullet_controller import BulletController
from .bullet_generator import BulletGenerator
from ..player import Player
from ..bullet import Bullet


def bullet_modifier(vector: Vector2, frame_time: float, bullet_lifetime: float, **kwargs) -> Vector2:
    sin = math.sin(bullet_lifetime**-1 * frame_time)
    cos = math.cos(bullet_lifetime**-1 * frame_time)

    x = vector.x
    y = vector.y
    vector.x = (cos * x) - (sin * y)
    vector.y = (sin * x) + (cos * y)

    return vector

class SpiralBulletGenerator(BulletGenerator):
    def __init__(self, cooldown_time: int = 1) -> None:
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
            bullet_controller.add_bullet(Bullet(deepcopy(position), Vector2(1, 0), bullet_modifier))
            bullet_controller.add_bullet(Bullet(deepcopy(position), Vector2(-1, 0), bullet_modifier))
            bullet_controller.add_bullet(Bullet(deepcopy(position), Vector2(0, 1), bullet_modifier))
            bullet_controller.add_bullet(Bullet(deepcopy(position), Vector2(0, -1), bullet_modifier))

            self.total_time += self.cooldown
