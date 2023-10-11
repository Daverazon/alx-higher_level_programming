#!/usr/bin/python3
'''Text printing function'''


def text_indentation(text):
    '''prints a text with 2 new lines after
    each of these characters: ., ? and :'''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for letter in text:
            print(letter, end='')
            for sign in ['.', '?', ':']:
                if letter == sign:
                    print('')
                    print('')
