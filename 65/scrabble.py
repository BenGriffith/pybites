from audioop import reverse
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

    for i in range(1, len(draw) + 1):
        
        list_of_permutations = list(itertools.permutations(draw, i))

        for word in list_of_permutations:
            words.append("".join(list(word)))
        
    return words


# if __name__ == "__main__":
#     letters  = 'T, I, I, G, T, T, L'.split(", ")
#     letters1 = 'B, R, C, O, O, E, O'.split(", ")
#     letters2 = 'O, N, V, R, A, Z, H'.split(", ")
#     print(get_possible_dict_words(letters2))