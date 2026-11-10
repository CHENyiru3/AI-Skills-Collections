"""Shared validation for the market's MAJOR.MINOR.PATCH version strings."""

import re

VERSION_PATTERN = r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"


def valid_version(value: object) -> bool:
    """Accept a quoted three-component release version without leading zeros."""
    return isinstance(value, str) and re.fullmatch(VERSION_PATTERN, value) is not None
