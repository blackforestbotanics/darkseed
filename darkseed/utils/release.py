"""utils for the release process."""

import sys
from darkseed.version import __version__

def update_version(version_file, version_str):
    """update the version file."""

    version_doc = f'__version__ = "{version_str}"\n'

    with open(version_file, 'w') as f:
        f.write(version_doc)

def commit_version():
    """commit all pending changes."""

def tag():
    """
    tag the commit.

    this kicks of CI. if all passes, then this is released on PyPi.
    """

def version_error():
    """print that invalid semver was supplied and exit with error code 1."""

    print('must supply version argument like "0.0.10".')
    print('exiting...')
    sys.exit(1)

def update_version_and_tag_for_release():
    """full process. utilized by root release script."""

    print(f'current version is {__version__}')

    if len(sys.argv) > 1:
        new_version = sys.argv[1]
    else:
        try:
            new_version = input(
                '''what do you want the new version to be?
enter new version: '''
            )
        except (KeyboardInterrupt, EOFError):
            print('\nexiting...')
            sys.exit(0)

    if new_version == "" or new_version.count(".") != 2 or len(new_version) < 5:
        version_error()

    update_version('darkseed/version.py', new_version)

    print(f'version updated to {new_version}.')
