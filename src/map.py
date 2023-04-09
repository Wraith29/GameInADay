__all__ = ["Map"]

from pygame.rect import Rect
from pygame.surface import Surface
from .entities.player import Player
from .entities.enemy_controller import EnemyController
from .entities.bullet_controller import BulletController
from .colour import Colour
from typing import Dict


class Map:
    __slots__ = ("player", "enemy_controller", "bullet_controller", "play_area", "multiplier", "play_area_size")

    player: Player
    enemy_controller: EnemyController
    bullet_controller: BulletController
    play_area: Rect
    multiplier: float
    play_area_size: Dict[str, float]

    def __init__(self) -> None:
        self.player = Player()
        self.enemy_controller = EnemyController()
        self.bullet_controller = BulletController()

        self.play_area_size = {
            "width": 1600,
            "height": 900
        }

        self.play_area = Rect(0, 0, self.play_area_size["width"], self.play_area_size["height"])
        self.play_area.center = (800, 450)
        self.multiplier = 1.0

    def update(self, frame_time: float, **kwargs) -> None:
        temp_multiplier = (frame_time * self.multiplier * 10)

        self.play_area_size["width"] -= temp_multiplier * (16/25) * 1.5
        self.play_area_size["height"] -= temp_multiplier * (9/25) * 1.5

        self.play_area = Rect(
            round((1600 - self.play_area_size["width"]) / 2),
            round((900 - self.play_area_size["height"]) / 2),
            self.play_area_size["width"],
            self.play_area_size["height"]
        )

        self.player.update(frame_time, play_area=self.play_area)

        self.enemy_controller.update(
            frame_time,
            play_area=self.play_area,
            player=self.player,
            bullet_controller=self.bullet_controller,
            **kwargs
        )

        self.bullet_controller.update(frame_time, player_sprite=self.player.sprite, **kwargs)

    def draw(self, window: Surface) -> None:
        window.fill(Colour.White, self.play_area)

        self.player.draw(window)
        self.enemy_controller.draw(window)
        self.bullet_controller.draw(window)

    def has_player_died(self) -> bool:

        if self.play_area.w == 0 or self.play_area.h == 0:
            return True
        else:
            return False
