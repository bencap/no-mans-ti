from no_mans_ti.constants import PlanetTrait, TechnologySpecialty, PlanetValues


class Planet:
    values: PlanetValues
    trait: PlanetTrait
    specialty: TechnologySpecialty

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

    def __init__(
        self,
        trait: PlanetTrait,
        specialty: TechnologySpecialty,
        resources: int = 0,
        influence: int = 0,
        values: PlanetValues | None = None,
    ) -> None:
        # if a values object is provided, prioritize that
        if values:
            self.values = values
        else:
            self.values = PlanetValues(resources=resources, influence=influence)

        self.trait = trait
        self.specialty = specialty
