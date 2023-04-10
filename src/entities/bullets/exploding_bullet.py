__all__ = ["ExplodingBullet"]

from math import sin, cos
from math import pi as PI

from random import random
from copy import deepcopy
from typing import Callable

from pygame.math import Vector2

from .bullet import Bullet
from .simple_bullet import SimpleBullet
from ..bullet_controllers.bullet_controller import BulletController

class ExplodingBullet(Bullet):
    def __init__(
                 self,
                 start_position: Vector2,
                 movement_vector: Vector2,
                 movement_speed: int | float = 100,
                 movement_modifier: Callable | None = None,
                 fuze: int | float = 3,
                 **kwargs
                ) -> None:
        Bullet.__init__(self, start_position, movement_vector, movement_speed, movement_modifier)
        self.set_texture("sprites/ExplodingBullet.png", start_position.x, start_position.y)
        self.fuze = fuze
    
    def update(self, frame_time: float, bullet_controller: BulletController, **kwargs) -> None:
        self.lifetime += frame_time
        self.position += self.movement_vector * self.movement_speed * frame_time

        def calculate_vector(angle: float) -> Vector2:
            vector = Vector2(1, 0)
            
            sinA = sin(angle)
            cosA = cos(angle)

            x = vector.x
            y = vector.y
            vector.x = (cosA * x) - (sinA * y)
            vector.y = (sinA * x) + (cosA * y)

            return vector

        if self.lifetime > self.fuze:
            random_offset = random() * PI
            bullet_controller.add_bullet(SimpleBullet(deepcopy(self.position), calculate_vector(random_offset)))
            bullet_controller.add_bullet(SimpleBullet(deepcopy(self.position), calculate_vector(random_offset + 0.5 * PI)))
            bullet_controller.add_bullet(SimpleBullet(deepcopy(self.position), calculate_vector(random_offset + 1 * PI)))
            bullet_controller.add_bullet(SimpleBullet(deepcopy(self.position), calculate_vector(random_offset + 1.5 * PI)))
        
            bullet_controller.remove_bullet(self)


        
        else:
            if self.movement_modifier:
                self.movement_vector = self.movement_modifier(self.movement_vector, frame_time, bullet_lifetime=self.lifetime)

            self.rect.center = (int(self.position.x), int(self.position.y))