__all__ = ["Colour"]


class Colour:
    White: tuple[int, int, int] = (255, 255, 255)
    Black: tuple[int, int, int] = (0, 0, 0)
    Pink: tuple[int, int, int] = (255, 174, 201)

    @staticmethod
    def darken(toDarken: tuple[int, int, int], delta: int = 40) -> tuple[int, int, int]:
        return (toDarken[0]-delta, toDarken[1]-delta, toDarken[2]-delta)
    
    @staticmethod
    def lighten(toDarken: tuple[int, int, int], delta: int = 40) -> tuple[int, int, int]:
        return (toDarken[0]+delta, toDarken[1]+delta, toDarken[2]+delta)