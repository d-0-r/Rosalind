#!/usr/bin/python

inp = open("rosalind_ini6.txt", "r").read().strip('\n')
out = "sol.txt"

def word_counter(i, o):
    '''
    Takes a string of text and writes out to a file each word
    in the text and the number of occurences of that word
    Eg) Deoxyribose 8
    '''
    words = i.split(" ")
    hashmap = {word: words.count(word) for word in words}
    output = open(o, 'w')
    for pair in hashmap.items():
        output.write(pair[0] + " " + str(pair[1]) + '\n')
    output.close()

word_counter(inp, out)
