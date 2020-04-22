import requests
import json

from pprint import pformat, pprint

from dataclasses import dataclass
from typing import List, Tuple

URL = "https://ctftime.org/api"
API_VERSION = "/v1"
API_URL = URL + API_VERSION


def _append_slash(s: str):
    if s.endswith("/"):
        return s
    return s + "/"


@dataclass
class TeamPoints(object):

    team_id: str
    team_name: str
    points: float

    @staticmethod
    def decode(dct):
        if "team_id" in dct and "team_name" in dct and "points" in dct:
            return TeamPoints(dct["team_id"], dct["team_name"], dct["points"])
        return None

    def __str__(self):
        return f"team_id: {self.team_id}\nteam_name: {self.team_name}\npoints: {self.points}\n"


@dataclass
class Top10(object):

    year: int
    top: List[TeamPoints]

    @staticmethod
    def decode(year):
        def _decode(dct):
            team = TeamPoints.decode(dct)
            if team is None:
                return Top10(year, dct[year])
            return TeamPoints.decode(dct)

        return _decode

    def __str__(self):
        return f"year: {self.year}\ntop: {pformat(self.top)}"


def top10(year: str = "2020"):
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
    print(json.loads(resp.content, object_hook=Top10.decode(year)))
    return resp


# print(top10("2015"))


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


@dataclass
class Rating(object):

    organizer_points: float
    rating_points: float
    rating_place: int

    @staticmethod
    def decode(dct):
        if (
            "organizer_points" in dct
            and "rating_points" in dct
            and "rating_place" in dct
        ):
            return Rating(
                dct["organizer_points"], dct["rating_points"], dct["rating_place"]
            )
        return None


@dataclass
class Team(object):

    id: str
    name: str
    aliases: List[str]
    country: str
    academic: bool
    rating: List[Tuple[int, Rating]]

    @staticmethod
    def decode(dct):
        pprint(dct)
        rating = Rating.decode(dct)
        if rating is not None:
            return rating
        if "id" not in dct:
            # hack to bypass the dumb use of year value as key
            for v in dct:
                return (v, dct[v])
        if "rating" not in dct:
            return Team(
                dct["id"], dct["name"], dct["aliases"], dct["country"], dct["academic"],
            )
        return Team(
            dct["id"],
            dct["name"],
            dct["aliases"],
            dct["country"],
            dct["academic"],
            dct["rating"],
        )


def teams(limit: int = 10, offset: int = 0):
    params = {"limit": limit, "offset": offset}
    url = "https://ctftime.org/api/v1/teams/"
    resp = requests.get(
        url,
        params=params,
        headers={
            "Referer": "https://ctftime.org/api/",
            "User-Agent": "Mozilla/5.0",  # the API does not accept the default UA
        },
    )
    # print(json.loads(resp.content, object_hook=Team.decode))
    return resp


# print(teams())


def team(team_id: str):
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
    print(resp.text)
    # print(json.loads(resp.content, object_hook=Team.decode))
    return resp


# print(team("1005"))
# print(team("112556"))


@dataclass
class Score(object):

    team_id: int
    points: float
    place: int

    @staticmethod
    def decode(dct):
        if "team_id" in dct and "points" in dct and "place" in dct:
            return Score(dct["team_id"], dct["points"], dct["place"])
        return None


class Results(object):

    title: str
    scores: List[Score]
    time: int

    @staticmethod
    def decode(dct):
        score = Score.decode(dct)
        if score is not None:
            return score
        print(dct)
        return Results(dct["title"], dct["scores"], dct["time"])


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
    print(resp.text)
    # print(json.loads(resp.content, object_hook=Team.decode))
    return resp


results("2020")


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
