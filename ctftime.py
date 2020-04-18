import requests
import json
from pprint import pformat

URL = "https://ctftime.org/api"
API_VERSION = "/v1"
API_URL = URL + API_VERSION


def _append_slash(s: str):
    if s.endswith("/"):
        return s
    else:
        return s + "/"


class ShortTeam(object):
    def __init__(self, team_id, team_name, points):
        super().__init__()
        self.team_id = team_id
        self.team_name = team_name
        self.points = points

    @staticmethod
    def decode(dct):
        if "team_id" in dct and "team_name" in dct and "points" in dct:
            return ShortTeam(dct["team_id"], dct["team_name"], dct["points"])
        else:
            return None

    def __str__(self):
        return f"team_id: {self.team_id}\nteam_name: {self.team_name}\npoints: {self.points}\n"


class Top10(object):
    def __init__(self, year, top):
        super().__init__()
        self.year = year
        self.top = top

    @staticmethod
    def decode(year):
        def _decode(dct):
            team = ShortTeam.decode(dct)
            if team is None:
                return Top10(year, dct[year])
            else:
                return ShortTeam.decode(dct)

        return _decode

    def __str__(self):
        return f"year: {self.year}\ntop: {pformat(self.top)}"


def top10(year: str = None):
    url = "https://ctftime.org/api/v1/top/"
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
    print(resp.text)
    print(json.loads(resp.content, object_hook=Top10.decode(year)))
    return resp


print(top10("2015"))


def events(limit: int = 10, start: int = None, finish: int = None):
    params = {}
    params["limit"] = limit
    if start is not None:
        params["start"] = start
    if finish is not None:
        params["finish"] = finish
    url = "https://ctftime.org/api/v1/events/"
    resp = requests.get(
        url,
        params=params,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return resp


def teams(limit: int = 10):
    url = "https://ctftime.org/api/v1/teams/"
    resp = requests.get(
        url,
        params={"limit": limit},
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    return resp


def team(team_id: str = None):
    url = "https://ctftime.org/api/v1/teams/"
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
    return resp


def results(year: str = None):
    url = "https://ctftime.org/api/v1/results/"
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
    return resp


def votes(year: str):
    url = "https://ctftime.org/api/v1/results/"
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
    return resp
