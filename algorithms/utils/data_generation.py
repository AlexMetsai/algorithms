import random


WHOLE_NUMBERS_ARRAY_LENGTH = 10_000
WHOLE_NUMBERS_RANGE = 1_000_000


def get_whole_number_array():
    return random.choices(population=range(WHOLE_NUMBERS_RANGE), k=WHOLE_NUMBERS_ARRAY_LENGTH)
