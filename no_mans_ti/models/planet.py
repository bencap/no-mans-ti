import random

from typing import Optional

from no_mans_ti.constants import (
    PlanetTrait,
    TechnologySpecialty,
    PlanetValues,
    BASE_RES_INF_DISTRIBUTION,
    ZERO_SEEDED_RES_INF_DISTRIBUTION,
    ONE_SEEDED_RES_INF_DISTRIBUTION,
    TWO_SEEDED_RES_INF_DISTRIBUTION,
    THREE_SEEDED_RES_INF_DISTRIBUTION,
    FOUR_SEEDED_RES_INF_DISTRIBUTION,
    FIVE_SEEDED_RES_INF_DISTRIBUTION,
    HAZARDOUS_SKEWED,
    CULTURAL_SKEWED,
    INDUSTRIAL_SKEWED,
    BASE_SPECIALTY_DISTRIBUTION,
)
from no_mans_ti.lib.planet_names import random_planet_name


# TODO: Support planet attachments
class Planet:
    values: PlanetValues
    trait: PlanetTrait
    specialty: TechnologySpecialty | None

    def __init__(
        self,
        resources: Optional[int] = None,
        influence: Optional[int] = None,
        trait: Optional[PlanetTrait] = None,
        specialty: Optional[TechnologySpecialty] = None,
    ) -> None:
        if resources is not None and influence is not None and trait is not None:
            self.values = PlanetValues(resources, influence)
            self.specialty = specialty
            self.trait = trait
        else:
            self.randomize_planet()

            if resources is not None:
                self.resources = resources

            if influence is not None:
                self.influence = influence

            if trait is not None:
                self.trait = trait

    def __str__(self):
        """String repr."""
        return f"\tResources: {self.values.resources}\n\tIfnluence: {self.values.influence}\n\tTrait: {self.trait}\n\tSpecialty: {self.specialty}"

    def randomize_planet(self):
        """
        Randomizes the resources, influence, trait, and technology
        specialty of this planet.
        """

        def randomize_planet_values():
            """
            Generate random resource and influence values based on a distribution
            of original values and a distribution of secondary values, which depend
            on the original value selected.
            """
            seed_value = random.choice(BASE_RES_INF_DISTRIBUTION)

            if seed_value == 0:
                variable_distribution = ZERO_SEEDED_RES_INF_DISTRIBUTION
            elif seed_value == 1:
                variable_distribution = ONE_SEEDED_RES_INF_DISTRIBUTION
            elif seed_value == 2:
                variable_distribution = TWO_SEEDED_RES_INF_DISTRIBUTION
            elif seed_value == 3:
                variable_distribution = THREE_SEEDED_RES_INF_DISTRIBUTION
            elif seed_value == 4:
                variable_distribution = FOUR_SEEDED_RES_INF_DISTRIBUTION
            elif seed_value == 5:
                variable_distribution = FIVE_SEEDED_RES_INF_DISTRIBUTION
            else:
                raise ValueError(
                    f"Selected planet value ({seed_value}) should not be greater than 5."
                )

            generated_value = random.choice(variable_distribution)

            # Randomly decide if the seed is the resource or influence value.
            if random.randint(0, 1):
                return seed_value, generated_value
            else:
                return generated_value, seed_value

        def randomize_planet_trait(resources: Optional[int], influence: Optional[int]) -> PlanetTrait:
            """
            Generate a random planet trait weighted based on the provided
            resource and influence values. Alternatively, return a random
            trait if no resources or influence values are provided.
            """
            if not resources or not influence:
                return random.choice([t for t in PlanetTrait])

            res_inf_diff = resources - influence
            if res_inf_diff > 1.5:
                trait_distribution = HAZARDOUS_SKEWED
            elif res_inf_diff < -1.5:
                trait_distribution = CULTURAL_SKEWED
            else:
                trait_distribution = INDUSTRIAL_SKEWED

            return random.choice(trait_distribution)

        def randomize_planet_specialty():
            """
            Generate a random planet specialty, or None.
            """
            return random.choice(BASE_SPECIALTY_DISTRIBUTION)

        resources, influence = randomize_planet_values()
        trait = randomize_planet_trait(resources, influence)
        specialty = randomize_planet_specialty()

        self.values = PlanetValues(resources, influence)
        self.trait = trait
        self.specialty = specialty

    def optimal_spend(self):
        """
        The optimal spend of this planet.
        """
        if self.values.resources > self.values.influence:
            return PlanetValues(self.values.resources, 0)
        elif self.values.influence > self.values.resources:
            return PlanetValues(0, self.values.influence)
        else:
            return PlanetValues(self.values.resources / 2, self.values.influence / 2)


if __name__ == "__main__":
    print(random_planet_name())
    print(Planet())
