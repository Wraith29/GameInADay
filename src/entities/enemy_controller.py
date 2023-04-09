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

    def spawn_enemy(self, map_constraints: Rect) -> None:
        pos_x = randint(map_constraints.x, map_constraints.x + map_constraints.width)
        pos_y = randint(map_constraints.y, map_constraints.y + map_constraints.height)

        self.enemy_group.add(Enemy(Vector2(pos_x, pos_y)))

    def update(self, frame_time: float, map_constraints: Rect, **kwargs) -> None:
        self.spawn_timer += frame_time

        if self.spawn_timer < ENEMY_SPAWN_TIMER:
            return
    
        self.spawn_timer -= ENEMY_SPAWN_TIMER

        self.spawn_enemy(map_constraints)

        self.enemy_group.update(frame_time, **kwargs)

    def draw(self, window: Surface) -> None:
        self.enemy_group.draw(window)
