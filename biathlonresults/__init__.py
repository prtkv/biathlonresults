"""
Python API wrapper for biathlonresults.com
"""
from .api import (
    cups,
    cup_results,
    athletes,
    cisbios,
    all_results,
    events,
    competitions,
    results,
    stats,
)

__all__ = [
    "cups",
    "cup_results",
    "athletes",
    "cisbios",
    "all_results",
    "events",
    "competitions",
    "results",
    "stats",
]

__author__ = "Ilya Porotikov"
__email__ = "ip.tspl@gmail.com"
__licence__ = "MIT"
__version__ = "0.1b1"
