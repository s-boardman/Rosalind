#!/home/sboardman/Projects/Rosalind/venv/bin/python3

import sys

TXT = sys.argv[1]


def word_dict_counter(txt):
    word_dict = {}
    with open(txt, 'r') as fin:
        for line in fin:
            for word in line.split():
                if word in word_dict:
                    word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1
    return word_dict


for k, v in word_dict_counter(TXT).items():
    print(k, v)
