import random
from time import perf_counter

def rand_n(bit_length):
    return random.randrange(2 ** (bit_length - 1) + 1, 2 ** bit_length - 1)


def miller_rabin(pc, k):
    # use the  2^s*r+1 formula
    r, s = 0, pc - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randint(2, pc - 1)

        x = pow(a, s, pc)  # a ** s % pc
        if x == 1 or x == pc - 1:
            continue
        for i_ in range(r - 1):
            x = pow(x, 2, pc)
            if x == pc - 1:
                break
        else:
            return False
    return True


def p_candidate(bit_length):
    # a^n-1 = 1(mod n)
    k = 2
    while True:
        # apply small fermats theorem
        pc = rand_n(bit_length)
        for i in range(k):
            a = random.randint(1, pc - 1)
            if pow(a, pc - 1, pc) != 1:
                continue
            else:
                return pc


if __name__ == '__main__':
    while True:
        print("enter bit length")
        bit_length = int(input())
        k = 5
        ref = perf_counter()
        pc = p_candidate(bit_length)
        if miller_rabin(pc, k) is False:
            continue
        else:
            print(bit_length, "bit prime is: \n", pc)
            print("Operace zabrala %.4f sekund" % (perf_counter() - ref))
            break

    """ run = True

    while run:
        options = [1, 2, 3, 4]
        print("choose a test")
        print("1_Miller Rabin")
        print("2_Fermat")
        print("3_Lucas Lehmer")
        print("4_quit")
        controls = int(input())
        if controls not in options:
            print("bruh")
        if controls == 1:
            print("input tested number")
            n = int(input())
            print("Input number of iterations for tests")
            k = int(input())
            if miller_rabin(n, k) is True:
                print("is prime according to miller rabin")
            else:
                print("not prime according to miller rabin")
        elif controls == 2:
            print("input tested number")
            n = int(input())
            print("Input number of iterations for tests")
            k = int(input())
            if fermat(n, k) is True:
                print("is prime according to fermat")
            else:
                print("not prime according to fermat")
        elif controls == 3:
            if lucas_lehmer(n) == 0:
                print("is composite or not mersennes prime")
            else:
                print(" is a mersennes prime")
        elif controls == 4:
            run = False"""
