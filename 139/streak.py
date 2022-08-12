from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = set()
    for element in data.split("|"):
        try:
            valid_date = datetime.strptime(element.strip(), "%Y-%m-%d")
            dates.add(valid_date.date())
        except:
            pass

    return sorted(list(dates), reverse=True)


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    highest_streak = 0
    coding_streak = 0
    yesterday = TODAY - timedelta(days=1)

    for i in range(len(dates)):
        if i == 0 and (dates[i] not in [yesterday, TODAY]):
            return coding_streak
            
        if dates[i] == TODAY:
            coding_streak += 1
            highest_streak += 1

        if dates[i] == yesterday:
            coding_streak += 1
            highest_streak += 1

        previous_date = dates[i - 1]
        current_date = dates[i]

        if current_date not in [TODAY, yesterday] and coding_streak > 0:
            if (previous_date - current_date).days == 1:
                coding_streak += 1
                if coding_streak > highest_streak:
                    highest_streak += 1
            else:
                coding_streak = 0

    return highest_streak
            




if __name__ == "__main__":
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-08 | pcc        | 1       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    print(calculate_streak(dates))