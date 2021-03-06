#!/bin/python

# Author: Clara~ <3


import argparse
import random

parser = argparse.ArgumentParser()

upper_help = "adds uppercase characters to the password generation"
lower_help = "adds lower characters to the password generation"
numbers_help = "adds numbers to the password generation"
symbols_help = "adds symbols to the password generation"
alphanum_help = "uses alphanumerical characters for the password generation"
all_help = "uses all available sets for the password"
strong_help = "same as -a, --all. Just an alias"

parser.add_argument('-u', '--upper', dest='Upper', required=False, action='store_true', help=upper_help)
parser.add_argument('-l', '--lower', required=False, action='store_true', help=lower_help)
parser.add_argument('-n', '--numbers', required=False, action='store_true', help=numbers_help)
parser.add_argument('-s', '--symbols', required=False, action='store_true', help=symbols_help)
parser.add_argument('-m', '--alnum', required=False, action='store_true', help=alphanum_help)
parser.add_argument('-a', '--all', required=False, action='store_true', help=all_help)
parser.add_argument('-S', '--strong', required=False, action='store_true', help=strong_help)
parser.add_argument('length', nargs='?', default=8, type=int, metavar='password_length')

args = parser.parse_args()
argv = vars(args)
argc = 1 + len([i for i in tuple(vars(args).values()) if i is not False])
flagc = len([i for i in tuple(vars(args).values()) if i is True])


def randomUpper():
    return chr(random.randint(65, 90))


def randomLower():
    return chr(random.randint(97, 122))


def randomNumbers():
    return chr(random.randint(48, 57))


def randomSymbols():
    sets = ((33, 47), (58, 64), (91, 95))   # different consecutive sets of symbols in ascii table
    choice = random.choice(sets)            # choose a random set of symbols
    return chr(random.randint(choice[0], choice[1]))    # return random symbol from set


def main(flagc: int, argv: dict):
    # Quick access: create a strong password by default
    if flagc == 0:
        argv['all'] = True

    length = int(argv['length'])    # saving the legth to a variable

    # Set upper and lower flags if alnum flag is used
    if argv['alnum'] is True:
        argv['upper'] = True
        argv['lower'] = True
        argv['numbers'] = True

    # Set all flags if all or strong flags are used
    if argv['all'] is True or argv['strong'] is True:
        argv = dict.fromkeys(argv, True)    # Sets all keys in the dict to True

    # delete these flags as they do not belong to specific charsets
    del argv['strong']
    del argv['length']
    del argv['alnum']
    del argv['all']

    flags = tuple(filter(argv.get, argv))
    flags = [i.capitalize() for i in flags]

    i = 0
    password = ''
    while i != length:
        password += globals()[f'random{random.choice(flags)}']()
        i += 1

    print(f'Password: {password}')

if __name__ == '__main__':
    main(flagc, argv)      # execute the main function
