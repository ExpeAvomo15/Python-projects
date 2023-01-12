
def perfumery_numbers():
    for n in range(1,10000):
        yield f'P-{n}'

def farmacy_numbers():
    for n in range(1,10000):
        yield f'F-{n}'

def cosmetics_numbers():
    for n in range(1,10000):
        yield f'C-{n}'

p=perfumery_numbers()
f=farmacy_numbers()
c=cosmetics_numbers()

def decorator(section):
    print('\n' + '*' * 23)
    print('Your number is: ')

    if section == 'p':
        print(next(p))

    elif section == 'f':
        print(next(f))

    else:
        print(next(c))

    print('Please, wait and you will be atended')
    print('*'*23 +'\n')











































