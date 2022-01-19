from multiprocessing.sharedctypes import Value


scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for belt_score, belt_color in BELTS.items():
            if belt_score > self._last_earned_belt:
                self._last_earned_belt = belt_color.capitalize()
        
    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int) or new_score < self._get_score():
            raise ValueError

        self._score = new_score        
        current_belt = self._last_earned_belt
        new_belt = self._get_belt(new_score)
        if new_belt == current_belt:
            print(f"Set new score to {self._score}")
        else:
            print(f"Congrats you earned {new_score} points obtaining the PyBites Ninja {new_belt} Belt")


    score = property(_get_score, _set_score)