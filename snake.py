from dataclasses import dataclass, field

from snaketypes import Vec2


@dataclass
class Snake:
    size: int
    body: list[Vec2]
    speed: float = field(default=0.225)

    def grow(self):
        self.size += 1
        self.speed = max(self.speed - 0.01, 0.05)

    def move(self, vec: Vec2) -> None:
        self.body.append((self.body[-1][0] + vec[0], self.body[-1][1] + vec[1]))
        self.body = self.body[-self.size:]
