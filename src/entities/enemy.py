__all__ = ["Enemy"]

from pygame import image, transform
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.rect import Rect
from .bullet_generators.bullet_generator import BulletGenerator
from .bullet_generators.simple_bullet_generator import SimpleBulletGenerator
from .bullets.exploding_bullet import ExplodingBullet

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
        self.bullet_generator = bullet_generator(0.75, bullet_type=ExplodingBullet)

        self.sprite = "sprites/Enemy.png"
        self.size = 20
        self.image = transform.scale(image.load(self.sprite), (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.center = (int(self.position.x), int(self.position.y))

    def update(self, frame_time: float, **kwargs) -> None:
        self.bullet_generator.update(frame_time, position=self.position, **kwargs)

    def get_pos(self) -> Rect:
        return self.rect
