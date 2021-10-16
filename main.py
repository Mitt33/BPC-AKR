import random
from time import perf_counter


def rand_n(bit_length):
    return random.randrange(2 ** (bit_length - 1) + 1, 2 ** bit_length - 1)


def miller_rabin(pc):
    refTesting = perf_counter()  # time reference for the testing of primality
    # use the  2^s*r+1 formula
    r, s = 0, pc - 1
    k = 10  # Number of rounds to test the number, increase gives a higher succes chance, decrease speeds up the script
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randint(2, pc - 1)  # choose a random "base" for the calculation

        x = pow(a, s, pc)  # a ** s % pc
        if x == 1 or x == pc - 1:
            continue
        for i_ in range(r - 1):
            x = pow(x, 2, pc)
            if x == pc - 1:
                break  # prime
        else:
            return False
    print("Testování %.4f sekund" % (perf_counter() - refTesting))
    return True


def p_candidate(bit_length):
    refGeneration = perf_counter()  # reference point for generation of the prime number candidate itself
    # a^n-1 = 1(mod n)
    k = 2
    #  use fermats test to test the generated candidate, probably redundant and can be removed

    while True:
        # apply small fermats theorem
        pc = rand_n(bit_length)
        for i in range(k):
            a = random.randint(1, pc - 1)
            if pow(a, pc - 1, pc) != 1:
                continue  # not prime
            else:
                print("Generace prvočísla zabrala %.4f sekund" % (perf_counter() - refGeneration))
                return pc


def eratosthenes_sieve(pc):
    # first we "presume" all values until the given number are prime
    # pc = 30 testing value
    primelist = [True for i in range(pc + 1)]

    primeCandidate = 2  # start with 2

    while primeCandidate * primeCandidate <= pc:
        # If list is not changed, then it is a prime
        if primelist[primeCandidate] is True:
            #  mark all multiples of primeCandidate as not prime
            for i in range(primeCandidate ** 2, pc + 1, primeCandidate):
                primelist[i] = False

        primeCandidate += 1
    #  manually remove 0, 1
    primelist[0] = False
    primelist[1] = False

    #  print out whatever remained maked as True
    for primeCandidate in range(pc + 1):
        if primelist[primeCandidate]:
            print(primeCandidate)


if __name__ == '__main__':
    while True:
        print("enter bit length")
        bit_length = int(input())

        pc = p_candidate(bit_length)
        if miller_rabin(pc) is False:
            continue
        else:
            print(bit_length, "bit prime is: \n", pc)
            print("input 1 to print all primes ")
            option = int(input())

            if option == 1:
                eratosthenes_sieve(pc)
            else:
                break
