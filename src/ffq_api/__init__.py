"""
ffq-api is an API to retrieve metadata about biological data from various sources.
"""

from pathlib import Path

with open(Path(__file__).parent / "VERSION", "r") as fh:
    __version__ = fh.read()
