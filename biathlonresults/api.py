import os
import re
from typing import Any, Optional, Union
from urllib.parse import urljoin

import requests

from .consts import AnalysisType, LevelType

SITE_URL = "https://biathlonresults.com/"
ROOT_API = SITE_URL + "modules/sportapi/api/"
TIMEOUT = 30

# Sent with every request, as by the biathlonresults.com frontend in Chrome
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36"
    ),
    "sec-ch-ua": (
        '"Not-A.Brand";v="99", "Google Chrome";v="157", "Chromium";v="157"'
    ),
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "Referer": SITE_URL,
}

# The sport API answers data requests with an empty 401 unless they carry an
# "apikey" header. The key is public: the biathlonresults.com frontend ships it
# in its app bundle (window.ApiKey) and sends it with every request. It is read
# from there on the first request and again whenever the API rejects it;
# $BIATHLONRESULTS_API_KEY, if set, is used until then.
API_KEY_ENV = "BIATHLONRESULTS_API_KEY"
_api_key = os.environ.get(API_KEY_ENV)

_SCRIPT_SRC = re.compile(r"""<script[^>]*\ssrc=["']?([^"'\s>]+\.js)""", re.I)
_API_KEY = re.compile(r"""ApiKey\s*=\s*["']([0-9a-fA-F-]{36})["']""")

ApiResponse = Union[dict[str, Any], list]


def _get(method: str, params: Optional[dict[str, str]]) -> requests.Response:
    headers = {**HEADERS, "apikey": _api_key} if _api_key else HEADERS
    return requests.get(ROOT_API + method, params=params, headers=headers)


def _request(method: str, params: Optional[dict[str, str]] = None) -> ApiResponse:
    global _api_key
    try:
        if _api_key is None:
            _api_key = fetch_api_key()
        response = _get(method, params)
        if response.status_code == 401:  # the site changed its key
            _api_key = fetch_api_key()
            response = _get(method, params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong", e)
        raise


def fetch_api_key() -> Optional[str]:
    """
    The API key the biathlonresults.com frontend currently sends: it is
    assigned to window.ApiKey in one of the scripts of the start page.
    None if the site no longer has it there.
    """
    page = requests.get(SITE_URL, headers=HEADERS, timeout=TIMEOUT)
    page.raise_for_status()
    scripts = [urljoin(SITE_URL, src) for src in _SCRIPT_SRC.findall(page.text)]
    # the key lives in the app bundles, check them before the vendor ones
    scripts.sort(key=lambda url: "app" not in url.rsplit("/", 1)[-1])
    for url in scripts:
        script = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if script.ok:
            match = _API_KEY.search(script.text)
            if match:
                return match.group(1)
    return None


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
