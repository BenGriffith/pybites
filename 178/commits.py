from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

def get_min_max_amount_of_commits(commit_log: str = commits, year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commit_log) as file:
        commit_data = file.readlines()
        commit_changes = Counter()

        for commit in commit_data:
            row_date, row_stats = commit.strip("\n").split("|")
            row_date = parse(row_date.lstrip("Date:").strip()).strftime('%Y-%m')

            row_stats = row_stats.split(",")[1:]
            changes = sum([int(row[:row.rfind(" ")].strip()) for row in row_stats])
            
            if year:
                if year == int(row_date[:row_date.find("-")]):
                    commit_changes.update({row_date: changes})
            else:
                commit_changes.update({row_date: changes})

    return (commit_changes.most_common()[-1][0], commit_changes.most_common()[0][0])

# if __name__ == "__main__":
#     print(get_min_max_amount_of_commits(commits, None))