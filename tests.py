import random
from time import perf_counter


def miller_rabin(prime_candidate):
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
            print("Testování trvalo %.4f sekund" % (perf_counter() - ref_testing))
            return False
    print("Testování trvalo %.4f sekund" % (perf_counter() - ref_testing))
    return True

def lucas_lehmer(prime_candidate):
    if prime_candidate == 2:
        return True
    s = 4
    M = pow(2, prime_candidate) - 1
    for x in range(1, (prime_candidate - 2) + 1):
        s = ((s * s) - 2) % M
    if s == 0:
        return True
    else:
        return False

def eratosthenes_sieve(prime_candidate):
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
