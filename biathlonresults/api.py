# -*- coding: utf-8 -*-
import requests

ROOT_API = 'http://biathlonresults.com/modules/sportapi/api/'


def _request(method, params):
    try:
        return requests.get(ROOT_API + method, params=params).json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong", e)


def cups(season_id):
    """
    List of Cups
    :param season_id: season identifier (1819 for season 2018/2019, get others in a similar way)
    :return: list of cups
    :rtype: list
    """
    return _request("Cups", {'SeasonId': season_id})


def cup_results(cup_id):
    """
    Cup results
    BT1819SWRLCP__SMTS - Men's WC Total 2018/2019
    BT1819SWRLCP__SWTS - Women's WC Total 2018/2019
    :param cup_id: cup identifier, get it by calling cups(season_id)
    :return: selected cup results
    :rtype: dict
    """
    return _request("CupResults", {'CupId': cup_id})


def athletes(family_name='', given_name=''):
    """
    Search athlete
    :param family_name:
    :param given_name:
    :return: found athletes
    :rtype: dict
    """
    return _request("Athletes", {"FamilyName": family_name, "GivenName": given_name})


def cisbios(ibu_id):
    """
    Get athlete by id
    :param ibu_id: ibu identifier of athlete
    :return: athlete info
    :rtype: dict
    """
    return _request("CISBios", {"IBUId": ibu_id})


def all_results(ibu_id):
    """
    All races results of the athlete
    :param ibu_id: ibu identifier of athlete
    :return: races results
    :rtype: dict
    """
    return _request('AllResults', {"IBUId": ibu_id})


def events(season_id, level=0):
    """
    Events of cup (schedule)
    :param season_id: season identifier (1819 for season 2018/2019, get others in a similar way)
    :param level: 0 - all, 1 - BMW IBU WC, 2 - IBU Cup, 3 - Jr. Cup
    :return: list of events
    :rtype: list
    """
    return _request("Events", {"SeasonId": season_id, "Level": level})


def competitions(event_id):
    """
    List of races in stage
    :param event_id: event identifier, get it by calling events(season_id, level=0)
    :return: list of races
    :rtype: list
    """
    return _request('Competitions', {'EventId': event_id})


def results(race_id):
    """
    Race results
    :param race_id: race identifier, get it by calling competitions(event_id)
    :return: list of races
    :rtype: dict
    """
    return _request('Results', {'RaceId': race_id})


def stats(statistic_id, stat_id, by_what, gender_id, season_id='', organizer_id='', ibu_id='', nat=''):
    """
    Statistics
    Not sure how to use it right, here's default query parameters:
    StatisticId=WCPOD_M&StatId=WCPOD&byWhat=ATH&SeasonId=&OrganizerId=&GenderId=M&IBUId=&Nat=
    :param statistic_id:
    :param stat_id:
    :param by_what:
    :param gender_id:
    :param season_id:
    :param organizer_id:
    :param ibu_id:
    :param nat:
    :return: statistics
    :rtype: dict
    """
    return _request('Stats', {
        'StatisticId': statistic_id,
        'StatId': stat_id,
        'byWhat': by_what,
        'SeasonId': season_id,
        'OrganizerId': organizer_id,
        'GenderId': gender_id,
        'IBUId': ibu_id,
        'Nat': nat,
    })
