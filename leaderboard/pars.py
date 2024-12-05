import json, datetime


class Stat:
    score: int
    stars: int
    days: dict # day: Day()

    class Day:
        def __init__(self, part1_ts, part2_ts) -> None:
            self.part1_ts = datetime.datetime.fromtimestamp(part1_ts) if part1_ts is not None else None
            self.part2_ts = datetime.datetime.fromtimestamp(part2_ts) if part2_ts is not None else None

    def __init__(self, name: str) -> None:
        self.name = name
        self.days = dict()


def get_stats(json_data):
    for member in j["members"].keys():
        mem = j["members"][member]
        stat = Stat(mem["name"])
        stat.score = mem["local_score"]
        stat.stars = mem["stars"]

        days = mem["completion_day_level"]
        for d in days.keys():
            day = days[d]
            part1_ts, part2_ts = (None, None)
            if day.get("1", None) != None:
                part1_ts = day["1"].get("get_star_ts", None)
            if day.get("2", None) != None:
                part1_ts = day["2"].get("get_star_ts", None)
            stat.days[d] = stat.Day(part1_ts, part2_ts)
            print(f"name: {stat.name} day {d}: part_1 = {stat.days[d].part1_ts}")


        # print(f"{stat.name} + {stat.score} + {stat.stars}")




with open("j.json") as f:
    j = json.load(f)

get_stats(j)
