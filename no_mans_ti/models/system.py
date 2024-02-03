import random

from typing import Optional

from no_mans_ti.lib.planet_names import random_planet_name
from no_mans_ti.models.planet import Planet
from no_mans_ti.models.space import Space
from no_mans_ti.constants import PlanetValues, PLANET_COUNT_DISTRIBUTION


class System:
    planets: set[Planet]
    space: Space

    def __init__(self, planets: Optional[set[Planet]] = None, space: Optional[Space] = None) -> None:
        # Generate an empty system by passing an empty set of planets.
        if planets is None and space is None:
            self.randomize_system()
        else:
            self.planets = planets
            self.space = space

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


if __name__ == "__main__":
    print(System())