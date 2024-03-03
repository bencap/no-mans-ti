import pytest

from no_mans_ti.models.galaxy import (
    Galaxy,
    BORDERS,
    POSITIONS,
    MECATOL_REX,
    MECATOL_REX_POSITION,
)
from no_mans_ti.models.system import System


class TestGalaxy:

    # XXX Use a pre-populated test galaxy as a fixture here
    def test_galaxy_get(self):
        galaxy = Galaxy()

        for position in POSITIONS:
            assert galaxy.get(position) == galaxy.galaxy[position]

    def test_galaxy_get_invalid_position(self):
        galaxy = Galaxy()
        with pytest.raises(Galaxy.PositionInvalidException):
            galaxy.get(-1)

    # XXX Use a pre-populated test galaxy as a fixture here
    def test_mecatol_position_galaxy(self):
        galaxy = Galaxy()
        assert galaxy.get(MECATOL_REX_POSITION) == MECATOL_REX

    def test_add_planet(self):
        galaxy = Galaxy()
        system = System()

        galaxy.add(system, 5)
        assert galaxy.get(5) == system

    def test_add_planet_with_force(self):
        galaxy = Galaxy()
        system1 = System()
        system2 = System()

        galaxy.add(system1, 5, force=True)
        galaxy.add(system2, 5, force=True)

        assert galaxy.get(5) == system2

    def test_add_planet_invalid_position(self):
        galaxy = Galaxy()
        system = System()

        with pytest.raises(Galaxy.PositionInvalidException):
            galaxy.add(system, -1)

    def test_add_planet_without_force(self):
        galaxy = Galaxy()
        system = System()

        with pytest.raises(ValueError):
            galaxy.add(system, 1, force=False)
            galaxy.add(system, 1, force=False)

    # XXX Use a pre-populated test galaxy as a fixture here
    @pytest.mark.parametrize("position", range(36))
    def test_add(self, position):
        galaxy = Galaxy()

        system = System()
        system = galaxy.add(system, position, force=True)

        for direction, neighboring_position in BORDERS[position].items():
            neighboring_system = galaxy.get(neighboring_position)
            assert system.neighbors[direction] == neighboring_system

            ## XXX: Any pre-populated test galaxy should be full
            if neighboring_system:
                assert neighboring_system.neighbors[direction.mirror()] == system
