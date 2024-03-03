from typing import Optional

from no_mans_ti.constants import PlanetTrait, Direction
from no_mans_ti.models.planet import Planet
from no_mans_ti.models.system import System

MECATOL_REX = System({Planet(0, 6, PlanetTrait.CULTURAL, None)})
MECATOL_REX_POSITION = 18
HOME_SYSTEM_POSITIONS = set((0, 6, 9, 27, 30, 36))

# Although this makes the code less buggy (since everything is preconfigured), it locks us into
# one map layout - standard 6 player. It would be cool to add some more configuration to make
# other map layouts possible.
BORDERS = {
    # Mecatol Rex
    18: {
        Direction.TOP: 11,
        Direction.TOP_LEFT: 14,
        Direction.TOP_RIGHT: 15,
        Direction.BOTTOM_LEFT: 21,
        Direction.BOTTOM_RIGHT: 22,
        Direction.BOTTOM: 23,
    },
    # Home Systems
    0: {
        Direction.BOTTOM_LEFT: 1,
        Direction.BOTTOM_RIGHT: 2,
        Direction.BOTTOM: 4,
    },
    6: {
        Direction.TOP_RIGHT: 3,
        Direction.BOTTOM_RIGHT: 10,
        Direction.BOTTOM: 13,
    },
    9: {
        Direction.TOP_LEFT: 5,
        Direction.BOTTOM_LEFT: 12,
        Direction.BOTTOM: 16,
    },
    27: {
        Direction.TOP: 20,
        Direction.TOP_RIGHT: 24,
        Direction.BOTTOM_RIGHT: 31,
    },
    30: {
        Direction.TOP: 23,
        Direction.TOP_LEFT: 26,
        Direction.BOTTOM_LEFT: 33,
    },
    36: {
        Direction.TOP: 32,
        Direction.TOP_LEFT: 34,
        Direction.TOP_RIGHT: 35,
    },
    # Non-home Systems
    1: {
        Direction.TOP_RIGHT: 0,
        Direction.BOTTOM_LEFT: 3,
        Direction.BOTTOM_RIGHT: 4,
        Direction.BOTTOM: 7,
    },
    2: {
        Direction.TOP_LEFT: 0,
        Direction.BOTTOM_LEFT: 4,
        Direction.BOTTOM_RIGHT: 5,
        Direction.BOTTOM: 8,
    },
    3: {
        Direction.TOP_RIGHT: 1,
        Direction.BOTTOM_LEFT: 6,
        Direction.BOTTOM_RIGHT: 7,
        Direction.BOTTOM: 10,
    },
    4: {
        Direction.TOP: 0,
        Direction.TOP_LEFT: 1,
        Direction.TOP_RIGHT: 2,
        Direction.BOTTOM_LEFT: 7,
        Direction.BOTTOM_RIGHT: 8,
        Direction.BOTTOM: 11,
    },
    5: {
        Direction.TOP_LEFT: 2,
        Direction.BOTTOM_LEFT: 8,
        Direction.BOTTOM_RIGHT: 9,
        Direction.BOTTOM: 12,
    },
    7: {
        Direction.TOP: 1,
        Direction.TOP_LEFT: 3,
        Direction.TOP_RIGHT: 4,
        Direction.BOTTOM_LEFT: 10,
        Direction.BOTTOM_RIGHT: 11,
        Direction.BOTTOM: 14,
    },
    8: {
        Direction.TOP: 2,
        Direction.TOP_LEFT: 4,
        Direction.TOP_RIGHT: 5,
        Direction.BOTTOM_LEFT: 11,
        Direction.BOTTOM_RIGHT: 12,
        Direction.BOTTOM: 15,
    },
    10: {
        Direction.TOP: 3,
        Direction.TOP_LEFT: 6,
        Direction.TOP_RIGHT: 7,
        Direction.BOTTOM_LEFT: 13,
        Direction.BOTTOM_RIGHT: 14,
        Direction.BOTTOM: 17,
    },
    11: {
        Direction.TOP: 4,
        Direction.TOP_LEFT: 7,
        Direction.TOP_RIGHT: 8,
        Direction.BOTTOM_LEFT: 14,
        Direction.BOTTOM_RIGHT: 15,
        Direction.BOTTOM: 18,
    },
    12: {
        Direction.TOP: 5,
        Direction.TOP_LEFT: 8,
        Direction.TOP_RIGHT: 9,
        Direction.BOTTOM_LEFT: 15,
        Direction.BOTTOM_RIGHT: 16,
        Direction.BOTTOM: 19,
    },
    13: {
        Direction.TOP: 6,
        Direction.TOP_RIGHT: 10,
        Direction.BOTTOM_RIGHT: 17,
        Direction.BOTTOM: 20,
    },
    14: {
        Direction.TOP: 7,
        Direction.TOP_LEFT: 10,
        Direction.TOP_RIGHT: 11,
        Direction.BOTTOM_LEFT: 17,
        Direction.BOTTOM_RIGHT: 18,
        Direction.BOTTOM: 21,
    },
    15: {
        Direction.TOP: 8,
        Direction.TOP_LEFT: 11,
        Direction.TOP_RIGHT: 12,
        Direction.BOTTOM_LEFT: 18,
        Direction.BOTTOM_RIGHT: 19,
        Direction.BOTTOM: 22,
    },
    16: {
        Direction.TOP: 9,
        Direction.TOP_LEFT: 12,
        Direction.BOTTOM_LEFT: 19,
        Direction.BOTTOM: 23,
    },
    17: {
        Direction.TOP: 10,
        Direction.TOP_LEFT: 13,
        Direction.TOP_RIGHT: 14,
        Direction.BOTTOM_LEFT: 20,
        Direction.BOTTOM_RIGHT: 21,
        Direction.BOTTOM: 24,
    },
    19: {
        Direction.TOP: 12,
        Direction.TOP_LEFT: 15,
        Direction.TOP_RIGHT: 16,
        Direction.BOTTOM_LEFT: 22,
        Direction.BOTTOM_RIGHT: 23,
        Direction.BOTTOM: 26,
    },
    20: {
        Direction.TOP: 13,
        Direction.TOP_RIGHT: 17,
        Direction.BOTTOM_RIGHT: 24,
        Direction.BOTTOM: 27,
    },
    21: {
        Direction.TOP: 14,
        Direction.TOP_LEFT: 17,
        Direction.TOP_RIGHT: 18,
        Direction.BOTTOM_LEFT: 24,
        Direction.BOTTOM_RIGHT: 25,
        Direction.BOTTOM: 28,
    },
    22: {
        Direction.TOP: 15,
        Direction.TOP_LEFT: 18,
        Direction.TOP_RIGHT: 19,
        Direction.BOTTOM_LEFT: 25,
        Direction.BOTTOM_RIGHT: 26,
        Direction.BOTTOM: 29,
    },
    23: {
        Direction.TOP: 16,
        Direction.TOP_LEFT: 19,
        Direction.BOTTOM_LEFT: 26,
        Direction.BOTTOM: 30,
    },
    24: {
        Direction.TOP: 17,
        Direction.TOP_LEFT: 20,
        Direction.TOP_RIGHT: 21,
        Direction.BOTTOM_LEFT: 27,
        Direction.BOTTOM_RIGHT: 28,
        Direction.BOTTOM: 31,
    },
    25: {
        Direction.TOP: 18,
        Direction.TOP_LEFT: 21,
        Direction.TOP_RIGHT: 22,
        Direction.BOTTOM_LEFT: 28,
        Direction.BOTTOM_RIGHT: 29,
        Direction.BOTTOM: 32,
    },
    26: {
        Direction.TOP: 19,
        Direction.TOP_LEFT: 22,
        Direction.TOP_RIGHT: 23,
        Direction.BOTTOM_LEFT: 29,
        Direction.BOTTOM_RIGHT: 30,
        Direction.BOTTOM: 33,
    },
    28: {
        Direction.TOP: 21,
        Direction.TOP_LEFT: 24,
        Direction.TOP_RIGHT: 25,
        Direction.BOTTOM_LEFT: 31,
        Direction.BOTTOM_RIGHT: 32,
        Direction.BOTTOM: 34,
    },
    29: {
        Direction.TOP: 22,
        Direction.TOP_LEFT: 25,
        Direction.TOP_RIGHT: 26,
        Direction.BOTTOM_LEFT: 32,
        Direction.BOTTOM_RIGHT: 33,
        Direction.BOTTOM: 35,
    },
    31: {
        Direction.TOP: 24,
        Direction.TOP_LEFT: 27,
        Direction.TOP_RIGHT: 28,
        Direction.BOTTOM_RIGHT: 34,
    },
    32: {
        Direction.TOP: 25,
        Direction.TOP_LEFT: 28,
        Direction.TOP_RIGHT: 29,
        Direction.BOTTOM_LEFT: 34,
        Direction.BOTTOM_RIGHT: 35,
        Direction.BOTTOM: 36,
    },
    33: {
        Direction.TOP: 26,
        Direction.TOP_LEFT: 29,
        Direction.TOP_RIGHT: 30,
        Direction.BOTTOM_LEFT: 35,
    },
    34: {
        Direction.TOP: 28,
        Direction.TOP_LEFT: 31,
        Direction.TOP_RIGHT: 32,
        Direction.BOTTOM_RIGHT: 36,
    },
    35: {
        Direction.TOP: 29,
        Direction.TOP_LEFT: 32,
        Direction.TOP_RIGHT: 33,
        Direction.BOTTOM_LEFT: 36,
    },
}

