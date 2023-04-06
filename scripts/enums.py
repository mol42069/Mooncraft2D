from enum import Enum

class SheetPos(Enum):
    Empty = (0, 0)

class Dir(Enum):
    SideScroll = 2
    Dim3 = 3

class MovementDirections(Enum):
    none = 4
    forwards = 1
    left = 2
    right = 3
    backwards = 0

class WBLayout(Enum):
    inventory = 0
    directory = 1

class Block(Enum):
    dirt = 'single_dirt.png'
    grass = 'single_grass.png'
    stone = 'single_stone.png'

    air = 999