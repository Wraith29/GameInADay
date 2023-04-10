__all__ = ["SimpleBulletGenerator"]

from copy import deepcopy
from pygame.math import Vector2
from ..bullet_controllers.bullet_controller import BulletController
from .bullet_generator import BulletGenerator
from ..player import Player

class SimpleBulletGenerator(BulletGenerator):
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
            player_pos = player.get_pos()  # Get the player position here
            bullet_controller.add_bullet(self.bullet_type(deepcopy(position), (player_pos-position).normalize()))

            self.total_time += self.cooldown
