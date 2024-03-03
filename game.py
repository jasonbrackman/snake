import datetime
import random
import time
from dataclasses import dataclass, field
from typing import ClassVar

from display import Display, ColourEnum
from snack import Snack
from snake import Snake
from snaketypes import Vec2


@dataclass
class Game:
    size: Vec2
    snake: Snake = field(init=False)
    snack: Snack = field(init=False)
    display: Display = field(init=False)
    counter: int = 0

    table: ClassVar[dict[str, tuple[int, int]]] = {
        'a': (0, -1),
        's': (1, 0),
        'd': (0, 1),
        'w': (-1, 0),
    }

    def __post_init__(self):
        self.snake = Snake(2, [(self.size[0]//2, self.size[1]//2)])
        self.snack = Snack((5, 5), 0)
        self.display = Display()

    def draw(self):
        tt = datetime.datetime.utcfromtimestamp(round(self.counter))

        for y in range(0, self.size[0] + 1):
            for x in range(self.size[1] + 1):
                if (y, x) == self.snack.head:
                    self.display.addch(y, x, 'X', ColourEnum.RED)
                elif 0 in (y, x) or self.size[0] == y or self.size[1] == x:
                    self.display.addch(y, x, "#", ColourEnum.WHITE)
                else:
                    if (y, x) in self.snake.body:
                        if self.snake.body[-1] == (y, x):  # head
                            self.display.addch(y, x, "*", ColourEnum.GREEN)
                        else:
                            self.display.addch(y, x, "+", ColourEnum.YELLOW)
                    else:
                        self.display.addch(y, x, " ", ColourEnum.BLACK)
        # self.display.screen.addstr(2, 17, tt.strftime("%H:%M:%S"))
        # self.display.screen.addstr(self.size[0]-3, 17, f"SCORE: {self.snack.count}")
        # self.display.screen.addch(self.size[0], self.size[1], "#", ColourEnum.WHITE)

    def move(self, dir: tuple[int, int]) -> None:

        self.snake.move(dir)

        if self.snack.head in self.snake.body:
            while self.snack.head in self.snake.body:
                self.snack.head = (
                    random.randint(1, self.size[0] -1),
                    random.randint(1, self.size[1] - 1)
                )
                self.snack.count += 1
            self.snake.grow()

    def run(self) -> None:
        playing = True
        last_dir = (0, 1)

        while playing:
            time.sleep(self.snake.speed)
            try:
                key = self.display.screen.getkey()
            except:
                key = ''
            if key in ('a', 's', 'd', 'w'):
                last_dir = self.table[key]
            elif key == 'q':
                playing = False

            self.move(last_dir)
            self.draw()
            self.counter += self.snake.speed