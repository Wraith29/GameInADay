__all__ = ["Enemy"]

from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame import image
from pygame.math import Vector2
from pygame import transform
from .bullet_generators.bullet_generator import BulletGenerator
from .bullet_generators.simple_bullet_generator import SimpleBulletGenerator
# from .bullet_generators.spiral_bullet_generator import SpiralBulletGenerator


class Enemy(Sprite):
    __slots__ = ("position", "bullet_generator", "sprite", "image", "size")

    position: Vector2
    bullet_generator: BulletGenerator
    sprite: str
    image: Surface
    size: int

    def __init__(self, start_pos: Vector2, bullet_generator: type = SimpleBulletGenerator) -> None:
        Sprite.__init__(self)

        self.position = start_pos
        self.bullet_generator = bullet_generator()

        self.sprite = "sprites/Enemy.png"
        self.size = 20
        self.image = transform.scale(image.load(self.sprite), (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.center = (int(self.position.x), int(self.position.y))

    def update(self, frame_time: float, **kwargs) -> None:
        self.bullet_generator.update(frame_time, position=self.position, **kwargs)
