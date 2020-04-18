import requests

URL = "https://ctftime.org/api"
API_VERSION = "/v1"
API_URL = URL + API_VERSION


def _append_slash(s: str):
    if s.endswith("/"):
        return s
    else:
        return s + "/"


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
    print(resp.request.headers)
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


print(top10("2014/").json())
print(teams().json())
print(team("112556").json())
