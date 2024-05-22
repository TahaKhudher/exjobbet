def linear_search(arr, key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1
