__all__ = ["Map"]

from pygame.rect import Rect
from pygame.surface import Surface
from .entities.player import Player
from .entities.enemy_controller import EnemyController
from .entities.bullet_controller import BulletController


class Map:
    __slots__ = ("player", "enemy_controller", "bullet_controller", "play_area")

    player: Player
    enemy_controller: EnemyController
    bullet_controller: BulletController
    play_area: Rect

    def __init__(self) -> None:
        self.player = Player()
        self.enemy_controller = EnemyController()
        self.bullet_controller = BulletController()
        self.play_area = Rect(0, 0, 1600, 900)

    def update(self, frame_time: float, **kwargs) -> None:
        self.player.update()

        self.enemy_controller.update(frame_time, map_constraints=self.play_area, player=self.player, bullet_controller=self.bullet_controller, **kwargs)
        self.bullet_controller.update(frame_time)

    def draw(self, window: Surface) -> None:
        self.player.draw(window)
        self.enemy_controller.draw(window)
        self.bullet_controller.draw(window)