__all__ = ["Player"]

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group as SpriteGroup
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.locals import K_w, K_s, K_a, K_d
import math
from copy import deepcopy

from src.playarea import PlayArea

from ..consts import WINDOW_WIDTH, WINDOW_HEIGHT
from .bullet_generators.player_bullet_generator import PlayerBulletGenerator
from .bullet_controllers.player_bullet_controller import PlayerBulletController


class Player(Sprite):
    __slots__ = ("position", "size", "speed", "sprite", "image", "bullet_generator", "bullet_controller", "move_vector")
    position: Vector2
    size: int
    speed: float
    sprite: str
    image: Surface
    bullet_generator: PlayerBulletGenerator
    bullet_controller: PlayerBulletController

    def __init__(self) -> None:
        Sprite.__init__(self)
        self.position = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.size = 20
        self.speed = 100
        self.move_vector = pygame.Vector2(0, 0)

        self.sprite = "sprites/Player.png"
        self.image = pygame.transform.scale(pygame.image.load(self.sprite), (int(self.size), int(self.size)))
        self.rect = self.image.get_rect()
        self.rect.center = (int(self.position.x), int(self.position.y))

        self.bullet_generator = PlayerBulletGenerator(0.5)
        self.bullet_controller = PlayerBulletController()

    def update(self, frame_time: float, play_area: PlayArea, enemy_group: SpriteGroup, **kwargs) -> None:
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

        self.position += self.move_vector * frame_time * self.speed

        # keep inside play area
        play_area_r = play_area.rect
        if self.position.x < play_area_r.x:
            self.position.x = play_area_r.x
        if self.position.x > play_area_r.x + play_area_r.width - self.size:
            self.position.x = play_area_r.x + play_area_r.width - self.size
        if self.position.y < play_area_r.y:
            self.position.y = play_area_r.y
        if self.position.y > play_area_r.y + play_area_r.height - self.size:
            self.position.y = play_area_r.y + play_area_r.height - self.size

        self.rect.center = (int(self.position.x), int(self.position.y))

        if pygame.mouse.get_pressed()[0] == 1:
            self.bullet_generator.update(frame_time, deepcopy(self.position), self.bullet_controller)
        else:
            self.bullet_generator.tick(frame_time)

        self.bullet_controller.update(frame_time, enemy_group, play_area)

    def draw(self, window: Surface) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(self.position.x - mouse_x, self.position.y - mouse_y))

        window.blit(pygame.transform.rotate(self.image, angle), (self.position.x, self.position.y))

    def get_pos(self) -> Vector2:
        return self.position

    def set_pos(self, x: int, y: int) -> None:
        self.position.x = x
        self.position.y = y
