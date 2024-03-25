import os
from pathlib import Path

# Define the project root as the parent directory of the current file.
# This assumes that the current file (__init__.py) is in the
# top-level directory of the project.

PROJECT_ROOT = (
    Path(os.path.dirname(os.path.realpath(__file__))).parent.resolve().as_posix()
)
