from enum import Enum


class PlayerType(Enum):
    goalkeeper = 1
    regular = 2


class Player:
    def __init__(self, name, player_type: PlayerType):
        self.name = name
        self.type = player_type

    def is_goalkeeper(self):
        return self.type == PlayerType.goalkeeper

