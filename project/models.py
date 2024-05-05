
import json
from datetime import datetime

from dataclasses import dataclass


@dataclass
class Set:
    repetitions: int = 0
    time: int = 0
    weight: float = 0.0
    distance_KM: float = 0.0

    @classmethod
    def load(cls, data: dict[str, int | int | float | float]) -> 'Set':
        return cls(repetitions=data["repetitions"], time=data["time"], weight=data["weight"],
                   distance_KM=data["distance_KM"])

    def dump(self) -> dict[str, int | str | float | float]:
        return {"repetitions": self.repetitions, "time": self.time, "weight": self.weight,
                "distance_KM": self.distance_KM}


@dataclass
class Exercise:
    name: str
    power: bool
    sets: list[Set]

    @classmethod
    def load(cls, data: dict[str, str | bool | list["sets"]]) -> 'Exercise':
        return cls(name=data["name"], power=data["power"], sets=[Set.load(s) for s in data["sets"]])

    def dump(self) -> dict[str, str | list[dict[str, int | bool | int]]]:
        return {"name": self.name, "power": self.power, "sets": [s.dump() for s in self.sets]}


@dataclass
class Workout:
    date: str
    workout_name: str
    exercises: list[Exercise]

    @classmethod
    def load(cls, data: dict[str, str | str | list[Exercise]]) -> 'Workout':
        return cls(date=data["date"], workout_name=data["workout_name"], exercises=[Exercise.load(e) for e in data["exercises"]])

    def dump(self) -> dict[str, str | list[dict[str, str | list[dict[str, int]]]]]:
        return {"date": self.date, "workout_name": self.workout_name, "exercises": [e.dump() for e in self.exercises]}


# sl = []
# s = Set(repetitions=10, time=2, weight=15, distance_KM=1.2)
# print(s)
# print(s.dump())
# print(type(s.dump()))
# sl.append(s)
#
#
# print("***********")
# print(json.dumps(s.dump()))
# print(type(json.dumps(s.dump())))
#
# s = Set(repetitions=20, time=1, weight=15)
# sl.append(s)
#
# print(sl)
#
# el = []
# e = Exercise(name="pushups", power=True, sets=sl)
# el.append(e)
# e2 = Exercise(name="squats", power=False, sets=sl)
# el.append(e2)
#
#
# print(e)
#
# print(e.dump())
#
# print(json.dumps(e.dump()))
#
# print(json.loads(json.dumps(e.dump())))
# print(type(json.loads(json.dumps(e.dump()))))
#
# print(Exercise.load(json.loads(json.dumps(e.dump()))))
#
#
# print("workout:")
#
# date1 = datetime(2024, 5, 6)
# d1 = date1.strftime('%Y-%m-%d')
#
# w = Workout(date=d1, workout_name="legs", exercises=el)
#
# print(w)
# print(json.dumps(w.dump(), indent=4))



