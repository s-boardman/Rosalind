#!/home/sboardman/Projects/Rosalind/venv/bin/python3


def odd_sum(a, b):
    c = [n for n in range(a, b) if n % 2 != 0]
    print(sum(c))

odd_sum(100, 200)
