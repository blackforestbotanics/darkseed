"""
all of darkseed must be import safe. autodoc runs on all members.

Top-level objects and functions are offered here for using Darkseed as a
library.
"""

from .utils import release

def get_path():
    """get the theme path"""

    import os

    return os.path.dirname(__file__)
