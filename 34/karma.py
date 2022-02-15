from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    
    def __init__(self, name):
        self.name = name
        self._transactions = []
        self._fans = []

    def __add__(self, other):
        self._transactions.append(other.points)
        if other.giver not in self._fans:
            self._fans.append(other.giver)
        return self

    def __str__(self):
        sing_or_plural = "fans" if self.fans > 1 else "fan"
        return f"{self.name} has a karma of {self.karma} and {self.fans} {sing_or_plural}"

    @property
    def karma(self):
        return sum(self._transactions)

    @property
    def points(self):
        return self._transactions

    @property
    def fans(self):
        return len(self._fans)