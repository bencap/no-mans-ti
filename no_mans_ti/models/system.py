from no_mans_ti.models.planet import Planet
from no_mans_ti.models.space import Space


class System:
    planets: set[Planet]
    space: Space

    def __init__(self, planets: set[Planet], space: Space) -> None:
        self.planets = planets
        self.space = space
