import random

from typing import Optional

from no_mans_ti.constants import PlanetTrait, TechnologySpecialty, PlanetValues


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
        if resources is None and influence is None:
            self.randomize_planet()

        else:
            self.values = PlanetValues(resources, influence)
            self.specialty = specialty

            assert trait, "Planet trait should not be `None`"
            self.trait = trait

    def randomize_planet(self):
        """
        Randomizes the resources, influence, trait, and technology
        specialty of this planet.
        """

        def randomize_planet_values(self):
            """
            Generate random resource and influence values based on a distribution
            of original values and a distribution of secondary values, which depend
            on the original value selected.
            """
            value_distribution = (
                [0] * 10 + [1] * 20 + [2] * 30 + [3] * 25 + [4] * 10 + [5] * 5
            )
            seed_value = random.choice(value_distribution)

            if seed_value == 0:
                variable_distribution = (
                    [0] * 0 + [1] * 5 + [2] * 20 + [3] * 25 + [4] * 30 + [5] * 20
                )
            elif seed_value == 1:
                variable_distribution = (
                    [0] * 5 + [1] * 10 + [2] * 25 + [3] * 35 + [4] * 25 + [5] * 0
                )
            elif seed_value == 2:
                variable_distribution = (
                    [0] * 10 + [1] * 20 + [2] * 30 + [3] * 40 + [4] * 0 + [5] * 0
                )
            elif seed_value == 3:
                variable_distribution = (
                    [0] * 25 + [1] * 50 + [2] * 25 + [3] * 0 + [4] * 0 + [5] * 0
                )
            elif seed_value == 4:
                variable_distribution = (
                    [0] * 50 + [1] * 50 + [2] * 25 + [3] * 35 + [4] * 25 + [5] * 0
                )
            elif seed_value == 5:
                variable_distribution = (
                    [0] * 100 + [1] * 0 + [2] * 0 + [3] * 0 + [4] * 0 + [5] * 0
                )
            else:
                raise ValueError(
                    f"Selected planet value ({seed_value}) should not be greater than 5."
                )

            generated_value = random.choice(variable_distribution)

            if random.randint(0, 1):
                return seed_value, generated_value
            else:
                return generated_value, seed_value

        def randomize_planet_trait(
            self, resources: Optional[int], influence: Optional[int]
        ):
            """
            Generate a random planet trait weighted based on the provided
            resource and influence values. Alternatively, return a random
            trait if no resources or influence values are provided.
            """
            if not resources or not influence:
                return random.choice(PlanetTrait._member_names_)

            res_inf_diff = resources - influence
            if res_inf_diff > 1.5:
                trait_distribution = (
                    [PlanetTrait.HAZARDOUS] * 50
                    + [PlanetTrait.INDUSTRIAL] * 25
                    + [PlanetTrait.CULTURAL] * 25
                )
            elif res_inf_diff < -1.5:
                trait_distribution = (
                    [PlanetTrait.HAZARDOUS] * 25
                    + [PlanetTrait.INDUSTRIAL] * 25
                    + [PlanetTrait.CULTURAL] * 50
                )
            else:
                trait_distribution = (
                    [PlanetTrait.HAZARDOUS] * 25
                    + [PlanetTrait.INDUSTRIAL] * 50
                    + [PlanetTrait.CULTURAL] * 25
                )

            return random.choice(trait_distribution)

        def randomize_planet_specialty(self, no_specialty=0.75):
            """
            Generate a random planet specialty, or None, based on
            the provided likelihood no specialty will be generated.
            """
            if random.random() < 0.75:
                return None

            return random.choice(
                [
                    TechnologySpecialty.BLUE,
                    TechnologySpecialty.GREEN,
                    TechnologySpecialty.RED,
                    TechnologySpecialty.YELLOW,
                ]
            )

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
