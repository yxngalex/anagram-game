import json
import random


class Anagram:
    def __init__(self, question, hint, answer):
        self._question = question
        self._hint = hint
        self._answer = answer

    def __repr__(self):
        return "{},\n{}".format(self._question, self._hint)


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


def anagram(length=5):
    data = json.load(open('anagram/data/dictionary.json'))

    while True:
        word = pick_word(data, length)
        question = shuffle(word)
        hint = data[word]

        question = question.lower()

        return Anagram(question, hint, word)
