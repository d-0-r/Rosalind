#!/usr/bin/env python3

from os import system

seq = open("rosalind_rna.txt", 'r').read().upper()

def transcribe(sequence):
    """Returns a string of a transcribed DNA Sequence aka RNA"""
    return sequence.replace("T", "U")

print(transcribe(seq))

system("python3 transcribing_DNA_into_RNA.py > solution.txt")
