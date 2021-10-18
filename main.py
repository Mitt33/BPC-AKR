import random
from time import perf_counter
import os
import re

'''
TODO:

Další Generace Primes
Další Test privočíselnosti
Lepší proměnné
Změna jmen funkcí
Logging při generace - errory 
Log výpis síta 
časovače
MultiThreading

Try Except: -- general Error handling
Docstringy

Projet Blackem

Pokud bude čas udělat Fancy menu

'''


def rand_n(bit_length):
    return random.randrange(2 ** (bit_length - 1) + 1, 2 ** bit_length - 1)


def miller_rabin(pc):
    ref_testing = perf_counter()  # time reference for the testing of primality
    # use the  2^s*r+1 formula
    r, s = 0, pc - 1
    k = 10  # Number of rounds to test the number, increase gives a higher success chance, decrease speeds up the script
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
    print("Testování trvalo %.4f sekund" % (perf_counter() - ref_testing))
    return True


def p_candidate(bit_length):
    ref_generation = perf_counter()  # reference point for generation of the prime number candidate itself
    # a^n-1 = 1(mod n)
    k = 2
    #  use fermat test to test the generated candidate, probably redundant and can be removed

    while True:
        # apply small fermat theorem
        pc = rand_n(bit_length)
        for i in range(k):
            a = random.randint(1, pc - 1)
            if pow(a, pc - 1, pc) != 1:
                continue  # not prime
            else:
                print("Generace prvočísla zabrala %.4f sekund" % (perf_counter() - ref_generation))
                return pc


def eratosthenes_sieve(pc):
    # first we "presume" all values until the given number are prime
    # pc = 30 testing value
    primelist = [True for i in range(pc + 1)]

    prime_candidate = 2  # start with 2

    while prime_candidate * prime_candidate <= pc:
        # If list is not changed, then it is a prime
        if primelist[prime_candidate] is True:
            #  mark all multiples of prime_candidate as not prime
            for i in range(prime_candidate ** 2, pc + 1, prime_candidate):
                primelist[i] = False

        prime_candidate += 1
    #  manually remove 0, 1
    primelist[0] = False
    primelist[1] = False

    #  print out whatever remained marked as True
    for prime_candidate in range(pc + 1):
        if primelist[prime_candidate]:
            print(prime_candidate)


if __name__ == '__main__':
    menu = True

    while menu:
        print("1__Generate prime number")
        print("2__Print all prime numbers")
        print("3__Save number")
        print("4__Load a number to test")
        print("5__Test a number")
        option = int(input())

        if option == 1:
            print("enter bit length")
            bit_length = int(input())
            while True:

                pc = p_candidate(bit_length)
                if miller_rabin(pc) is False:
                    continue
                else:
                    print(bit_length, "bit prime is: \n", pc)
                    break

        # print all primes until the given number
        elif option == 2:
            eratosthenes_sieve(pc)
            continue

        # save number into a .txt file
        elif option == 3:
            print("input file name")
            fname = str(input())  # choose a name
            f = open(fname + ".txt", "w")
            f.write(str(pc))  # write the generated prime into the file
            f.close()  # close the file
        # loading from a file and testing
        elif option == 4:
            file_list = os.listdir()  # list all files in the project directory
            r = re.compile(f"[\w]+\.txt")  # filter out anything thats not .txt
            filtered_list = list(filter(r.match, file_list))
            print(filtered_list)  # print .txt files in directory
            print("input file name")
            choose_file = str(input())
            f = open(choose_file + ".txt", "r")
            pc = int(f.read())  # save the number as a prime candidate to test

            if miller_rabin(pc) is True:
                print("The given number is prime")
            else:
                print("the number is composite")
            continue
        # number testing
        elif option == 5:  # needs another way to test prime numbers ( Lucas Lehmer ?)
            print("input tested number")
            pc = int(input())
            if miller_rabin(pc) is True:
                print("is prime")
            else:
                print("is composite")
            continue
        else:
            break
