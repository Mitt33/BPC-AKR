import random
import settings
from time import perf_counter
from tests import miller_rabin, lucas_lehmer


def generate_nbit_number(bit_length):
    return random.randrange(2 ** (bit_length - 1) + 1, 2 ** bit_length - 1)


def generate_prime():
    bit_length = int(input('Bit Length: '))
    tested_numbers = 0
    ref_generation = perf_counter()

    isprime = False
    while not isprime:
        prime_candidate = generate_nbit_number(bit_length)
        tested_numbers += 1
        if miller_rabin(prime_candidate) is True:
            isprime = True
            settings.prime = prime_candidate
    print(f"Bylo otestováno {tested_numbers} čísel\nVygenerováno bylo prvočíslo {prime_candidate}")
    print("Generace prvočísla trvala: %.4f sekund" % (perf_counter() - ref_generation))
