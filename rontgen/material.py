"""
"""

from __future__ import absolute_import

import numpy as np

import os

import astropy.units as u
from scipy import interpolate
import rontgen

__all__ = ['Material', 'Mass_attenuation_coefficient']

_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, '..', 'data'))
#_filename = 'mass_attenuation_coefficient.hdf5'
#_data_file = os.path.join(_data_directory, _filename)


class Material(object):
    """An object which provides the properties of a material in x-rays

    Parameters
    ----------
    material : str
        A string representing a material (e.g. cdte, be, mylar, si)
    thickness : `astropy.units.Quantity`
        The thickness of the material in the optical path.

    Examples
    --------
    >>> from rontgen.material import Material
    >>> import astropy.units as u
    >>> detector = Material('cdte', 500 * u.um)
    >>> thermal_blankets = Material('mylar', 0.5 * u.mm)
    """

    def __init__(self, material, thickness):
        self.name = material
        self.long_name = _get_long_name(material)
        self.thickness = thickness
        self.mass_attenuation_coefficient = Mass_attenuation_coefficient(material)
        self.density = self.mass_attenuation_coefficient.density

    def __repr__(self):
        """Returns a human-readable representation."""
        return '<Material ' + str(self.name) + ' (' + str(self.long_name) + ') ' + str(self.thickness) + ' ' + str(self.density) + '>'

    def transmission(self, energy):
        """Provide the transmission fraction (0 to 1).

        Parameters
        ----------
        energy : `astropy.units.Quantity`
            An array of energies in keV
        """
        energy_kev = energy.to('keV').value
        coefficients = self.mass_attenuation_coefficient.func(energy_kev) * u.cm ** 2 / u.gram
        transmission = np.exp(- coefficients * self.density * self.thickness)
        return transmission

    def absorption(self, energy):
        """Provides the absorption fraction (0 to 1).

        Parameters
        ----------
        energy : `astropy.units.Quantity`
            An array of energies in keV.
        """
        return 1 - self.transmission(energy)


class Mass_attenuation_coefficient(object):
    """

    """
    def __init__(self, material):
        self.name = material
        datafile_path = os.path.join(_data_directory, rontgen.material_list[material]['file'])
        self.data = np.loadtxt(datafile_path, delimiter=',')
        self.density = u.Quantity(rontgen.material_list[material]['density']['value'], rontgen.material_list[material]['density']['unit'])

        data_energy_kev = np.log10(self.data[0,:] * 1000)
        data_attenuation_coeff = np.log10(self.data[1,:])
        self._f = interpolate.interp1d(data_energy_kev, data_attenuation_coeff, bounds_error=False, fill_value=0.0)
        self.func = lambda x: 10 ** self._f(np.log10(x))

def _get_long_name(material):
    return rontgen.material_list.get(material)['name']
