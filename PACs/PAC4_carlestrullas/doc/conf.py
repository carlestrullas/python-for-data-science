"""
Sphinx configuration file for PAC4 - Student Performance in Catalonia.

This file sets up the Sphinx documentation builder, including extensions,
paths, and theme options.
"""

import os
import sys

# -- Project information -----------------------------------------------------

PROJECT = "PAC4 - Student Performance in Catalonia"
AUTHOR = "Carles Trullàs"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

TEMPLATES_PATH = []
EXCLUDE_PATTERNS = []

# Napoleon settings to support Google/NumPy style docstrings
NAPOLEON_GOOGLE_DOCSTRING = True
NAPOLEON_NUMPY_DOCSTRING = True
NAPOLEON_INCLUDE_PRIVATE_WITH_DOC = False
NAPOLEON_USE_PARAM = True
NAPOLEON_USE_RTYPE = True

# Ensure project root is on the path so `src` package is importable
sys.path.insert(0, os.path.abspath(".."))

# -- Options for HTML output -------------------------------------------------

HTML_THEME = "alabaster"
HTML_STATIC_PATH = []
