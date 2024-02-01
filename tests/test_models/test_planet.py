import pytest

from no_mans_ti.constants import PlanetTrait, PlanetValues, TechnologySpecialty
from no_mans_ti.models.planet import Planet


class TestExplicitPlanetCreation:
    def test_planet_values(self):
        planet = Planet(
            resources=1, influence=1, trait=PlanetTrait.CULTURAL, specialty=None
        )

        assert planet.values.resources == 1
        assert planet.values.influence == 1

    def test_planet_values_zero(self):
        planet = Planet(
            resources=0, influence=0, trait=PlanetTrait.CULTURAL, specialty=None
        )

        assert planet.values.resources == 0
        assert planet.values.influence == 0

    def test_no_planet_trait(self):
        with pytest.raises(AssertionError):
            Planet(resources=0, influence=0, trait=None, specialty=None)

    def test_planet_trait(self):
        planet = Planet(
            resources=0, influence=0, trait=PlanetTrait.CULTURAL, specialty=None
        )

        assert planet.trait == PlanetTrait.CULTURAL

    def test_no_planet_specialty(self):
        planet = Planet(
            resources=0, influence=0, trait=PlanetTrait.CULTURAL, specialty=None
        )

        assert planet.specialty is None

    def test_planet_specialty(self):
        planet = Planet(
            resources=0,
            influence=0,
            trait=PlanetTrait.CULTURAL,
            specialty=TechnologySpecialty.BLUE,
        )

        assert planet.specialty == TechnologySpecialty.BLUE


class TestOptimalSpend:
    def test_optimal_resources(self):
        planet = Planet(
            resources=1,
            influence=0,
            trait=PlanetTrait.CULTURAL,
            specialty=None,
        )

        assert planet.optimal_spend() == PlanetValues(1, 0)

    def test_optimal_influence(self):
        planet = Planet(
            resources=0,
            influence=1,
            trait=PlanetTrait.CULTURAL,
            specialty=None,
        )

        assert planet.optimal_spend() == PlanetValues(0, 1)

    def test_optimal_equal(self):
        planet = Planet(
            resources=1,
            influence=1,
            trait=PlanetTrait.CULTURAL,
            specialty=None,
        )

        assert planet.optimal_spend() == PlanetValues(0.5, 0.5)

    def test_optimal_zero_case(self):
        planet = Planet(
            resources=0,
            influence=0,
            trait=PlanetTrait.CULTURAL,
            specialty=None,
        )

        assert planet.optimal_spend() == PlanetValues(0, 0)
