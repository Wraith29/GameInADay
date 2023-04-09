from src.log import error
import pygame


def main() -> int:
    _, num_errors = pygame.init()

    if num_errors != 0:
        error("Failed To Initialise Pygame")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
