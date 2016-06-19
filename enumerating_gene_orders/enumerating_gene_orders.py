#!/usr/bin/python3

from itertools import permutations

upper_bound = int(open("rosalind_perm.txt", 'r').read().strip())
permutations_list = permutations(range(1, upper_bound+1))

counter = 0

for perm in permutations_list:
    print(str(perm).strip("()").replace(",", ""))
    counter += 1

print(counter)
