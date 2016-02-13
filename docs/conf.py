# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
    'h5py': ('http://docs.h5py.org/en/latest/', None)
    }

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    'matplotlib.sphinxext.mathmpl'
]

if on_rtd:
    extensions.append('sphinx.ext.mathjax')
else:
    extensions.append('sphinx.ext.pngmath')

try:
    import matplotlib.sphinxext.plot_directive
    extensions += [matplotlib.sphinxext.plot_directive.__name__]

# AttributeError is checked here in case matplotlib is installed but
# Sphinx isn't.  Note that this module is imported by the config file
# generator, even if we're not building the docs.

except (ImportError, AttributeError):
    warnings.warn(
        "matplotlib's plot_directive could not be imported. " +
        "Inline plots will not be included in the output")


if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = 'Rontgen'
year = '2016'
author = 'Steven D Christe'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.1.0'

git_url_root = "https://github.com/NASA-GSFC-Heliophysics/rontgen/"

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': (git_url_root + 'issues/%s', '#'),
    'pr': (git_url_root + 'pulls/%s', 'PR #'),
}
import sphinx_py3doc_enhanced_theme
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': git_url_root
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

import rontgen
for mat in rontgen.material_list:
    print(mat)
