#!/usr/bin/python3

q = open('sol.txt', 'w')

with open("rosalind_ini5.txt", "r") as f:
    counter = 0
    for line in f:
        if counter % 2 != 0:
            q.write(line.lstrip())
        counter += 1

q.close()
