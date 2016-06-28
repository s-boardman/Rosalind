#!/home/sboardman/Projects/Rosalind/venv/bin/python3

import sys

TXT = sys.argv[1]


def even_lines(txt):
    evenlines = []
    with open(txt, 'r') as fin:
        counter = 0
        for line in fin:
            counter += 1
            if counter % 2 == 0:
                evenlines.append(line.rstrip())
            else:
                pass
    return '\n'.join(evenlines)


print(even_lines(TXT))
