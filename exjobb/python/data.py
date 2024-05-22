import random

def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

def generate_sorted_array(size):
    arr = generate_random_array(size)
    return sorted(arr)

def generate_descending_array(size):
    return list(range(size, 0, -1))
