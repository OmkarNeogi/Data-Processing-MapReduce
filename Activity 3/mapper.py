import csv
import sys
import string

def remPunct(inputArr):
    output = []
    # Do not remove punctuation from the location of the file (the first two or three indices of the array)
    # There are arrow brackets in the "location" indices of the array read as input
    for i in range(0, len(inputArr), 1):
        output.append(inputArr[i].translate(None, string.punctuation))
    return output

def normalize_word(wordArr):
    for i in range(0, len(wordArr), 1):
        wordArr[i] = wordArr[i].lower().replace("j", "i").replace("v", "u")
    return wordArr

csv_file_name = "/Users/omkarneogi/Downloads/new_lemmatizer.csv"
csv_file = []
first_row=True
with open(csv_file_name, 'rb') as csv_file_to_read:
    csv_reader = csv.reader(csv_file_to_read, delimiter=' ', quotechar='|')
    for row in csv_reader:
        if(first_row == True):
            first_row = False
            continue
        else:
            csv_inner_array = row[0]
            arr = csv_inner_array.split(",")
            csv_file.append(arr)

def check_lemmatizer(location, word_to_check):
    for i in range(0, len(csv_file), 1):
        row = csv_file[i]
        first_column_word = row[0]
        if(first_column_word == word_to_check):
            for lemma_iter in range(1, len(row), 1):
                if(row[lemma_iter] != ""):
                    print('%s\t%s' % (row[lemma_iter], location))

    return "done"

dnr = True
words_list = []
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    location = words[0]+words[1]
    del words[0]
    del words[0]
    if('>' in words[0]):
        location = location+words[0]
        del words[0]

    words = remPunct(words)
    words = normalize_word(words)
    for word in words:
        a = check_lemmatizer(location, word)
    words_list.append(words)
