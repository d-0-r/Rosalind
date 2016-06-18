#!/usr/bin/python3

sequence = open("rosalind_revc.txt", "r").read().upper()

def reverse_complement(seq):
    """returns the reverse complement of a string argument dna sequence"""
    new = ""
    for base in seq:
        if base == 'T':
            new += 'A'
        elif base == 'A':
            new += "T"
        elif base == "C":
            new += "G"
        else:
            new += "C"
    return new[::-1]

print(reverse_complement(sequence))

'''
Alternative Solution using BioPy

from Bio.Seq import Seq

sequence = open("rosalind_revc.txt", "r").read()

seq = Seq(sequence)

print(seq.reverse_complement())
'''
