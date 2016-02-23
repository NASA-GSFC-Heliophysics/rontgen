from __future__ import absolute_import

from rontgen.material import *
import os
import json


_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, 'data'))

with open(os.path.join(_data_directory, 'elements.json')) as data_file:
    elements_list = json.load(data_file)

with open(os.path.join(_data_directory, 'compounds_mixtures.json')) as data_file:
    compounds_mixtures_list = json.load(data_file)

material_list = elements_list.copy()
material_list.update(compounds_mixtures_list)
