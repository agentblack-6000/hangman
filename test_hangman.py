"""
Unit tests for methods implemented in class Hangman
"""
from hangman import Hangman
from hangman_stages import ANIMALS


def test_get_occurrences():
    """Tests the get_occurrences() method in class Hangman"""
    test_hangman = Hangman()

    test_hangman.word = "hello"
    assert test_hangman.get_occurrences(test_hangman.word, "h") == [0]
    assert test_hangman.get_occurrences(test_hangman.word, "e") == [1]
    assert test_hangman.get_occurrences(test_hangman.word, "l") == [2, 3]

    test_hangman.word = "assassination"
    assert test_hangman.get_occurrences(test_hangman.word, "a") == [0, 3, 8]
    assert test_hangman.get_occurrences(test_hangman.word, "s") == [1, 2, 4, 5]


def test_random_word():
    """Tests the generate_random_word() method in class Hangman"""
    test_hangman = Hangman()
    assert test_hangman.generate_random_word() in ANIMALS


def test_update_hangman_text():
    """Tests the update_hangman_text() method in class Hangman"""
    word = "koala"
    letter = "l"
    hangman_word = ["__", "__", "__", "__", "__"]
    assert Hangman.update_hangman_text(word, letter, hangman_word) == ["__", "__", "__", "L", "__"]

    letter = "k"
    assert Hangman.update_hangman_text(word, letter, hangman_word) == ["K", "__", "__", "L", "__"]
