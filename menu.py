from number_generators import generate_prime

menu = {
    1: 'Generate Prime Number',
    2: 'Print All Prime Numbers',
    3: 'Save Number To File',
    4: 'Load Number From File',
    5: 'Load Number From File To Test',
    6: 'W I P'
}


def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])


def option1():
    generate_prime()


def option2():
    print('Option 2')


def option3():
    print('Option 3')


def option4():
    print('Option 4')


def option5():
    print('Option 5')


def option6():
    print('Option 6')


if __name__ == '__main__':
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