POSITIONS = BORDERS.keys()


class Galaxy:
    galaxy: dict[int, Optional[System]]

    def __init__(self, galaxy: Optional[dict[int, Optional[System]]] = None):
        self.galaxy = {}

        if galaxy is not None:
            # Ensure the provided galaxy is valid
            assert galaxy[MECATOL_REX_POSITION] == MECATOL_REX

            self.galaxy = galaxy
            return

        for position in POSITIONS:
            self.galaxy[position] = None

        self.galaxy[MECATOL_REX_POSITION] = MECATOL_REX

    def get(self, position: int) -> Optional[System]:
        if position not in POSITIONS:
            raise self.PositionInvalidException()

        return self.galaxy[position]

    def add(self, system: System, position: int, force: bool = False) -> System:
        existing_system = self.get(position)

        if existing_system and not force:
            raise ValueError(
                f"System already exists at galaxy position {position}. Use `force`."
            )

        # Resolve system borders prior to placing system
        for direction, neighboring_position in BORDERS[position].items():
            border_system = self.get(neighboring_position)

            if border_system:
                system.associate_system(border_system, direction)

        # place system in galaxy
        self.galaxy[position] = system
        return system

    class PositionInvalidException(KeyError):
        """Raised when the position provided is not a possible galaxy position."""
