#!/usr/bin/env python3

seq = open("rosalind_dna.txt", 'r').read().lower()

def count_nucleotides(sequence):
    """
    DNA nucleotide counter
    Returns string of counts of Adenine, Cytosine, Thymine, and Guanine
    In that exact order separated by spaces
    """
    a_count = sequence.count("a")
    c_count = sequence.count("c")
    g_count = sequence.count("g")
    t_count = sequence.count("g")
    return "{} {} {} {}".format(a_count, c_count, t_count, g_count)

print(count_nucleotides(seq))
