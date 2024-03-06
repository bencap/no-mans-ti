import random

from typing import Optional

from no_mans_ti.lib.planet_names import random_planet_name
from no_mans_ti.models.planet import Planet
from no_mans_ti.models.space import Space
from no_mans_ti.constants import Direction, PlanetValues, PLANET_COUNT_DISTRIBUTION


class System:
    planets: set[Planet]
    space: Space

    neighbors: dict[Direction, Optional["System"]]

    def __init__(
        self, planets: Optional[set[Planet]] = None, space: Optional[Space] = None
    ) -> None:
        # Generate an empty system by passing an empty set of planets.
        if planets and space:
            self.planets = planets
            self.space = space
        else:
            self.randomize_system()

            if planets is not None:
                self.planets = planets

            if space is not None:
                self.space = space

        self.neighbors = {direction: None for direction in Direction}

    def __str__(self):
        """String repr."""
        output = "Planets:\n"

        for planet in self.planets:
            output += random_planet_name()
            output += "\n"
            output += planet.__str__()
            output += "\n"

        output += f"--------------\nSpace:\n{self.space.__str__()}\n"
        output += f"--------------\nGross spend: {self.gross_spend()}\nOptimal spend: {self.optimal_spend()}"

        return output
    
    def __compact_str__(self):
        """Compact string repr."""
        str_size = 26

        # XXX: Ugly!
        def buffer(input):
            str_len = len(input)
            buf_len = str_size - str_len
            front = buf_len // 2
            end = buf_len // 2
            return (" " * front) + input + (" " * end)
        
        planet_repr = [planet.__compact_str__() for planet in self.planets]
        
        # XXX: So ugly!!
        if len(planet_repr) == 1:
            system_str = f"{buffer(planet_repr[0])}\n"
        elif len(planet_repr) == 2:
            system_str = f"{buffer(planet_repr[0] + ", " + planet_repr[1])}\n"
        elif len(planet_repr) == 3:
            system_str = f"{buffer(planet_repr[0] + ", " + planet_repr[1])}\n{buffer(planet_repr[2])}"
        elif len(planet_repr) == 4:
            system_str = f"{buffer(planet_repr[0] + ", " + planet_repr[1])}\n{buffer(planet_repr[2] + ", " + planet_repr[3])}"
        else:
            system_str = f"{buffer("--\n")}"

        system_str += f"\n\n{buffer(self.space.__compact_str__())}"
        return system_str

    def randomize_system(self):
        """
        Randomizes the planets and space area within a system.
        """
        self.planets = set()

        planet_distribution = PLANET_COUNT_DISTRIBUTION
        num_planets = random.choice(planet_distribution)

        for i in range(num_planets):
            self.planets.add(Planet())

        self.space = Space()

    def gross_spend(self):
        """
        Gross spend of the planets within this system.
        """
        spend = PlanetValues(0, 0)
        spend.frozen = False

        for planet in self.planets:
            spend.resources += planet.values.resources
            spend.influence += planet.values.influence

        spend.frozen = True
        return spend

    def optimal_spend(self):
        """
        Optimal spend of the planets within this system.
        """
        spend = PlanetValues(0, 0)
        spend.frozen = False

        for planet in self.planets:
            spend.resources += planet.optimal_spend().resources
            spend.influence += planet.optimal_spend().influence

        spend.frozen = True
        return spend

    def associate_system(self, system: "System", direction: Direction):
        """
        Associate a system with a neighbor.
        """
        # Reset any prior associations if necessary
        prior_association = self.neighbors[direction]
        if prior_association is not None:
            prior_association.neighbors[direction.mirror()] = None
            self.neighbors[direction] = None

        self.neighbors[direction] = system
        system.neighbors[direction.mirror()] = self

    def unassociate_system(self, direction: Direction):
        """
        Un-associate a system with a neighbor.
        """
        # Reset any prior associations if necessary
        prior_association = self.neighbors[direction]
        if prior_association is not None:
            prior_association.neighbors[direction.mirror()] = None
            self.neighbors[direction] = None


if __name__ == "__main__":
    s = System()
    print(s)
    print()
    print(s.__compact_str__())
