from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast, Tuple, Dict
from enum import Enum
from datetime import datetime
import dateutil.parser


@dataclass
class TeamPoints:

    team_id: str
    team_name: str
    points: float

    @staticmethod
    def from_dict(dct) -> "TeamPoints":
        return TeamPoints(dct["team_id"], dct["team_name"], dct["points"])

    def to_dict(self) -> dict:
        result: dict = {}
        result["team_id"] = self.team_id
        result["team_name"] = self.team_name
        result["points"] = self.points
        return result


@dataclass
class Top10:

    year: int
    top: List[TeamPoints]

    @staticmethod
    def from_dict(dct) -> "Top10":
        for year in dct:
            # since theres only one year
            return Top10(year, list(map(TeamPoints.from_dict, dct[year])))

    def to_dict(self) -> dict:
        result: dict = {}
        result["year"] = year
        result["top"] = top
        return result


@dataclass
class Rating:

    organizer_points: float
    rating_points: float
    rating_place: int

    @staticmethod
    def from_dict(dct) -> "Rating":
        return Rating(
            dct["organizer_points"], dct["rating_points"], dct["rating_place"]
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["organizer_points"] = self.organizer_points
        result["rating_points"] = self.rating_points
        result["rating_place"] = self.rating_place
        return result


@dataclass
class Team:

    id: str
    name: str
    aliases: List[str]
    country: str
    academic: bool
    rating: Dict[int, Rating]

    @staticmethod
    def from_dict(obj: dict) -> "Team":
        rating: dict = {}
        for r in obj["rating"]:
            # dumb year as key again
            for year in r:
                rating[year] = Rating.from_dict(r[year])
        return Team(
            obj["id"],
            obj["name"],
            obj["aliases"],
            obj["country"],
            obj["academic"],
            rating,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = self.id
        result["name"] = self.name
        result["aliases"] = self.aliases
        result["country"] = self.country
        result["academic"] = self.academic
        result["rating"] = self.rating
        return result


@dataclass
class TeamsInfo:
    limit: int
    offset: int
    result: List[Team]

    @staticmethod
    def from_dict(obj: dict) -> "TeamsInfo":
        return TeamsInfo(
            obj["limit"], obj["offset"], list(map(Team.from_dict, obj["result"]))
        )

    def to_dict(self):
        result: dict = {}
        result["limit"] = self.limit
        result["offset"] = self.offset
        result["result"] = self.result
        return result


@dataclass
class Score:

    team_id: int
    points: float
    place: int

    @staticmethod
    def from_dict(dct):
        return Score(dct["team_id"], dct["points"], dct["place"])

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Results:

    title: str
    scores: List[Score]
    time: int

    @staticmethod
    def from_dict(obj: dict) -> "Results":
        return Results(
            obj["title"], list(map(Score.from_dict, obj["scores"])), obj["time"]
        )

    def to_dict(self) -> dict:
        results: dict = {}
        results["title"] = self.title
        results["scores"] = self.scores
        results["time"] = self.time
        return results


@dataclass
class Organizer:
    id: int
    name: str

    @staticmethod
    def from_dict(obj: Any) -> "Organizer":
        assert isinstance(obj, dict)
        id = obj["id"]
        name = obj["name"]
        return Organizer(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = self.id
        result["name"] = self.name
        return result


@dataclass
class Duration:
    hours: int = 0
    days: int = 0

    @staticmethod
    def from_dict(obj: Any) -> "Duration":
        assert isinstance(obj, dict)
        hours = obj["hours"]
        days = obj["days"]
        return Duration(hours, days)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hours"] = self.hours
        result["days"] = self.days
        return result


@dataclass
class Event:

    organizers: List[Organizer]
    onsite: bool
    finish: datetime
    description: str
    weight: float
    title: str
    url: str
    is_votable_now: bool
    restrictions: str
    format: str
    start: datetime
    participants: int
    ctftime_url: str
    location: str
    live_feed: str
    public_votable: bool
    duration: Duration
    logo: str
    format_id: int
    id: int
    ctf_id: int

    @staticmethod
    def from_dict(obj: Any) -> "Event":
        assert isinstance(obj, dict)
        organizers = list(map(Organizer.from_dict, obj["organizers"]))
        onsite = obj["onsite"]
        finish = obj["finish"]
        description = obj["description"]
        weight = obj["weight"]
        title = obj["title"]
        url = obj["url"]
        is_votable_now = obj["is_votable_now"]
        restrictions = obj["restrictions"]
        format = obj["format"]
        start = dateutil.parser.parse(obj["start"])
        participants = obj["participants"]
        ctftime_url = obj["ctftime_url"]
        location = obj["location"]
        live_feed = obj["live_feed"]
        public_votable = obj["public_votable"]
        duration = Duration(obj["duration"])
        logo = obj["logo"]
        format_id = obj["format_id"]
        id = obj["id"]
        ctf_id = obj["ctf_id"]
        return Event(
            organizers,
            onsite,
            finish,
            description,
            weight,
            title,
            url,
            is_votable_now,
            restrictions,
            format,
            start,
            participants,
            ctftime_url,
            location,
            live_feed,
            public_votable,
            duration,
            logo,
            format_id,
            id,
            ctf_id,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["organizers"] = list(map(Organizer.to_dict, self.organizers))
        result["onsite"] = self.onsite
        result["finish"] = self.finish.isoformat()
        result["description"] = self.description
        result["weight"] = self.weight
        result["title"] = self.title
        result["url"] = self.url
        result["is_votable_now"] = self.is_votable_now
        result["restrictions"] = self.restrictions
        result["format"] = self.format
        result["start"] = self.start.isoformat()
        result["participants"] = self.participants
        result["ctftime_url"] = self.ctftime_url
        result["location"] = self.location
        result["live_feed"] = self.live_feed
        result["public_votable"] = self.public_votable
        result["duration"] = self.duration
        result["logo"] = self.logo
        result["format_id"] = self.format_id
        result["id"] = self.id
        result["ctf_id"] = self.ctf_id
        return result


@dataclass
class Vote:
    event_id: int
    user_id: int
    user_teams: List[int]
    weight: str
    creation_date: int

    @staticmethod
    def from_dict(obj: dict) -> "Vote":
        return Vote(
            obj["event_id"],
            obj["user_id"],
            obj["user_teams"],
            obj["weight"],
            obj["creation_date"],
        )

    def to_dict(self):
        result: dict = {}
        result["event_id"] = event_id
        result["user_id"] = user_id
        result["user_teams"] = user_teams
        result["weight"] = weight
        result["creation_date"] = creation_date
        return result
