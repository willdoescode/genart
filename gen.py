from PIL import Image, ImageDraw
import random
from typing import List, Tuple
from enum import Enum


def random_hex() -> str:
    def h(): return random.randint(0, 255)
    return '#%02X%02X%02X' % (h(), h(), h())


def random_hexs(amount: int) -> List[str]:
    return [random_hex() for _ in range(amount)]


def random_color_range() -> List[str]:
    return random_hexs(random.randint(1, 20))


class DrawType(Enum):
    ELLIPSE = 0


class Shape:
    x: int
    y: int
    color: str
    line_width: int

    def __init__(self, x: int, y: int, color: str, line_width: int = 1) -> None:
        (self.x, self.y, self.color, self.line_width) = (x, y, color, line_width)

    def draw(self, image_draw: ImageDraw, xy: Tuple[Tuple[int, int], Tuple[int, int]], draw_type: DrawType = DrawType.ELLIPSE) -> None:
        if draw_type == DrawType.ELLIPSE:
            image_draw.ellipse(
                xy=xy,
                outline=self.color,
                width=self.line_width
            )


class Circle(Shape):
    radius: float

    def __init__(self, x: int, y: int, color: str, radius: float, line_width: int = 1) -> None:
        super().__init__(x, y, color, line_width=line_width)
        self.radius = radius

    def draw(self, image_draw: ImageDraw) -> None:
        return super().draw(image_draw=image_draw, xy=(
            (self.x - self.radius, self.y - self.radius),
            (self.x + self.radius, self.y + self.radius)
        ), draw_type=DrawType.ELLIPSE)


def main() -> None:
    image = Image.new('RGBA', (1200, 1200), random_hex())
    image_draw = ImageDraw.Draw(im=image)
    circle = Circle(
        x=1200/2,
        y=1200/2,
        radius=random.randint(0, 1200),
        color=random_hex(),
        line_width=10,
    )
    circle.draw(image_draw=image_draw)
    image.save(f'img_{random.randint(0, 100000000000000000)}.png')
    image.show()


if __name__ == '__main__':
    main()
