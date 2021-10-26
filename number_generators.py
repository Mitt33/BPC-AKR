import random
from time import perf_counter


def generate_nbit_number(bit_length):
    return random.randrange(2 ** (bit_length - 1) + 1, 2 ** bit_length - 1)

