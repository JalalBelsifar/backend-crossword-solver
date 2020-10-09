#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Jalal, help from Rachida"
import re
# YOUR HELPER FUNCTION GOES HERE


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
    test_word = input(
        '''Please enter a word to solve.
        \nUse spaces to signify unknown letters: ''').lower()

    # YOUR ADDITIONAL CODE HERE
    test_word = test_word.replace(" ", ".")
    matches = re.compile(test_word)
    exact_length = [word for word in words if matches.match(
        word) and len(word) == len(test_word)]
    print(exact_length)
    for word in exact_length:
        print(word)


if __name__ == '__main__':
    main()
