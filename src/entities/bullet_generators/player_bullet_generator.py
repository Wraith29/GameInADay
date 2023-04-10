__all__ = ["PlayerBulletGenerator"]

import pygame

from pygame.math import Vector2
from ..bullet_controllers.bullet_controller import BulletController
from .bullet_generator import BulletGenerator
from ..bullets.player_bullet import PlayerBullet


class PlayerBulletGenerator(BulletGenerator):
    def __init__(self, cooldown : int | float = 1, bullet_type: type = PlayerBullet):
        BulletGenerator.__init__(self, cooldown, bullet_type)

    def update(self, frame_time: float, position: Vector2, bullet_controller: BulletController, **kwargs) -> None:
        self.total_time -= frame_time

        if self.total_time < 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            target_pos = Vector2(mouse_x, mouse_y)  # Get the player position here
            bullet_controller.add_bullet(self.bullet_type(position, (target_pos-position).normalize()))

                self.total_time += self.cooldown
