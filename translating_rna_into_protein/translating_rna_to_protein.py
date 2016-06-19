#!/usr/bin/python3

rna = open("rosalind_prot.txt", 'r').read().upper()

codon_dict = {
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': "AUG",
    'V': ['GUU', 'GUA', 'GUC', 'GUG'],
    'S': ['UCU', 'UCA', 'UCG', 'UCC', 'AGU', 'AGC'],
    'P': ['CCU', 'CCG', 'CCC', 'CCA'],
    'T': ['ACU', 'ACG', 'ACC', 'ACA'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'],
    'H': ['CAU', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAG', 'GAA'],
    'C': ['UGU', 'UGC'],
    'W': "UGG",
    'R': ['CGA', 'CGU', 'CGG', 'CGC', 'AGA', 'AGG'],
    'G': ['GGU', 'GGA', 'GGG', 'GGC'],
    #'STOP': ['UGA', 'UAA', 'UAG']
}

def translate(hash, seq):
    """
    Takes a dictionary of codons and an RNA string as an arguments
    returns a string of a translated RNA strand aka a Protein
    """
    protein = ""
    for idx in range(0,len(seq),3):
        for key in hash.keys():
            if seq[idx:idx+3] in hash[key]:
                protein += key
    return protein

print(translate(codon_dict, rna))
