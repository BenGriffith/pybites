from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    titles = soup.find_all("span", class_="title")
    titles_points_comments = soup.find_all("span", class_="controls")

    entries_titles = []
    for title in titles:
        title = title.get_text().strip()
        entries_titles.append([title])

    entries_points_comments = []
    for points_comments in titles_points_comments:
        points, comments = points_comments.get_text().strip().split("|")
        points, comments = points.strip().split(" ")[0], comments.strip().split(" ")[0]
        entries_points_comments.append([points, comments])

    entries = []
    for i in zip(entries_titles, entries_points_comments):
        title, points_comments = i[0], [int(num) for num in i[1]]
        entry = title + points_comments
        entries.append(entry)

    entries.sort(key=lambda x: (x[1], x[2]), reverse=True)

    for i in range(len(entries)):
        entry = entries[i]
        title, points, comments = entry[0], entry[1], entry[2]
        entries[i] = Entry(title, points, comments)

    return entries[:top]