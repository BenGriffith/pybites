from dataclasses import dataclass, field
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __lt__(self, other):
        return self.bites < other.bites

    def __gt__(self, other):
        return self.bites > other.bites

    def __eq__(self, other):
        return self.bites == other.bites

    def __repr__(self):
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    ninjas: list[Ninja] = field(default_factory=list)

    def __len__(self):
        return len(self.ninjas)

    def add(self, ninja):
        self.ninjas.append(ninja)
        return self

    def dump(self):
        self.ninjas.sort(key=lambda x: x.bites, reverse=True)
        return self.ninjas.pop()

    def highest(self, count=None):
        self.ninjas.sort(key=lambda x: x.bites, reverse=True)
        if count:
            return self.ninjas[:count]
        return self.ninjas[:1]

    def lowest(self, count=None):
        self.ninjas.sort(key=lambda x: x.bites)
        if count:
            return self.ninjas[:count]
        return self.ninjas[:1]

    def pair_up(self, count=3):
        return list(zip(self.highest(count), self.lowest(count)))


if __name__ == "__main__":
    ben = Ninja("Ben", 200)
    rankings = Rankings()
    rankings.add(ben)
    jess = Ninja("Jess", 100)
    rankings.add(jess)
    print(len(rankings))
    print(rankings)
    print(rankings.lowest())