from typing import Any, Optional, Union

import requests

from .consts import AnalysisType, LevelType

ROOT_API = "http://biathlonresults.com/modules/sportapi/api/"

ApiResponse = Union[dict[str, Any], list]


def _request(method: str, params: Optional[dict[str, str]] = None) -> ApiResponse:
    try:
        return requests.get(ROOT_API + method, params=params).json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong", e)
        raise


def organizers() -> ApiResponse:
    return _request("Organizers")


def seasons() -> ApiResponse:
    return _request("Seasons")


def events(season_id: str, level: Union[LevelType, str] = LevelType.ALL) -> ApiResponse:
    """
    Events of cup (schedule)
    """
    if isinstance(level, LevelType):
        level = str(level.value)
    return _request("Events", {"SeasonId": season_id, "Level": level})


def competitions(event_id: str) -> ApiResponse:
    """
    List of races in stage
    """
    return _request("Competitions", {"EventId": event_id})


def cups(season_id: str) -> ApiResponse:
    """
    List of Cups
    season_id: season identifier (1819 for season 2018/2019, get others in a similar way)
    """
    return _request("Cups", {"SeasonId": season_id})


def cup_results(cup_id: str) -> ApiResponse:
    """
    Cup results
    BT1819SWRLCP__SMTS - Men's WC Total 2018/2019
    BT1819SWRLCP__SWTS - Women's WC Total 2018/2019
    """
    return _request("CupResults", {"CupId": cup_id})


def athletes(family_name: str = "", given_name: str = "") -> ApiResponse:
    """
    Search athlete
    """
    return _request("Athletes", {"FamilyName": family_name, "GivenName": given_name})


def cisbios(ibu_id: str) -> ApiResponse:
    """
    Get athlete by id
    """
    return _request("CISBios", {"IBUId": ibu_id})


def all_results(ibu_id: str) -> ApiResponse:
    """
    All races results of the athlete
    """
    return _request("AllResults", {"IBUId": ibu_id})


def results(race_id: str) -> ApiResponse:
    """
    Race results
    """
    return _request("Results", {"RaceId": race_id})


def analytic_results(race_id: str, type_id: Union[AnalysisType, str]) -> ApiResponse:
    if isinstance(type_id, AnalysisType):
        type_id = type_id.value
    return _request("AnalyticResults", {"RaceId": race_id, "TypeId": type_id})


def stats(
    statistic_id: str,
    stat_id: str,
    by_what: str,
    gender_id: str,
    season_id: str = "",
    organizer_id: str = "",
    ibu_id: str = "",
    nat: str = "",
) -> ApiResponse:
    """
    Statistics
    Not sure how to use it right, here's default query parameters:
    StatisticId=WCPOD_M&StatId=WCPOD&byWhat=ATH&SeasonId=&OrganizerId=&GenderId=M&IBUId=&Nat=
    """
    return _request(
        "Stats",
        {
            "StatisticId": statistic_id,
            "StatId": stat_id,
            "byWhat": by_what,
            "SeasonId": season_id,
            "OrganizerId": organizer_id,
            "GenderId": gender_id,
            "IBUId": ibu_id,
            "Nat": nat,
        },
    )
