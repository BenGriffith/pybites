from typing import Tuple
from collections import Counter


def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    if not isinstance(text, str):
        raise ValueError

    words = text.split(" ")
    counters = []
    acceptable = ["-", "'"]
    for word in words:
        characters_remove = []
        for char in word:
            if char in acceptable:
                continue
            
            if not char.isalpha():
                characters_remove.append(char)

        if len(characters_remove) > 0:
            word = list(word)
            for char in characters_remove:
                word.remove(char)
            word = "".join(word)

        letter_frequency = Counter()
        letter_frequency.update(word.casefold())
        counters.append({word.strip(acceptable[0] + acceptable[1]): letter_frequency})
    
    max_word = ""
    max_letter = ""
    max_count = 0

    for counter in counters:
        for counter_word, counter_letters in counter.items():
            for counter_letter, counter_count in counter_letters.items():
                if counter_letter.isalpha() and counter_count > max_count:
                    max_word = counter_word
                    max_letter = counter_letter
                    max_count = counter_count

    return (max_word, max_letter, max_count)


# if __name__ == "__main__":
#     print(max_letter_word('der Schloß is riesig'))