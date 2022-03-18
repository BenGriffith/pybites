from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    result = []
    if N == 0:
        return result

    while len(result) < N:
        if len(result) == 0:
            result.append([1])
        elif len(result) == 1:
            result.append([1, 1])
        else:
            result.append([1, 1])
            print(result[-2])
            for i in range(len(result[-2])):
                print(i)
                if i == 0:
                    continue
                result[-1].insert(1, result[-2][i - 1] + result[-2][i])
    return result[-1]


if __name__ == "__main__":
    print(pascal(10))