from dataclasses import dataclass
from enum import Enum


## Planet area stuff


@dataclass
class PlanetValues:
    resources: int
    influence: int

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
    [PlanetTrait.HAZARDOUS.name] * 50
    + [PlanetTrait.INDUSTRIAL.name] * 25
    + [PlanetTrait.CULTURAL.name] * 25
)
INDUSTRIAL_SKEWED = (
    [PlanetTrait.HAZARDOUS.name] * 25
    + [PlanetTrait.INDUSTRIAL.name] * 50
    + [PlanetTrait.CULTURAL.name] * 25
)
CULTURAL_SKEWED = (
    [PlanetTrait.HAZARDOUS.name] * 25
    + [PlanetTrait.INDUSTRIAL.name] * 25
    + [PlanetTrait.CULTURAL.name] * 50
)

# Planet specialty distributions
BASE_SPECIALTY_DISTRIBUTION = (
    [None] * 75
    + [TechnologySpecialty.BLUE.name] * 6
    + [TechnologySpecialty.GREEN.name] * 6
    + [TechnologySpecialty.RED.name] * 6
    + [TechnologySpecialty.YELLOW.name] * 6
)

# Space object distribution
SPACE_OBJECT_DISTRIBUTION = [0] * 70 + [1] * 25 + [2] * 5

# Planet distribution
PLANET_COUNT_DISTRIBUTION = [0] * 10 + [1] * 24 + [2] * 50 + [3] * 15 + [4] * 1