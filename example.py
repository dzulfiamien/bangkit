from scripts.hello import print_hello
from scripts.hello import filter_only_word

# print_hello()
import os
import sys
filename = sys.argv[1]

if not os.path.exists(filename):
    print("file not found")
    raise Exception("EXCEPTION!! file not found")

else:
    print("file is found, start to process files")
    lines = []
    with open('text.txt', 'r') as f:
        lines = f.readlines()

    words = []
    for l in lines:
        # words.append(l.split(' '))
        words += l.split(' ')

    lower_words = []
    for w in words:
        lower_words.append(w.lower())

    filtered_words = []
    for lw in lower_words:
        filter_result = filter_only_word(lw)
        if filter_result:
            filtered_words.append(filter_result)

    import collections
    collection = collections.Counter(filtered_words)
    collection = collection.most_common()

    for c in collection:
        with open('word_count.txt', 'a') as f:
            f.write("{}, {}\n".format(c[0], c[1]))