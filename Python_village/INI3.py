#!/home/sboardman/Projects/Rosalind/venv/bin/python3


def slicer(sentence, sta, spa, stb, spb):
    a = sentence[sta:(spa+1)]
    b = sentence[stb:(spb+1)]
    print(a, b)

seq = "ugWHxuvrH6u5BW3R4vGaviaY5w2aSFFexEWRU8jJ97FzTLw4Dp7GnboQnBPoe6CBWEItSyhUpYWG7mAHTZMR3Bcasualis4n6qzUSoesHUw9Ekd9oDGje1yUZxGRd731dEv0DW84hy0rDSI4pkoWh0pi1DzrjmjPoUxp6KBFCUEdexGZ0C4I."

slicer(seq, 18, 22, 86, 93)
