import random
import settings
from time import perf_counter
from tests import miller_rabin, lucas_lehmer
from setup_logs import setup_logger

# first file logger
generated_prime_logger = setup_logger('generated_prime', ".\logs\generated_prime.log")


def generate_nbit_number(bit_length):
    return random.randrange(2 ** (bit_length - 1) + 1, 2 ** bit_length - 1)


def generate_prime():
    while True:
        bit_length = int(input('Bit Length: '))
        if bit_length <= 2:
            print('Bit Length must be greater than 2\n'
                  'try again')
        else:
            break
    tested_numbers = 0
    ref_generation = perf_counter()
    lm = False
    isprime = False
    while not isprime:
        prime_candidate = generate_nbit_number(bit_length)
        tested_numbers += 1
        print(f"Testing Number: ", tested_numbers, end='\r', flush=True)
        if miller_rabin(prime_candidate, lm) is True:
            isprime = True
            settings.prime = prime_candidate
    print(f"Bylo otestováno {tested_numbers} čísel\nVygenerováno bylo prvočíslo {prime_candidate}")
    print("Generace prvočísla trvala: %.4f sekund" % (perf_counter() - ref_generation))
    generated_prime_logger.info(
        'time: {a}, bit_lenght: {b}, tested_numbers: {c}, number_generated: {d}'.format
        (a=(perf_counter() - ref_generation), b=bit_length, c=tested_numbers, d=prime_candidate))


def generate_meresennes():
    index = int(input("Počet mersennových prvočísel:"))
    lm = True
    print(3)
    counter = 1

    for prime_candidate in range(3, 1000000, 2):
        if index == counter:
            break

        if miller_rabin(prime_candidate, lm) and lucas_lehmer(prime_candidate):
            counter += 1
            print(2 ** prime_candidate - 1)
