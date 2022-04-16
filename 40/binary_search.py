from string import ascii_lowercase

def binary_search(sequence, target):

    start = 0
    end = len(sequence) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if sequence[mid] == target:
            return mid
        
        elif sequence[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return None
