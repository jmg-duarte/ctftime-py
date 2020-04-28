from dataclasses import dataclass
from typing import List, Dict

from .team import TeamPoints


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
