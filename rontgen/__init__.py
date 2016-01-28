from __future__ import absolute_import

from rontgen.material import *
import os
import h5py

_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, '..', 'data'))
_filename = 'mass_attenuation_coefficient.hdf5'
_data_file = os.path.join(_data_directory, _filename)

def _get_material():
    """Returns all the of the materials currently available"""
    h = h5py.File(_data_file, 'r')
    material_list = h.keys()
    h.close()
    return material_list

material_list = _get_material()
