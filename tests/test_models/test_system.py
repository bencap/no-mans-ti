import pytest
import random

from no_mans_ti.constants import PlanetTrait, Direction
from no_mans_ti.models.planet import Planet
from no_mans_ti.models.system import System

RANDOM_RESOURCES = RANDOM_INFLUENCE = random.randint(1, 3)

LARGER_RESOURCES = random.randint(RANDOM_INFLUENCE + 1, 5)
LARGER_INFLUENCE = random.randint(RANDOM_RESOURCES + 1, 5)


class TestSystemSpend:
    def test_gross_spend_empty(self):
        system = System(planets=set())
        assert system.gross_spend().resources == 0
        assert system.gross_spend().influence == 0

    def test_gross_spend_zeroes(self):
        system = System(
            planets=set(
                (Planet(resources=0, influence=0, trait=PlanetTrait.CULTURAL),)
            )
        )
        assert system.gross_spend().resources == 0
        assert system.gross_spend().influence == 0

    def test_gross_spend_zeroes_multiple_planets(self):
        system = System(
            planets=set(
                (
                    Planet(resources=0, influence=0, trait=PlanetTrait.CULTURAL),
                    Planet(resources=0, influence=0, trait=PlanetTrait.INDUSTRIAL),
                    Planet(resources=0, influence=0, trait=PlanetTrait.HAZARDOUS),
                )
            )
        )
        assert system.gross_spend().resources == 0
        assert system.gross_spend().influence == 0

    def test_gross_spend_single_planet_r(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=1,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.gross_spend().resources == RANDOM_RESOURCES
        assert system.gross_spend().influence == 1

    def test_gross_spend_single_planet_i(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=1,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.gross_spend().resources == 1
        assert system.gross_spend().influence == RANDOM_INFLUENCE

    def test_gross_spend_single_planet_e(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=RANDOM_RESOURCES,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.gross_spend().resources == RANDOM_RESOURCES
        assert system.gross_spend().influence == RANDOM_INFLUENCE

    def test_gross_spend_multiple_planets(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=1,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=1,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.gross_spend().influence == 1 + (2 * RANDOM_INFLUENCE)
        assert system.gross_spend().resources == 1 + (2 * RANDOM_RESOURCES)

    def test_optimal_spend_empty(self):
        system = System(planets=set())
        assert system.optimal_spend().resources == 0
        assert system.optimal_spend().influence == 0

    def test_optimal_spend_zeroes(self):
        system = System(
            planets=set(
                (Planet(resources=0, influence=0, trait=PlanetTrait.CULTURAL),)
            )
        )
        assert system.optimal_spend().resources == 0
        assert system.optimal_spend().influence == 0

    def test_optimal_spend_zeroes_multiple_planets(self):
        system = System(
            planets=set(
                (
                    Planet(resources=0, influence=0, trait=PlanetTrait.CULTURAL),
                    Planet(resources=0, influence=0, trait=PlanetTrait.INDUSTRIAL),
                    Planet(resources=0, influence=0, trait=PlanetTrait.HAZARDOUS),
                )
            )
        )
        assert system.optimal_spend().resources == 0
        assert system.optimal_spend().influence == 0

    def test_optimal_spend_single_planet_r(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=LARGER_RESOURCES,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.optimal_spend().resources == LARGER_RESOURCES
        assert system.optimal_spend().influence == 0

    def test_optimal_spend_single_planet_i(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=LARGER_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.optimal_spend().resources == 0
        assert system.optimal_spend().influence == LARGER_INFLUENCE

    def test_optimal_spend_single_planet_e(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert system.optimal_spend().resources == RANDOM_RESOURCES / 2
        assert system.optimal_spend().influence == RANDOM_INFLUENCE / 2

    def test_optimal_spend_multiple_planets(self):
        system = System(
            planets=set(
                (
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=LARGER_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                    Planet(
                        resources=RANDOM_RESOURCES,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                    Planet(
                        resources=LARGER_RESOURCES,
                        influence=RANDOM_INFLUENCE,
                        trait=PlanetTrait.CULTURAL,
                    ),
                )
            )
        )
        assert (
            system.optimal_spend().influence
            == LARGER_INFLUENCE + 0 + RANDOM_INFLUENCE / 2
        )
        assert (
            system.optimal_spend().resources
            == LARGER_RESOURCES + 0 + RANDOM_RESOURCES / 2
        )


class TestSystemAdjacency:
    def test_adjacency_initialization(self):
        system = System()

        assert all(
            [dir in Direction._member_map_.values() for dir in system.neighbors.keys()]
        )
        assert all(
            [adjacent_system is None for adjacent_system in system.neighbors.values()]
        )

    @pytest.mark.parametrize("direction", Direction._member_map_.values())
    def test_adjacency(self, direction: Direction):
        reference = System()
        neighbor = System()

        reference.associate_system(neighbor, direction)

        assert reference.neighbors[direction] == neighbor
        assert neighbor.neighbors[direction.mirror()] == reference
