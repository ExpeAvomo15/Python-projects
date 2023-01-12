import numbers


def preguntar():

    print('Welcome to Python farmacy')

    while True:
        print("[P] - Perfumery\n[F] - Farmacy\n [C] Cosmetyc")
        try:
            my_choise = input ('Choise your section: ').upper()
            ['P', 'F', 'C'].index(my_choise)
        except ValueError:
            print('That is not a valid choise')

        else:
            break

    numbers.decorator (my_choise)


def home():

    while True:
        preguntar()
        try:
            other_turn = input ('Do yu want to choose another turn? [Y] [N]: ').upper()
            ['Y', 'N'].index(other_turn)
        except ValueError:
            print('That is not a valid option')
        else:
            if other_turn == 'N':
                print('Thank you for visit us in Python Pharmacy we hope see you soon again.')
                break

home()












