__all__ = ["EnemyController"]

from random import randint
from pygame.math import Vector2
from pygame.sprite import Group as SpriteGroup
from pygame.rect import Rect
from pygame.surface import Surface
from .enemy import Enemy
from ..consts import ENEMY_SPAWN_TIMER


class EnemyController:
    __slots__ = ("enemy_group", "spawn_timer")
    enemy_group: SpriteGroup
    spawn_timer: float

    def __init__(self) -> None:
        self.enemy_group = SpriteGroup()
        self.spawn_timer = 0

    def spawn_enemy(self, play_area: Rect) -> None:
        pos_x = randint(play_area.x, play_area.x + play_area.width)
        pos_y = randint(play_area.y, play_area.y + play_area.height)

        self.enemy_group.add(Enemy(Vector2(pos_x, pos_y)))

    def update(self, frame_time: float, play_area: Rect, **kwargs) -> None:
        self.enemy_group.update(frame_time, **kwargs)

        self.spawn_timer += frame_time

        if self.spawn_timer > ENEMY_SPAWN_TIMER:
            self.spawn_enemy(play_area)
            self.spawn_timer -= ENEMY_SPAWN_TIMER

    def draw(self, window: Surface) -> None:
        self.enemy_group.draw(window)
