import re
import settings
from os import listdir
from number_generators import miller_rabin
from setup_logs import setup_logger

file_operations_logger = setup_logger('file_operations', ".\logs\\file_operations.log")


def savetofile():
    fname = str(input('input a file name: '))
    f = open(fname + ".txt", "w")
    f.write(str(settings.prime))
    f.close()
    file_operations_logger.info("number: {a} saved, file: {b}".format(a=str(settings.prime), b=str(fname + ".txt")))


def loadtotest():
    lm = False
    file_list = listdir()
    r = re.compile(f"[\w]+\.txt")
    filtered_list = list(filter(r.match, file_list))
    print(filtered_list)
    counter = 0
    while True:
        try:
            if counter >= 3:
                break
            choose_file = str(input('input a filename without extension: '))
            f = open(choose_file + ".txt", "r")
            numbertotest = int(f.read())
            if miller_rabin(numbertotest, lm):
                print("The number is prime")
            else:
                print("The number is composite")
            file_operations_logger.info("number: {a} loaded, file: {b}".format(a=numbertotest, b=(choose_file + ".txt")))
            break
        except FileNotFoundError:
            counter += 1
            print("File with that name doesn't exist\n"
                  "Try again")
