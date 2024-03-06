from typing import Optional
import random

from no_mans_ti.constants import PlanetTrait, BORDERS
from no_mans_ti.models.planet import Planet
from no_mans_ti.models.system import System

MECATOL_REX = System({Planet(0, 6, PlanetTrait.CULTURAL, None)})
MECATOL_REX_POSITION = 18
HOME_SYSTEM_POSITIONS = set((0, 6, 9, 27, 30, 36))

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

    def remove(self, position: int) -> Optional[System]:
        system_to_be_removed = self.get(position)

        if system_to_be_removed is None:
            return None

        for neighboring_direction in system_to_be_removed.neighbors.keys():
            system_to_be_removed.unassociate_system(neighboring_direction)

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

    def randomize_galaxy(self):
        randomized_positions = list(BORDERS.keys())

        for position in random.sample(randomized_positions, len(randomized_positions)):
            # XXX elegance
            if position == MECATOL_REX_POSITION:
                continue

            self.add(System(), position)

        return self

    class PositionInvalidException(KeyError):
        """Raised when the position provided is not a possible galaxy position."""


if __name__ == "__main__":
    galaxy = Galaxy()
    galaxy.randomize_galaxy()

    for idx, system in galaxy.galaxy.items():
        print(f"--------------- Position {idx} ---------------")
        print(system)
        print()
