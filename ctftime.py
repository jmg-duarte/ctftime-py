import requests
import json

from pprint import pformat, pprint

from dataclasses import dataclass
from typing import List, Tuple

from data import *

URL = "https://ctftime.org/api"
API_VERSION = "/v1"
API_URL = URL + API_VERSION


def _append_slash(s: str):
    if s.endswith("/"):
        return s
    return s + "/"


def top10(year: str = "2020"):
    url = f"{API_URL}/top/"
    if year is not None:
        url += year
    url = _append_slash(url)
    print(url)
    resp = requests.get(
        url,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return Top10.from_dict(json.loads(resp.content))


# print(top10("2015"))


def events(limit: int = 10, start: int = None, finish: int = None):
    params = {}
    params["limit"] = limit
    if start is not None:
        params["start"] = start
    if finish is not None:
        params["finish"] = finish
    url = f"{API_URL}/events/"
    resp = requests.get(
        url,
        params=params,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return list(map(Event.from_dict, json.loads(resp.content)))


def teams(limit: int = 10, offset: int = 0):
    params = {"limit": limit, "offset": offset}
    url = f"{API_URL}/teams/"
    resp = requests.get(
        url,
        params=params,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return TeamsInfo.from_dict(json.loads(resp.content))


# print(teams())


def team(team_id: str):
    url = f"{API_URL}/teams/"
    if team_id is not None:
        url += team_id
    url = _append_slash(url)
    resp = requests.get(
        url,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return Team.from_dict(json.loads(resp.content))


# print(team("1005"))
# print(team("112556"))


def results(year: str = None) -> List[Results]:
    url = f"{API_URL}/results/"
    if year is not None:
        url += year
    url = _append_slash(url)
    resp = requests.get(
        url,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    j = json.loads(resp.content)
    return list(map(lambda x: j[x], j))


# print(results("2020"))


def votes(year: str):
    url = f"{API_URL}/votes/"
    if year is None:
        return  # this should be an exception
    url += year
    url = _append_slash(url)
    resp = requests.get(
        url,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return list(map(Vote.from_dict, json.loads(resp.content)))


# print(votes("2020"))
