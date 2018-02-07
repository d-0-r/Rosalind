#!/usr/bin/python3

from itertools import product

input_string = open('rosalind_lexf.txt', 'r').read().replace(' ', '').replace('\n', '')

letters = input_string[:-1] if input_string[-2:] != '10' else input_string[:-2]
repeat = int(input_string[-1:]) if input_string[-2:] != '10' else int(input_string[-2:])

groups = product(letters, repeat=repeat)

for group in groups:
    print(str(group).strip('(),').replace('\'', '').replace(', ', ''))
