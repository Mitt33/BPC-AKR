import random
import settings

from time import perf_counter
from setup_logs import setup_logger

tested_prime_logger = setup_logger('tested_prime', ".\logs\\tested_prime.log")


def miller_rabin(prime_candidate, lm):
    if not lm:
        ref_testing = perf_counter()  # time reference for the testing of primality
    # use the  2^s*r+1 formula
    r, s = 0, prime_candidate - 1
    k = 10  # Number of rounds to test the number, increase gives a higher success chance, decrease speeds up the script
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        prime_base = random.randint(2, prime_candidate - 1)  # choose a random "base" for the calculation
        x = pow(prime_base, s, prime_candidate)  # a ** s % prime_candidate
        if x == 1 or x == prime_candidate - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, prime_candidate)
            if x == prime_candidate - 1:
                break  # prime
        else:

            return False
    if not lm:
        print("Testing prime number took %.4f seconds" % (perf_counter() - ref_testing))
    return True



def lucas_lehmer(p):
    s = 4
    m = 2 ** p - 1
    for _ in range(p - 2):
        s = ((s * s) - 2) % m
    return s == 0



def eratosthenes_sieve():
    print("numbers are generating...this can take a while")
    prime_candidate = int(settings.prime)
    # first we "presume" all values until the given number are prime
    # prime_candidate = 30 testing value
    primelist = [True for prime_candidate in range(prime_candidate + 1)]
    tested_number = 2  # start with 2
    while tested_number * tested_number <= prime_candidate:
        # If list is not changed, then it is a prime
        if primelist[tested_number] is True:
            #  mark all multiples of prime_candidate as not prime
            for i in range(tested_number ** 2, prime_candidate + 1, tested_number):
                primelist[i] = False
        tested_number += 1
    #  manually remove 0, 1
    primelist[0] = False
    primelist[1] = False
    #  print out whatever remained marked as True
    for tested_number in range(prime_candidate + 1):
        if primelist[tested_number]:
            print(tested_number)



"""def sieveOfAtkin():
    prime_candidate = int(settings.prime)
    primelist = [2, 3]
    primelist = [False] * (prime_candidate + 1)
    for x in range(1, int(math.sqrt(prime_candidate)) + 1):
        for y in range(1, int(math.sqrt(prime_candidate)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= prime_candidate and (n % 12 == 1 or n % 12 == 5): primelist[n] = not primelist[n]
            n = 3 * x ** 2 + y ** 2
            if n <= prime_candidate and n % 12 == 7: primelist[n] = not primelist[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= prime_candidate and n % 12 == 11: primelist[n] = not primelist[n]
    for x in range(5, int(math.sqrt(prime_candidate))):
        if primelist[x]:
            for y in range(x ** 2, prime_candidate + 1, x ** 2):
                primelist[y] = False
    for prime_candidate in range(5, prime_candidate):
        if primelist[prime_candidate]: primelist.append(prime_candidate)
    return primelist
"""

def testnumber():
    number = int(input('Input number to be tested: '))
    lm = False
    if miller_rabin(number,lm) is True:
        print("is prime")
        tested_prime_logger.info("number: {a} is: prime".format(a=number))
    else:
        print("not prime")
        tested_prime_logger.info("number: {a} is: composite".format(a=number))