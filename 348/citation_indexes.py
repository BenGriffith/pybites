from typing import Sequence

TYPE_ERROR_MSG = "Unsupported input type: use either a list or a tuple"
VALUE_ERROR_MSG = "Unsupported input value: citations cannot be neither empty nor None"


def check_errors(citations):
    if citations is None:
        raise ValueError(VALUE_ERROR_MSG)

    if not isinstance(citations, (list, tuple)):
        raise TypeError(TYPE_ERROR_MSG)

    if len(citations) == 0:
        raise ValueError(VALUE_ERROR_MSG)

    for citation in citations:
        if not isinstance(citation, int):
            raise ValueError(VALUE_ERROR_MSG)
            
        if citation < 0:
            raise ValueError(VALUE_ERROR_MSG)


def h_index(citations: Sequence[int]) -> int:
    """Return the highest number of papers h having at least h citations"""
   
    check_errors(citations)

    if isinstance(citations, tuple):
        citations = list(citations)
    
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i < citations[i]:
            continue
        return i


def i10_index(citations: Sequence[int]) -> int:
    """Return the number of papers having at least 10 citations"""
    
    check_errors(citations)

    citation_count = 0
    for citation in citations:
        if citation >= 10:
            citation_count += 1
    return citation_count


if __name__ == "__main__":
    print(h_index([0, 0, 1, 1, 10, 5, 11, 13]))
    print(h_index([0, 0, 0, 0]))