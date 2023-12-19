import random
import requests

WORD_LENGTH = random.randint(4,6)

word_lists = [
    "mit_",
    "umich_"
]

# noinspection SpellCheckingInspection

"""
get_keywords pulls a random 6 letter word from one of the dictionaries. 
compares them with dictionary API to validate and ensure they're relatively common
"""


# noinspection SpellCheckingInspection
def get_keywords():
    chosen_list = random.choice(word_lists)
    print("chosen word list: ", chosen_list)
    addtl_words = []
    # noinspection SpellCheckingInspection
    full_word_list = []
    with open('assets/wordlist/' + chosen_list + 'wordlist.txt', 'r') as f:
        for word in f:
            word = word.strip()
            if len(word) == WORD_LENGTH:
                full_word_list.append(word)
    verified_word_list = []

    # grab random word to serve as key word for 2 additional words
    # validate word and add to verified word list
    while True:
        key_word = random.choice(full_word_list)
        # validate word is in common dictionary
        validation = validate_word(key_word)
        if validation:
            verified_word_list.append(key_word)
            break

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

    # create list of keys (indexes for kw)
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

    # validate and assign 2 more random words from word list
    while True:
        kw_two = random.choice(first_index_list)
        kw_three = random.choice(second_index_list)
        if kw_two == key_word or kw_three == key_word:
            continue
        val_two = validate_word(kw_two)
        if val_two:
            kw_three = random.choice(second_index_list)
            val_three = validate_word(kw_three)
            if val_three:
                verified_word_list.extend([kw_two, kw_three])
                break
            else:
                continue
        else:
            continue

    addtl_words.extend([key_word, kw_two, kw_three])
    # select 3 more random words. Validate and add all words to additional_words
    for x in range(3):
        while True:
            rand_word = random.choice(full_word_list)
            val_word = validate_word(rand_word)
            if val_word and rand_word not in addtl_words:
                verified_word_list.append(rand_word)
                break
            else:
                continue

    return verified_word_list


def get_letters(word_list):
    letters = []
    for word in word_list:
        for letter in word:
            letters.append(letter)

    return letters


def create_sets(word_list):
    # groups is a dictionary with a key of index and a value = set of letters found at that index.
    groups = {}
    i = 0
    while i < len(word_list[0]):
        group_list = [word[i] for word in word_list]
        groups[i] = set(group_list)
        i += 1

    return groups


def validate_word(word):
    # check key_word validity against API
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)
    # extract JSON data
    response_ans = response.json()
    # verify it's in common dictionary, otherwise search for new word
    try:
        if response_ans[0]["word"]:
            return True
    except Exception as e:
        if response_ans["title"] == "No Definitions Found":
            print(e)
            return False
