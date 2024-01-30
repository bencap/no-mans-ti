from dataclasses import dataclass
from enum import Enum


## Planet area stuff

@dataclass
class PlanetValues:
    resources: int
    influence: int


class PlanetTrait(Enum):
    CULTURAL = 1
    INDUSTRIAL = 2
    HAZARDOUS = 3


class TechnologySpecialty(Enum):
    NONE = 0
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
    ION = 5
