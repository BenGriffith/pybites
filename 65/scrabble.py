import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    possible_words = []
    list_of_permutations = _get_permutations_draw(draw)
    for word in list_of_permutations:
        word = word.lower()
        if word in dictionary:
            possible_words.append(word)
    
    return possible_words

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    words = []

    #draw = draw.replace(", ", "")
    for i in range(len(draw) +1):
        #print(draw[i])
        temp = list(draw[:i +1])
        print(temp[:i])
        for j in itertools.permutations(temp, i):
            print(j)
            #words.append("".join(j))
    return words


if __name__ == "__main__":
    letters = 'T, I, I, G, T, T, L'.split(", ")
    #letters1 = 'B, R, C, O, O, E'.split(",")
    #print(_get_permutations_draw(letters))
    print(get_possible_dict_words(letters))