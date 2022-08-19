from collections import namedtuple
from datetime import date

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(year=stime.tm_year, month=stime.tm_mon, day=stime.tm_mday)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
        Return a list of Entry namedtuples (date = date, drop time part)
    """
    entries = []

    feed_parsed = feedparser.parse(feed)
    for key, value in feed_parsed.items():
        if key == "entries":
            for _food_entry in value:
                entry_date = _convert_struct_time_to_dt(_food_entry.get("published_parsed"))

                feed_entry = Entry(
                    date=entry_date, 
                    title=_food_entry.get("title"), 
                    link=_food_entry.get("link"), 
                    tags=[value.lower() for tag in _food_entry.get("tags") for key, value in tag.items() if key == "term"]
                    )

                entries.append(feed_entry)

    return entries


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
        (case insensitive, only whole, not partial string matches).
        Returns bool: True if match, False if not.
        Supported searches:
        1. If & in search do AND match,
            e.g. flask&api should match entries with both tags
        2. Elif | in search do an OR match,
            e.g. flask|django should match entries with either tag
        3. Else: match if search is in tags
    """
    search = search.lower()
    is_match = False
    if search.find("&") > 0:
        terms = search.split("&")
        for term in terms:
            if term in entry.tags:
                is_match = True
            else:
                is_match = False

    elif search.find("|") > 0:
        terms = search.split("|")
        for term in terms:
            if term in entry.tags:
                is_match = True
    else:
        if search in entry.tags:
            is_match = True

    return is_match


def main():
    """Entry point to the program
        1. Call get_feed_entries and store them in entries
        2. Initiate an infinite loop
        3. Ask user for a search term:
            - if enter was hit (empty string), print 'Please provide a search term'
            - if 'q' was entered, print 'Bye' and exit/break the infinite loop
        4. Filter/match the entries (see filter_entries_by_tag docstring)
        5. Print the title of each match ordered by date ascending
        6. Secondly, print the number of matches: 'n entries matched'
            (use entry if only 1 match)
    """
    feed_entries = get_feed_entries()

    while True:
        search_term = input("Please provide a search term: ")
        if search_term == "":
            print("Please provide a search term: ")
            continue
        if search_term == "q":
            print("Bye")
            break
        
        matches = []
        for entry in feed_entries:
            is_match = filter_entries_by_tag(search_term, entry)
            if is_match:
                matches.append(entry)

        matches.sort(key=lambda x: x.date)
        for match in matches:
            print(match.title)

        matches_count = len(matches)
        if matches_count == 0:
            print("0 entries matched")
        elif matches_count == 1:
            print("1 entry matched")
        else:
            print(f"{matches_count} entries matched")


if __name__ == '__main__':
    main()