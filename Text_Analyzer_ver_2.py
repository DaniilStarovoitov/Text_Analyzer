"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Daniil Starovoitov
email: daniil.s@seznam.cz
discord: Sweet Procrastination#6256
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

if __name__ == "__main__":

    registrated_users = {
        'bob':'123',
        'ann':'pass123',
        'mike':'password123',
        'liz':'pass123'}

    user = input('username: ')

    if user not in registrated_users:
        print('unregistered user, terminating the program..')
        quit()
    else:
        password = input('password: ')
        p = registrated_users.get(user)
        if password != p:
            print('wrong password, terminating the program..')
            quit()
        else:
            print(f'----------------------------------------')
            print(f'Welcome to the app, {user}')
            print(f'We have 3 texts to be analyzed.')
            print(f'-----------------------------------------')

    search = input('Enter a number btw. 1 and 3 to select: ')

    if search == '1':
        text = TEXTS[0]
    elif search == '2':
        text = TEXTS[1]
    elif search == '3':
        text = TEXTS[2]
    else:
        print('You can only choose text 1, 2 or 3')
        quit()

    words = text.split()

    length = len(words)

    titlecase = len([word for word in words if word[0].isupper()])

    upper = len([word for word in words if word.isupper()])

    num = [int(word) for word in words if word.isdigit()]

    len_num = len(num)

    lower = len([word for word in words if word.islower()])

    sum = 0
    for count in (num):
        sum += count


    print(f'There are {length} words in the selected text.')
    print(f'There are {titlecase} titlecase words.')
    print(f'There are {upper} uppercase words.')
    print(f'There are {lower} lowercase words.')
    print(f'There are {len_num} numeric strings.')
    print(f'The sum of all the numbers {sum}')
    print('----------------------------------------')


    dictionary = {}

    for word in words:
        word = word.rstrip(',.')
        if len(word) in dictionary:
            dictionary[len(word)] = dictionary[len(word)] + 1
        else:
            dictionary[len(word)] = 1

    for i in sorted(dictionary):
        st = dictionary[i] * '*'
        print(f'{i:2}|{st:20}|{dictionary[i]}')