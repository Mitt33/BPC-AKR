import re
import settings
from os import listdir
from number_generators import miller_rabin
from setup_logs import setup_logger

save_to_file_logger = setup_logger('save_to_file', ".\logs\save_to_file.log")
load_to_test_logger = setup_logger('load_to_test', ".\logs\load_to_test.log")

def savetofile():
    fname = str(input('input a file name: '))
    f = open(fname + ".txt", "w")
    f.write(str(settings.prime))
    f.close()
    save_to_file_logger.info("number: {a} saved, file: {b}".format(a=str(settings.prime), b=str(fname + ".txt")))


def loadtotest():
    lm = False
    file_list = listdir()
    r = re.compile(f"[\w]+\.txt")
    filtered_list = list(filter(r.match, file_list))
    print(filtered_list)
    choose_file = str(input('input a filename: '))
    f = open(choose_file + ".txt", "r")
    numbertotest = int(f.read())
    if miller_rabin(numbertotest, lm):
        print("The number is prime")
    else:
        print("The number is composite")
    load_to_test_logger.info("number: {a} loaded, from file: {b}".format(a=numbertotest, b=choose_file))
