# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FRC Players Handbook'
copyright = 'Pre-2024 Season'
author = 'Wile E. Coyote'

release = '1.0'
version = '2024.12.29'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

html_theme_options = {
    'css_files': [
        'https://cyber-coyotes-handbook.readthedocs.io/en/latest/_static/css/custom.css',
    ],
}

html_css_files = [
    'https://cyber-coyotes-handbook.readthedocs.io/en/latest/_static/css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'