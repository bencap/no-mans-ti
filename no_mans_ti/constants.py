from dataclasses import dataclass
from enum import Enum
from typing import Union


## Planet area stuff


@dataclass
class PlanetValues:
    resources: Union[int, float]
    influence: Union[int, float]

    # Prevent accidental modification of planet values by default
    frozen = True


class PlanetTrait(Enum):
    CULTURAL = 1
    INDUSTRIAL = 2
    HAZARDOUS = 3


class TechnologySpecialty(Enum):
    BLUE = 1
    RED = 2
    GREEN = 3
    YELLOW = 4


## Space area stuff


class Anomalies(Enum):
    ASTEROID_FIELD = 1
    GRAVITY_RIFT = 2
    NEBULA = 3
    SUPERNOVA = 4


class Wormholes(Enum):
    ALPHA = 1
    BETA = 2
    DELTA = 3
    GAMMA = 4


## System Stuff


class Direction(Enum):
    TOP = 1
    TOP_RIGHT = 2
    BOTTOM_RIGHT = 3
    BOTTOM = 4
    BOTTOM_LEFT = 5
    TOP_LEFT = 6

    def mirror(self):
        if self.name == Direction.BOTTOM.name:
            return Direction.TOP
        elif self.name == Direction.TOP.name:
            return Direction.BOTTOM
        elif self.name == Direction.TOP_RIGHT.name:
            return Direction.BOTTOM_LEFT
        elif self.name == Direction.BOTTOM_LEFT.name:
            return self.TOP_RIGHT
        elif self.name == Direction.TOP_LEFT.name:
            return self.BOTTOM_RIGHT
        elif self.name == Direction.BOTTOM_RIGHT.name:
            return Direction.TOP_LEFT

        raise ValueError(f"No direction ?? `{self.name}`")


## Generation distributions and rates

# Planet resource/influence distributions
BASE_RES_INF_DISTRIBUTION = (
    [0] * 10 + [1] * 20 + [2] * 30 + [3] * 25 + [4] * 10 + [5] * 5
)

ZERO_SEEDED_RES_INF_DISTRIBUTION = (
    [0] * 0 + [1] * 5 + [2] * 20 + [3] * 25 + [4] * 30 + [5] * 20
)

ONE_SEEDED_RES_INF_DISTRIBUTION = (
    [0] * 5 + [1] * 10 + [2] * 25 + [3] * 35 + [4] * 25 + [5] * 0
)

TWO_SEEDED_RES_INF_DISTRIBUTION = (
    [0] * 10 + [1] * 20 + [2] * 30 + [3] * 40 + [4] * 0 + [5] * 0
)

THREE_SEEDED_RES_INF_DISTRIBUTION = (
    [0] * 25 + [1] * 50 + [2] * 25 + [3] * 0 + [4] * 0 + [5] * 0
)

FOUR_SEEDED_RES_INF_DISTRIBUTION = (
    [0] * 50 + [1] * 50 + [2] * 25 + [3] * 35 + [4] * 25 + [5] * 0
)

FIVE_SEEDED_RES_INF_DISTRIBUTION = (
    [0] * 100 + [1] * 0 + [2] * 0 + [3] * 0 + [4] * 0 + [5] * 0
)

# Planet trait distributions
HAZARDOUS_SKEWED = (
    [PlanetTrait.HAZARDOUS] * 50
    + [PlanetTrait.INDUSTRIAL] * 25
    + [PlanetTrait.CULTURAL] * 25
)
INDUSTRIAL_SKEWED = (
    [PlanetTrait.HAZARDOUS] * 25
    + [PlanetTrait.INDUSTRIAL] * 50
    + [PlanetTrait.CULTURAL] * 25
)
CULTURAL_SKEWED = (
    [PlanetTrait.HAZARDOUS] * 25
    + [PlanetTrait.INDUSTRIAL] * 25
    + [PlanetTrait.CULTURAL] * 50
)

# Planet specialty distributions
BASE_SPECIALTY_DISTRIBUTION = (
    [None] * 75
    + [TechnologySpecialty.BLUE] * 6
    + [TechnologySpecialty.GREEN] * 6
    + [TechnologySpecialty.RED] * 6
    + [TechnologySpecialty.YELLOW] * 6
)

# Space object distribution
SPACE_OBJECT_DISTRIBUTION = [0] * 70 + [1] * 25 + [2] * 5

# Planet distribution
PLANET_COUNT_DISTRIBUTION = [0] * 10 + [1] * 24 + [2] * 50 + [3] * 15 + [4] * 1

# Galaxy borders
# TODO Although this makes the code less buggy (since everything is preconfigured), it locks us into
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