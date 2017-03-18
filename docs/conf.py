import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import netsgiro  # noqa


# -- General configuration ------------------------------------------------

# needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'netsgiro'
copyright = '2017, Otovo AS'
author = 'Otovo AS'

release = netsgiro.__version__
version = '.'.join(release.split('.')[:2])

language = None
exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'alabaster'
# html_theme_options = {}
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'netsgiro'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    # 'pointsize': '10pt',
    # 'preamble': '',
    # 'figure_align': 'htbp',
}

latex_documents = [
    (
        master_doc,
        'netsgiro.tex',
        'netsgiro documentation',
        'Otovo AS',
        'manual',
    ),
]
