__all__ = ["Map"]

from pygame.rect import Rect
from pygame.surface import Surface
from .entities.player import Player
from .entities.enemy_controller import EnemyController
from .entities.bullet_controllers.enemy_bullet_controller import EnemyBulletController
from .colour import Colour

from .playarea import PlayArea


class Map:
    __slots__ = ("player", "enemy_controller", "bullet_controller", "play_area", "current_play_area")

    player: Player
    enemy_controller: EnemyController
    bullet_controller: EnemyBulletController
    play_area: PlayArea
    current_play_area: Rect

    def __init__(self) -> None:
        self.player = Player()
        self.enemy_controller = EnemyController()
        self.bullet_controller = EnemyBulletController()

        self.play_area = PlayArea(900, 600, 3.0)
        self.current_play_area = self.play_area.play_area

    def update(self, frame_time: float, **kwargs) -> None:
        play_area = self.play_area.update(frame_time, self.current_play_area)
        self.current_play_area = play_area

        self.player.update(frame_time, play_area)

        self.enemy_controller.update(
            frame_time,
            play_area=play_area,
            player=self.player,
            bullet_controller=self.bullet_controller,
            **kwargs
        )

        self.bullet_controller.update(frame_time, player=self.player, play_area=self.play_area, **kwargs)

    def draw(self, window: Surface) -> None:
        window.fill(Colour.White, self.current_play_area)

        self.player.draw(window)
        self.player.bullet_controller.draw(window)
        self.enemy_controller.draw(window)
        self.bullet_controller.draw(window)

    def has_player_died(self) -> bool:

        if self.current_play_area.w == 0 or self.current_play_area.h == 0:
            return True
        else:
            return False
