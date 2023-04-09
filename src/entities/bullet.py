__all__ = ["Bullet"]

from typing import Callable
from pygame import image, transform
from pygame.math import Vector2
from pygame.sprite import Sprite


class Bullet(Sprite):
    __slots__ = ("position", "movement_vector", "movement_modifier", "size")
    position: Vector2
    movement_vector: Vector2
    movement_modifier: Callable[[Vector2, float], Vector2] | None
    size: int

    def __init__(
                 self,
                 start_position: Vector2,
                 movement_vector: Vector2,
                 movement_modifier: Callable[[Vector2, float], Vector2] | None = None
                ) -> None:
        Sprite.__init__(self)
        self.sprite = "sprites/Bullet.png"
        self.size = 20
        self.image = transform.scale(image.load(self.sprite), (int(self.size), int(self.size)))

        self.rect = self.image.get_rect()
        self.rect.center = (int(start_position.x), int(start_position.y))

        self.position = start_position
        self.movement_vector = movement_vector
        self.movement_modifier = movement_modifier

    def update(self, frame_time: float, **kwargs) -> None:
        self.position += self.movement_vector * frame_time * 100

        if self.movement_modifier:
            self.movement_vector = self.movement_modifier(self.movement_vector, frame_time)

        self.rect.center = (int(self.position.x), int(self.position.y))
