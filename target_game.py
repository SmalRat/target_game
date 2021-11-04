"""
Module of game about making words
"""
from typing import List
import random


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = []
    for i in range(3):
        grid.append([])
        for j in range(3):
            grid[i].append(chr(random.randint(65, 90)))
    return grid


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    print(letters)
    good_words = []
    main_letter = letters[4]
    with open(f, "r", encoding="utf-8") as dictionary:
        lines = dictionary.readlines()
        for i in range(3, len(lines)):
            lines[i] = lines[i].lower().strip()
            if (main_letter in lines[i]) and len(lines[i]) >= 4:
                check = 1
                for letter in lines[i]:
                    if (letter not in letters) or lines[i].count(letter) > letters.count(letter):
                        check = 0
                if check == 1:
                    good_words.append(lines[i])
    return good_words


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
letters_init = generate_grid()
letters_end = []
for i in range(3):
    letters_end += letters_init[i]
for i, letter in enumerate(letters_end):
    letters_end[i] = letter.lower()
print(letters_end)
print(get_words("en.txt", [el for el in 'jniarnoah']))
