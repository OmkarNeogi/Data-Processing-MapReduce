#!/usr/bin/env python
import sys
import string

for line in sys.stdin:
    line = line.strip()

    wordsArr = line.split(" ")

    counter = 1
    for i in range(0, len(wordsArr), 1):
        for j in range(0, len(wordsArr), 1):
            if(i==j):
                continue
            else:
                word = wordsArr[i]+","+wordsArr[j]
                print('%s\t%s' % (word, "1"))
