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


class TestRandomPlanetCreation:
    generated_planets: list[Planet] = []
    resource_counts = [0, 0, 0, 0, 0, 0]
    influence_counts = [0, 0, 0, 0, 0, 0]
    trait_counts = {
        PlanetTrait.CULTURAL.name: 0,
        PlanetTrait.HAZARDOUS.name: 0,
        PlanetTrait.INDUSTRIAL.name: 0,
    }
    specialty_counts = {
        None: 0,
        TechnologySpecialty.BLUE.name: 0,
        TechnologySpecialty.GREEN.name: 0,
        TechnologySpecialty.RED.name: 0,
        TechnologySpecialty.YELLOW.name: 0,
    }

    @pytest.fixture(scope="class", autouse=True)
    def _setup_randomized_planets(self):
        for i in range(100000):
            planet = Planet()

            self.resource_counts[planet.values.resources] += 1
            self.influence_counts[planet.values.influence] += 1

            self.trait_counts[planet.trait] += 1
            self.specialty_counts[planet.specialty] += 1

            self.generated_planets.append(Planet)

    # TODO
    def test_resource_distribution(self):
        pass

    # TODO
    def test_influence_distribution(self):
        pass

    # TODO
    def test_trait_distribution(self):
        pass

    def test_specialty_distribution(self):
        # Assert that the percentage of non-tech specialty planets is ~75%.
        # If this is the case, the percentage of the tech-specialty planets
        # must be ~25%.
        assert self.specialty_counts[None] / sum(self.specialty_counts.values()) < 0.77
        assert self.specialty_counts[None] / sum(self.specialty_counts.values()) > 0.73
        
        # Assert that each tech skip appears ~6% of the time
        assert self.specialty_counts[TechnologySpecialty.BLUE.name] / sum(self.specialty_counts.values()) < 0.07
        assert self.specialty_counts[TechnologySpecialty.BLUE.name] / sum(self.specialty_counts.values()) > 0.05
        assert self.specialty_counts[TechnologySpecialty.GREEN.name] / sum(self.specialty_counts.values()) < 0.07
        assert self.specialty_counts[TechnologySpecialty.GREEN.name] / sum(self.specialty_counts.values()) > 0.05
        assert self.specialty_counts[TechnologySpecialty.YELLOW.name] / sum(self.specialty_counts.values()) < 0.07
        assert self.specialty_counts[TechnologySpecialty.YELLOW.name] / sum(self.specialty_counts.values()) > 0.05
        assert self.specialty_counts[TechnologySpecialty.RED.name] / sum(self.specialty_counts.values()) < 0.07
        assert self.specialty_counts[TechnologySpecialty.RED.name] / sum(self.specialty_counts.values()) > 0.05


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
