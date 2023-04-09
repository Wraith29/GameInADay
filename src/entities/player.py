__all__ = ["Player"]

import pygame
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.locals import K_w, K_s, K_a, K_d
from pygame.rect import Rect
import math
from copy import deepcopy
from ..consts import WINDOW_WIDTH, WINDOW_HEIGHT
from .bullet_generators.bullet_generator import BulletGenerator
from .bullet_generators.player_bullet_generator import PlayerBulletGenerator
from .bullet_controller import BulletController


class Player:
    __slots__ = ("pos", "size", "speed", "sprite", "bullet_generator", "bullet_controller", "move_vector")
    pos: Vector2
    size: int
    speed: float
    sprite: Surface
    bullet_generator: BulletGenerator
    bullet_controller: BulletController

    def __init__(self) -> None:
        self.pos = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.size = 20
        self.speed = 100
        self.move_vector = pygame.Vector2(0, 0)

        self.sprite = pygame.transform.scale(pygame.image.load("sprites/Player.png"), (int(self.size), int(self.size)))
        self.bullet_generator = PlayerBulletGenerator(1)
        self.bullet_controller = BulletController()

    def update(self, frame_time: float, play_area: Rect, **kwargs) -> None:
        # user input
        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            self.move_vector.y = -1
        elif pressed[K_s]:
            self.move_vector.y = 1
        else:
            self.move_vector.y = 0
        if pressed[K_a]:
            self.move_vector.x = -1
        elif pressed[K_d]:
            self.move_vector.x = 1
        else:
            self.move_vector.x = 0

        self.pos += self.move_vector * frame_time * self.speed

        if pygame.mouse.get_pressed()[0] == 1:
            self.bullet_generator.update(frame_time, deepcopy(self.pos), self.bullet_controller)

        self.bullet_controller.update(frame_time)

        # keep inside play area
        if self.pos.x < play_area.x:
            self.pos.x = play_area.x
        if self.pos.x > play_area.x + play_area.width - self.size:
            self.pos.x = play_area.x + play_area.width - self.size
        if self.pos.y < play_area.y:
            self.pos.y = play_area.y
        if self.pos.y > play_area.y + play_area.height - self.size:
            self.pos.y = play_area.y + play_area.height - self.size

    def draw(self, window: Surface) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(self.pos.x - mouse_x, self.pos.y - mouse_y))

        window.blit(pygame.transform.rotate(self.sprite, angle), (self.pos.x, self.pos.y))

    def get_pos(self) -> Vector2:
        return self.pos

    def set_pos(self, x: int, y: int) -> None:
        self.pos.x = x
        self.pos.y = y
