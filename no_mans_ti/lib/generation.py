import random

from no_mans_ti.constants import PlanetTrait, TechnologySpecialty, Anomalies, Wormholes
from no_mans_ti.models.planet import Planet
from no_mans_ti.models.space import Space
from no_mans_ti.models.system import System


def generate_planet():
    resources = random.randint(0, 4)
    influence = random.randint(0, 4)
    trait = random.choice(PlanetTrait._member_names_)
    specialty = random.choice(TechnologySpecialty._member_names_)

    return Planet(
        resources=resources, influence=influence, trait=trait, specialty=specialty
    )


def generate_space():
    anomalies = set()
    wormholes = set()

    for i in range(random.randint(0, 2)):
        anomalies.add(random.choice(Anomalies._member_names_))

    for i in range(random.randint(0, 2)):
        wormholes.add(random.choice(Wormholes._member_names_))

    return Space(wormholes=wormholes, anomalies=anomalies)


def generate_system():
    planets = set()
    space = generate_space()

    for i in range(random.randint(0, 3)):
        planets.add(generate_planet())

    return System(planets=planets, space=space)


def generate_universe():
    pass


def generate_slices():
    pass
