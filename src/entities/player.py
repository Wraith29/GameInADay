__all__ = ["Player"]

import pygame
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.locals import *
import math
from ..consts import WINDOW_WIDTH, WINDOW_HEIGHT


class Player:
    __slots__ = ("pos", "size", "speed", "sprite")
    pos: Vector2
    size: int
    speed: float
    sprite: Surface

    def __init__(self) -> None:
        self.pos = Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.size = 20
        self.speed = 0.5
        self.sprite = pygame.transform.scale(pygame.image.load("sprites/Player.png"), (int(self.size), int(self.size)))
        
    def move_up(self) -> None:
        self.pos.y -= self.speed

    def move_down(self) -> None:
        self.pos.y += self.speed

    def move_left(self) -> None:
        self.pos.x -= self.speed

    def move_right(self) -> None:
        self.pos.x += self.speed
        
    def shoot(self) -> None:
        # bullet generator stuff
        pass
    
    def update(self) -> None:
        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            self.move_up()
        if pressed[K_s]:
            self.move_down()
        if pressed[K_a]:
            self.move_left()
        if pressed[K_d]:
            self.move_right()
        
    def draw(self, window: Surface) -> None:
        # pygame.mouse.get_pos()[0]
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(self.pos.x - mouse_x, self.pos.y - mouse_y))
        
        window.blit(pygame.transform.rotate(self.sprite, angle), (self.pos.x, self.pos.y))

    def get_pos(self) -> Vector2:
        return self.pos
    
    def set_pos(self, x: int, y: int) -> None:
        self.pos.x = x
        self.pos.y = y