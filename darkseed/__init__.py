"""
all of darkseed must be import safe. autodoc runs on all members.
"""

def get_path():
    """get the theme path"""

    import os

    return os.path.dirname(__file__)
