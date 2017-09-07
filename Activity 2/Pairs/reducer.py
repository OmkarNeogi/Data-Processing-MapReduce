#!/usr/bin/env python

from operator import itemgetter
import sys
import string

current_word = None
word_count_current = 0
word = None


for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        word_count_current += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, word_count_current)
        word_count_current = count
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, word_count_current)
