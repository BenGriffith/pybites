from collections import Counter
from datetime import tzinfo
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commit_log) as file:
        commit_data = file.readlines()

        for commit in commit_data[:1]:
            row_date, row_stats = commit.strip("\n").split("|")
            row_date = parse(row_date.lstrip("Date:").strip(), ignoretz=True)

            row_stats = row_stats.split(",")
            row_stats_insertion = row_stats[1].strip()[0]
            row_stats_deletion = row_stats[2].strip()[0]

    return row_date, row_stats_insertion, row_stats_deletion


if __name__ == "__main__":
    print(get_min_max_amount_of_commits())