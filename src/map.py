__all__ = ["Map"]

from pygame.surface import Surface

from .consts import DEFAULT_SCREEN_MULTIPLIER
from .entities.player import Player
from .entities.enemy_controller import EnemyController
from .entities.bullet_controllers.enemy_bullet_controller import EnemyBulletController
from .colour import Colour

from .playarea import PlayArea


class Map:
    __slots__ = ("player", "enemy_controller", "bullet_controller", "play_area")

    player: Player
    enemy_controller: EnemyController
    bullet_controller: EnemyBulletController
    play_area: PlayArea

    def __init__(self) -> None:
        self.player = Player()
        self.enemy_controller = EnemyController()
        self.bullet_controller = EnemyBulletController()

        self.play_area = PlayArea(1550, 850, DEFAULT_SCREEN_MULTIPLIER)

    def update(self, frame_time: float, **kwargs) -> None:
        self.play_area.update(frame_time)
        self.enemy_controller.cull_enemies_outside_bounds(self.play_area.rect)

        self.player.update(frame_time, self.play_area, self.enemy_controller.enemy_group)

        self.enemy_controller.update(
            frame_time,
            play_area=self.play_area.rect,
            player=self.player,
            bullet_controller=self.bullet_controller,
            **kwargs
        )

        self.bullet_controller.update(frame_time, player=self.player, play_area=self.play_area, **kwargs)

    def draw(self, window: Surface) -> None:
        window.fill(Colour.White, self.play_area.rect)

        self.player.draw(window)
        self.player.bullet_controller.draw(window)
        self.enemy_controller.draw(window)
        self.bullet_controller.draw(window)

    def has_player_died(self) -> bool:
        return 0 in (self.play_area.rect.w, self.play_area.rect.h)
