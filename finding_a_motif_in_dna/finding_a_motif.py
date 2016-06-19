#!/usr/bin/python3

seq = open('rosalind_subs.txt', 'r').read().upper()

arr = seq.split('\n')

def find_motif(string, substr):
    """
    Finds the 1-based indices (from the start) of a substring in a DNA string assuming it exists
    Takes two string arguments, first is DNA string, then the substring you're comparing
    Returns the 1-based indices of the start of the substring sequence thats found
    """
    indices = ""
    for idx in range(len(string)):
        if string[idx:idx+len(substr)] == substr:
            indices += "{} ".format(idx+1)
    return indices

print(find_motif(arr[0], arr[1]))
