__all__ = ["Bullet"]

from typing import Callable
from pygame import image, transform
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.sprite import Sprite


class Bullet(Sprite):
    __slots__ = ("position", "movement_vector", "movement_modifier", "size", "lifetime", "rect")
    position: Vector2
    movement_vector: Vector2
    movement_modifier: Callable | None
    size: int
    lifetime: float
    rect: Rect

    def __init__(
                 self,
                 start_position: Vector2,
                 movement_vector: Vector2,
                 movement_modifier: Callable | None = None
                ) -> None:
        Sprite.__init__(self)

        self.position = start_position
        self.movement_vector = movement_vector
        self.movement_modifier = movement_modifier
        self.lifetime = 0

        self.set_texture("sprites/EnemyBullet.png", start_position.x, start_position.y)

    def set_texture(self, texture: str, x_pos: float, y_pos: float) -> None:
        self.sprite = texture
        self.size = 20
        self.image = transform.scale(image.load(self.sprite), (int(self.size), int(self.size)))
        self.rect = self.image.get_rect()
        self.rect.center = (int(x_pos), int(y_pos))

    def update(self, frame_time: float, **kwargs) -> None:
        self.lifetime += frame_time
        self.position += self.movement_vector * frame_time * 100

        if self.movement_modifier:
            self.movement_vector = self.movement_modifier(self.movement_vector, frame_time, bullet_lifetime=self.lifetime)

        self.rect.center = (int(self.position.x), int(self.position.y))


class PlayerBullet(Bullet):
    def __init__(self, start_position: Vector2,
                 movement_vector: Vector2,
                 movement_modifier: Callable[[Vector2, float], Vector2] | None = None
                 ) -> None:
        super().__init__(start_position, movement_vector, movement_modifier)
        self.set_texture("sprites/PlayerBullet.png", start_position.x, start_position.y)
