#!/usr/bin/env python3

dna_input = open('rosalind_hamm.txt', 'r').read().upper()

input_strands = dna_input.split('\n')

def count_point_mutations(first, second):
    '''
    Counts the amount of point mutations between 2 DNA string arguments
    Returns int-type amount of point mutations through hamming distance calculation
    '''
    mutation_count = 0
    for idx in range(len(first)):  # we're assuming no insertions/deletions, equal lengthed strands
        if first[idx] != second[idx]:
            mutation_count += 1
    return mutation_count

print(count_point_mutations(input_strands[0], input_strands[1]))
