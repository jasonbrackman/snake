from dataclasses import dataclass, field

from snaketypes import Vec2


@dataclass
class Snack:
    head: Vec2
    count:int = field(default=0)