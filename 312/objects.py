import keyword
import importlib
from typing import Dict, List

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    
    score = []

    for object in objects:

        try:
            importlib.import_module(object)
            score.append(scores["module"])
        except:
            if object in keyword.__builtins__:
                score.append(scores["builtin"])
            
            if keyword.iskeyword(object):
                score.append(scores["keyword"])
            else:
                continue

    return sum(score)


if __name__ == "__main__":
    objects = ['builtins', 'numbers', 'os']
    score_objects(objects)