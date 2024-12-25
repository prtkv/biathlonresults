"""
Python API wrapper for biathlonresults.com
"""

from . import consts
from .api import (
    all_results,
    analytic_results,
    athletes,
    cisbios,
    competitions,
    cup_results,
    cups,
    events,
    organizers,
    results,
    seasons,
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
    "analytic_results",
    "seasons",
    "organizers",
    "consts",
]

__author__ = "Ilya Porotikov"
__email__ = "ip.tspl@gmail.com"
__licence__ = "MIT"
__version__ = "0.1"
