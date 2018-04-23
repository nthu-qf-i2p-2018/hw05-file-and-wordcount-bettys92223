
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import sys
import csv
import json
import pickle
import string
from collections import Counter


def main(filename):
    # read file into lines
    lines = open("i_have_a_dream.txt").readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words = line.split()

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            for p in string.punctuation:
                word = word.replace(p, "")
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)
    # print(counter)
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...

    csv_filename = "wordcount.csv"
    print(csv_filename)
    with open(csv_filename, "w") as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file)
                # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        
        # writer.writerows(counter)
        for key, value in counter.items():
            writer.writerow([key, value])


    
    # # dump to a json file named "wordcount.json"
    # ...
    json_filename = "wordcount.json"
    with open(json_filename, "w") as json_file:
        json.dump(counter,json_file)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    pickle_filename = "wordcount.pkl"
    with open(pickle_filename, "wb") as pkl_file:
        pickle.dump(counter,pkl_file)

    # test to load pickle
    # with open(pickle_filename, "rb") as pkl_file:
    #     content = pickle.load(pkl_file)
    #     print(content)
if __name__ == '__main__':
#     main("i_have_a_dream.txt")
    main(sys.argv[1])

