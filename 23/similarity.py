import os
import re
from difflib import SequenceMatcher
import itertools
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TMP = os.getenv("TMP", "/tmp")
TEMPFILE = os.path.join(TMP, 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
    TEMPFILE
)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # do your thing ...
    similar_tags = []
    for tag in tags:     
        for _tag in tags:
            if tag == _tag:
                continue
            else:
                comparison = SequenceMatcher(None, tag, _tag)
                if comparison.ratio() > SIMILAR:
                    similar_tags.append((tag, _tag))

    return similar_tags


if __name__ == "__main__":
    print(get_similarities())