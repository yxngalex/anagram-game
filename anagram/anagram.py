import json
import random


def pick_word(data, length):
    words = list(data.keys())
    while True:
        word = random.choice(words)
        if length > len(word) > 2:
            return word


def shuffle(word):
    characters = list(word)
    shuffled = word
    while True:
        random.shuffle(characters)
        shuffled = ''.join(characters)
        if shuffled != word:
            return shuffled


def anagram():
    data = json.load(open('anagram/data/dictionary.json'))

    while True:
        word = pick_word(data, 9)
        question = shuffle(word)
        hint = data[word]

        question = question.lower()

        return {question, hint}
