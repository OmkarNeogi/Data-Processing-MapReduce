#!/usr/bin/env python

from operator import itemgetter
import sys

current_lemma = None
old_lemma = None

locations_list_for_a_lemma = []
first_time = True
for line in sys.stdin:
    line = line.strip()
    current_lemma, location = line.split("\t")
    # print("sadf "+location)
    #
    # # if(current_lemma == old_lemma):
    # #     print("here")
    # #     locations_list_for_a_lemma.append(location)
    # # else:
    # #     if (first_time == True):
    # #         first_time = False
    # #         locations_list_for_a_lemma = []
    # #         old_lemma = current_lemma
    # #     else:
    # #         print("%s\t%s" % (old_lemma, locations_list_for_a_lemma))
    # #         locations_list_for_a_lemma = []
    # #         locations_list_for_a_lemma.append(location)
    # #         old_lemma = current_lemma
    #
    # if(current_lemma != old_lemma):
    #     print("%s\t%s" % (current_lemma, locations_list_for_a_lemma))
    #     locations_list_for_a_lemma = []
    #     locations_list_for_a_lemma.append(location)
    #     old_lemma = current_lemma
    # else:
    #     if(first_time == True):
    #         first_time = False
    #         locations_list_for_a_lemma.append(location)
    #         old_lemma = current_lemma
    #     else:
    #         locations_list_for_a_lemma.append(location)
    if(first_time == True):
        first_time = False
        locations_list_for_a_lemma.append(location)
        old_lemma = current_lemma
    else:
        if(current_lemma == old_lemma):
            locations_list_for_a_lemma.append(location)
        else:
            print("%s\t%s" % (old_lemma, locations_list_for_a_lemma))
            locations_list_for_a_lemma = []
            locations_list_for_a_lemma.append(location)
            old_lemma = current_lemma
print("%s\t%s" % (old_lemma, locations_list_for_a_lemma))
