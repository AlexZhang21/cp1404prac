"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 8 minutes
Actual:   10 minutes
"""


def word_count():
    text = input("Enter a string: ")
    words = text.split()
    word_counts = {}

    #for each word
    for word in words:
        #existed, add 1
        if word in word_counts:
            word_counts[word] += 1
        #new word, insert
        else:
            word_counts[word] = 1

    #get the length of longest word
    longest_word_length = max(len(word) for word in word_counts.keys())

    for word, count in sorted(word_counts.items()):
        print(f"{word:{longest_word_length}} : {count}")

word_count()