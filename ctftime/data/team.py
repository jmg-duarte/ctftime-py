from dataclasses import dataclass
from typing import List, Dict


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
        if "rating" in obj:
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
