__all__ = ["FlowerBulletGenerator"]

import math
from copy import deepcopy
from pygame.math import Vector2
from ..bullet_controllers.bullet_controller import BulletController
from .bullet_generator import BulletGenerator
from ..player import Player
from ..bullets.simple_bullet import SimpleBullet

def bullet_modifier(vector: Vector2, frame_time: float, **kwargs) -> Vector2:
    sin = math.sin(5 * frame_time)
    cos = math.cos(5 * frame_time)

    x = vector.x
    y = vector.y
    vector.x = (cos * x) - (sin * y)
    vector.y = (sin * x) + (cos * y)

    return vector.normalize() * 3


class FlowerBulletGenerator(BulletGenerator):
    def update(
                self,
                frame_time: float,
                position: Vector2,
                bullet_controller: BulletController,
                **kwargs
              ) -> None:
        self.total_time -= frame_time

        if self.total_time < 0:
            bullet_controller.add_bullet(self.bullet_type(deepcopy(position), Vector2(1, 0), movement_modifier=bullet_modifier))
            bullet_controller.add_bullet(self.bullet_type(deepcopy(position), Vector2(-1, 0), movement_modifier=bullet_modifier))
            bullet_controller.add_bullet(self.bullet_type(deepcopy(position), Vector2(0, 1), movement_modifier=bullet_modifier))
            bullet_controller.add_bullet(self.bullet_type(deepcopy(position), Vector2(0, -1), movement_modifier=bullet_modifier))

            self.total_time += self.cooldown
