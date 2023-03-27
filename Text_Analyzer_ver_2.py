"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Daniil Starovoitov
email: daniil.s@seznam.cz
discord: Scorched_Earth#6256
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

import re

if __name__ == "__main__":

    separator = 40 * '-'

    # dictionary of registered users and their passwords
    registrated_users = {
        'bob':'123',
        'ann':'pass123',
        'mike':'password123',
        'liz':'pass123'}

    # get user input for username
    user = input('username: ')

    # check if the user is registered
    if user not in registrated_users:
        print('unregistered user, terminating the program..')
        quit()
    else:
        # get user input for password and check if it matches
        password = input('password: ')
        p = registrated_users.get(user)
        if password != p:
            print('wrong password, terminating the program..')
            quit()
        else:
            # welcome message
            print(separator)
            print(f'Welcome to the app, {user}')
            print(f'We have 3 texts to be analyzed.')
            print(separator)

    # get user input for which text to analyze
    search = int(input('Enter a number btw. 1 and 3 to select: '))

    # select the corresponding text
    index = search - 1

    if index < len(TEXTS) - 1:
        text = TEXTS[index]
    else:
        print('You can only choose text 1, 2 or 3')
        quit()

    # analyze the text and count various features
    words = re.sub(r'[^\w\s]', '', text).split()

    length = len(words)

    titlecase = len([word for word in words if word.istitle()])

    upper = len([word for word in words if word.isupper()])

    num = [int(word) for word in words if word.isdigit()]

    len_num = len(num)

    lower = len([word for word in words if word.islower()])

    sum = 0
    for count in (num):
        sum += count

    # print the results
    print(f'There are {length} words in the selected text.')
    print(f'There are {titlecase} titlecase words.')
    print(f'There are {upper} uppercase words.')
    print(f'There are {lower} lowercase words.')
    print(f'There are {len_num} numeric strings.')
    print(f'The sum of all the numbers {sum}')
    print(separator)

    # create a dictionary of word length and their occurrence
    dictionary = {}

    for word in words:
        if len(word) in dictionary:
            dictionary[len(word)] = dictionary[len(word)] + 1
        else:
            dictionary[len(word)] = 1

    # print the histogram
    text_one = 'LEN'
    text_two = 'OCCURENCES'
    text_three = 'NR.'

    print(f'{text_one:3}|{text_two:20}|{text_three}')
    print(separator)
    for i in sorted(dictionary):
        st = dictionary[i] * '*'
        print(f'{i:3}|{st:20}|{dictionary[i]}')
