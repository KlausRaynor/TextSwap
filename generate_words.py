import random


def get_keywords():
    keyword_list = []
    # noinspection SpellCheckingInspection
    full_word_list = []
    with open('wordlist/mit_wordlist.txt', 'r') as f:
        for word in f:
            word = word.strip()
            if len(word) == 6:
                full_word_list.append(word)

    # grab random word to serve as key word for 2 additional words
    key_word = random.choice(full_word_list)
    # get 2 random numerical indexes based on length of keyword
    kw_index_one = random.randint(0, len(key_word) - 1)
    kw_index_two = kw_index_one
    # Set indexes to each other. ensure they aren't equal w/while statement
    while kw_index_two == kw_index_one:
        kw_index_two = random.randint(0, len(key_word) - 1)
    # create dictionary of index and char pairs
    # use these to grab words with equivalent index: char pairs
    kw = {kw_index_one: key_word[kw_index_one],
          kw_index_two: key_word[kw_index_two]}

    # create list of keys
    keys = list(kw.keys())
    # create 2 lists. 1 with all words with same char as first index
    # second with all words with same char as second index
    first_index_list = []
    second_index_list = []
    for word in full_word_list:
        if word[keys[0]] == key_word[keys[0]]:
            first_index_list.append(word)
        elif word[keys[1]] == key_word[keys[1]]:
            second_index_list.append(word)

    # grab 2 more random words from word list
    kw_two = random.choice(first_index_list)
    kw_three = random.choice(second_index_list)

    keyword_list.extend([key_word, kw_two, kw_three])

    # select 3 more random words. Add all words to keyword_list
    for x in range(3):
        word_choice = random.choice(full_word_list)
        if word_choice not in keyword_list:
            keyword_list.append(random.choice(full_word_list))
    print(keyword_list)
    return keyword_list


def get_letters(word_list):
    letters = []
    for word in word_list:
        for letter in word:
            letters.append(letter)

    return letters


def group_letters(word_list):
    # groups is a dictionary with a key of index and a value = set of letters found at that index.
    groups = {}
    group_list = []
    for n, word in enumerate(word_list):
        group_list.append(word[n])
        groups[n] = group_list
    print(groups)
        # for n, letter in enumerate(word):
        #     groups[n]: letter
