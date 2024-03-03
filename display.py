import curses
from enum import Enum


class ColourEnum(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
    WHITE = 4
    BLACK = 5


class Display:
    def __init__(self) -> None:
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()

        self.screen.keypad(True)
        self.screen.nodelay(True)
        if curses.has_colors():
            # Start color mode
            curses.start_color()
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLACK)

    def addch(self, y: int, x: int, s: str, c: ColourEnum = ColourEnum.WHITE) -> None:
        """Display a single character to the screen."""
        self.screen.addch(y, x, s, c.value)

    def __del__(self):
        # close with this
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
