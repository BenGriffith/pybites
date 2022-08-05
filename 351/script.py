from typing import List, NamedTuple

from textblob import Word

MIN_CONFIDENCE = 0.5


# define SuggestedWord NamedTuple with attributes
# word (str) and confidence (float)
class SuggestedWord(NamedTuple):
    word: str
    confidence: float


def get_spelling_suggestions(
    word: str, min_confidence: float = MIN_CONFIDENCE
) -> List[SuggestedWord]:
    """
    Find spelling suggestions with at least minimum confidence score
    Use textblob.Word (check out the docs)
    """
    suggestions = []
    
    for suggestion in Word(word).spellcheck():
        word, confidence = suggestion
        if confidence >= min_confidence:
            suggestions.append(SuggestedWord(word, confidence))
    
    return suggestions


if __name__ == "__main__":
    print(get_spelling_suggestions("kinda"))