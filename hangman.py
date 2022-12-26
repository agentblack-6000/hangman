import random
import requests

from tkinter import *
from hangman_stages import HANGMAN_STAGES

WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"
BACKGROUND_COLOR = "#144272"
DEFEAT = "#ff0000"


class Hangman:
    """
    An implementation of Hangman with a GUI interface
    """
    def __init__(self):
        """
        Sets up the GUI interface to play Hangman
        """

        self.root = Tk()
        self.root.title("Hangman")
        self.root.minsize(width=500, height=600)
        self.root.config(background=BACKGROUND_COLOR)

        self.dummy_widget = Label(background=BACKGROUND_COLOR, padx=250)
        self.dummy_widget.grid(column=1, row=1)

        self.guess_input = Entry(width=3, font=("Arial", 25, "normal"))
        self.guess_input.config(background="#0A2647", highlightthickness=0, borderwidth=0)
        self.guess_input.grid(column=1, row=3)

        self.submit_button = Button(text="Guess", command=self.update_hangman, highlightthickness=0,
                                    font=("Helvetica", 20, "bold"), borderwidth=0, width=6, height=2)
        self.submit_button.config(fg="#0A2647")
        self.submit_button.grid(column=1, row=4, pady=20)

        self.guesses = []
        self.tries = 0
        self.word = ""
        self.hangman_word = []

        self.guessed_font = ("Arial", 20, "normal")
        self.guessed = Label(text="  ".join(self.guesses), background=BACKGROUND_COLOR, font=self.guessed_font)
        self.guessed.grid(column=1, row=5, pady=15)

        self.hangman = Label(text="---", font=("Arial", 50, "normal"))
        self.hangman.config(background=BACKGROUND_COLOR)
        self.hangman.grid(column=1, row=6)

        self.hangman_stage = Label(text="", font=("Arial", 50, "normal"))
        self.hangman_stage.config(background=BACKGROUND_COLOR)
        self.hangman_stage.grid(column=1, row=7)

        self.start_game()
        self.root.mainloop()

    def update_hangman(self):
        """
        Updates the guesses array displayed
        """
        text = self.guess_input.get().lower()

        if not text.isalpha() or len(text) > 1:
            pass
        elif text in self.word:
            occurrence = self.get_occurrences(text)
            for occurrence in occurrence:
                self.hangman_word[occurrence] = text.upper()

            self.hangman.config(text=" ".join(self.hangman_word))

            if "__" not in self.hangman_word:
                self.root.destroy()

        else:
            self.tries += 1
            self.hangman_stage.config(text=HANGMAN_STAGES[self.tries - 1])

            if self.tries >= len(HANGMAN_STAGES):
                self.hangman.config(text=" ".join(self.word.upper()))
                self.root.config(background=DEFEAT)
                self.hangman.config(background=DEFEAT)
                self.hangman_stage.config(background=DEFEAT)
                self.dummy_widget.config(background=DEFEAT)
                self.submit_button.config(background=DEFEAT)
                self.guessed.config(background=DEFEAT)
                self.guess_input.config(background=DEFEAT)

                self.guess_input.destroy()
                self.submit_button.destroy()
            else:
                self.guesses.append(text)
                self.guessed = Label(text="  ".join(sorted(self.guesses)), background=BACKGROUND_COLOR,
                                     font=self.guessed_font)
                self.guessed.grid(column=1, row=5)

    def generate_random_word(self) -> str:
        """
        Generates a random word based on a random difficulty.

        :returns: The random word generated
        :rtype: str
        """

        response = requests.get(WORD_SITE, timeout=10)
        words = response.content.splitlines()

        word = random.choice(words).decode('ASCII')
        while len(word) <= 4 or len(word) > 7:
            word = random.choice(words).decode('ASCII')

        self.word = word
        return word

    def get_occurrences(self, letter: str) -> list:
        """
        Goes through the word and returns the indices of its occurrences in a list

        :param letter: what to check the word against
        :type letter: str
        :returns: list containing the indices of all the occurrences of the letter in the word passed, or [-1]
        :rtype: list
        """
        letter = letter.lower()
        word = self.word.lower()
        occurrences = []
        char_index = 0

        if letter in word:
            letters = list(word)
            for char in letters:
                if char == letter:
                    occurrences.append(char_index)
                char_index += 1

            return occurrences

        return [-1]

    def start_game(self):
        """Starts game by setting word and printing dashes"""
        self.generate_random_word()
        for _ in self.word:
            self.hangman_word.append("__")

        self.hangman.config(text=" ".join(self.hangman_word))


hangman = Hangman()
