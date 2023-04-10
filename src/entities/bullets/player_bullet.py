__all__ = ["PlayerBullet"]

from typing import Callable
from pygame.math import Vector2
from .bullet import Bullet

class PlayerBullet(Bullet):
    def __init__(
                 self,
                 start_position: Vector2,
                 movement_vector: Vector2,
                 movement_speed: int | float = 200,
                 movement_modifier: Callable | None = None,
                 **kwargs
                ) -> None:
        Bullet.__init__(self, start_position, movement_vector, movement_speed, movement_modifier, **kwargs)
        self.set_texture("sprites/PlayerBullet.png", start_position.x, start_position.y)
