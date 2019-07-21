from darkseed.version import __version__

def test_version():
    """
    stupid test for release version.

    it gets overwritten when executing ./release.py.
    """

    assert len(__version__) >= 5
    assert __version__.count('.') == 2
