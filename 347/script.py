from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """

    left_hand, right_hand = False, False

    for char in word:
        char = char.upper()
        if char in LEFT_HAND_CHARS:
            left_hand = True
        
        if char in RIGHT_HAND_CHARS:
            right_hand = True

    if left_hand and right_hand:
        return Hand.BOTH

    if left_hand:
        return Hand.LEFT
    
    if right_hand:
        return Hand.RIGHT