import re
import settings
from os import listdir
from number_generators import miller_rabin

def savetofile():
    fname = str(input('input a file name: '))
    f = open(fname + ".txt", "w")
    f.write(str(settings.prime))
    f.close()

def loadtotest():
    file_list = listdir()
    r = re.compile(f"[\w]+\.txt")
    filtered_list = list(filter(r.match, file_list))
    print(filtered_list)
    choose_file = str(input('input a filename: '))
    f = open(choose_file + ".txt", "r")
    numbertotest = int(f.read())
    miller_rabin(numbertotest)
