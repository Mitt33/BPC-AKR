from file_operations import savetofile, loadtotest
from tests import testnumber, eratosthenes_sieve
from number_generators import generate_prime, generate_meresennes
import settings
import os


menu = {
    1: 'Generate Prime Number',
    2: 'Print All Prime Numbers',
    3: 'Save Number To File',
    4: 'Load Number From File To Test',
    5: 'Test a number',
    6: 'End program'
}


def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])


def option1():
    option = int(input('1 -- Generate n-bit prime \n2 -- Generate Mersennes primes: '))

    if option == 1:
        generate_prime()
    elif option == 2:
        generate_meresennes()

def option2():
    print(eratosthenes_sieve())



def option3():
    savetofile()


def option4():
    loadtotest()


def option5():
    testnumber()


def option6():
    quit()


if __name__ == '__main__':
    settings.init()
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Try again')
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        else:
            print(f'Invalid option. Please enter a number between 1 and {list(menu.keys())[-1]}')
