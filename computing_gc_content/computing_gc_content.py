#!/usr/bin/python3

sequence = open("rosalind_gc.txt", 'r').read()

arr = sequence.split(">")[1:]  # get rid of first empty index

def gc_content(seq):
    """
    Finds GC content of a DNA string.
    Takes DNA string argument.
    Returns a string with FASTA header and GC content
    """
    g_count = seq.count("G")
    c_count = seq.count("C")
    a_count = seq.count("A")
    t_count = seq.count("T")
    return "{}\n{}".format(seq[:13],
                          ((g_count + c_count) / \
                          (g_count + c_count + a_count + t_count))
                          * 100
                          ) # header \n gc percentage

gc_contents = [gc_content(x) for x in arr] # header +  gc_content
gc_contents2 = [float(x[13:]) for x in gc_contents] # just gc_content converted to float
largest = gc_contents2.index(max(gc_contents2)) # index of largest gc_content
print(gc_contents[largest]) # solution
