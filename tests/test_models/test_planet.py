import pytest

from no_mans_ti.constants import PlanetTrait, PlanetValues, TechnologySpecialty
from no_mans_ti.models.planet import Planet


class TestPlanet:
    def test_optimal_resources(self):
        planet = Planet(
            resources=1,
            influence=0,
            trait=PlanetTrait.CULTURAL,
            specialty=TechnologySpecialty.NONE,
        )

        assert planet.optimal_spend() == PlanetValues(1, 0)

    def test_optimal_influence(self):
        planet = Planet(
            resources=0,
            influence=1,
            trait=PlanetTrait.CULTURAL,
            specialty=TechnologySpecialty.NONE,
        )

        assert planet.optimal_spend() == PlanetValues(0, 1)

    def test_optimal_equal(self):
        planet = Planet(
            resources=1,
            influence=1,
            trait=PlanetTrait.CULTURAL,
            specialty=TechnologySpecialty.NONE,
        )

        assert planet.optimal_spend() == PlanetValues(0.5, 0.5)

    def test_optimal_zero_case(self):
        planet = Planet(
            resources=0,
            influence=0,
            trait=PlanetTrait.CULTURAL,
            specialty=TechnologySpecialty.NONE,
        )

        assert planet.optimal_spend() == PlanetValues(0, 0)

    def test_full_values_object(self):
        planet = Planet(
            values=PlanetValues(1, 1),
            trait=PlanetTrait.CULTURAL,
            specialty=TechnologySpecialty.NONE,
        )
        
        assert planet.values == PlanetValues(1, 1)
