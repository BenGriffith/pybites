import calendar
from datetime import date
from typing import Tuple

"""
Sample text if on-track:
Congratulations! You are on track with your steps goal. The target for 2023-01-12 is 164,383 steps and you are 11 ahead.

Sample text if not on track:
You have some catching up to do! The target for 2023-09-30 is 27,300 pages read and you are 2 behind.
"""


def goal_tracker(desc: str, annual_target: int, current_score: int, score_date: Tuple[int, int, int]):
     """Return a string determining whether a goal is on track
     by calculating the current target and comparing it with the current achievement.
     The function assumes the goal is to be achieved in a calendar year. Think New Year's Resolution :)
     """
     year, month, day = score_date
     _score_date = date(year, month, day)

     days_in_year = 366 if calendar.isleap(year) else 365
     elapsed_days = day if month == 1 else (_score_date - date(year, 1, 1)).days + 1

     daily_target = annual_target / days_in_year
     current_target = int(daily_target * elapsed_days)
 
     if current_score >= current_target:
          return f"Congratulations! You are on track with your {desc} goal. The target for {_score_date} is {current_target:,} {desc} and you are {current_score - current_target} ahead."
     
     return f"You have some catching up to do! The target for {_score_date} is {current_target:,} {desc} and you are {current_target - current_score} behind."