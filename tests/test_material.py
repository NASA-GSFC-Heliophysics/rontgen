import pytest
from rontgen import Mass_attenuation_coefficient
import rontgen
import numpy as np
import astropy.units as u

@pytest.fixture(params=rontgen.material_list.keys())
def mass_atten(request):
    return Mass_attenuation_coefficient(request.param)


def test_returns_quantity(mass_atten):
    assert type(mass_atten.func(1 * u.keV)) == type(7927 * u.cm)


def test_number_of_energies(mass_atten):
    energy = u.Quantity(np.arange(1, 1000), 'keV')
    atten = mass_atten.func(energy)
    assert len(energy) == len(atten)
