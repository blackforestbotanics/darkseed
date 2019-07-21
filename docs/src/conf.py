"""
darkseed must be import safe due to importing with autodocs.

https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
"""

import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc']
