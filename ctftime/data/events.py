from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime
from dateutil import parser


@dataclass
class Organizer:
    id: int
    name: str

    @staticmethod
    def from_dict(obj: dict) -> "Organizer":
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
    def from_dict(obj: dict) -> "Duration":
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
    def from_dict(obj: dict) -> "Event":
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
        start = parser.parse(obj["start"])
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
