"""
An implementation of Hangman using the tkinter module, complete with hangman ASCII art and
a list of guessed alphabets
"""
import random
from tkinter import Tk, Label, Entry, Button
from hangman_stages import HANGMAN_STAGES, ANIMALS

BACKGROUND_COLOR = "#144272"
DEFEAT = "#ff0000"
VICTORY = "#00ff00"


class Hangman:
    """
    An implementation of Hangman with a GUI interface.
    """
    def __init__(self):
        """
        Sets up the GUI interface to play Hangman.
        """

        # Creates the main game window
        self.root = Tk()
        self.root.title("Hangman")
        self.root.minsize(width=500, height=600)
        self.root.config(background=BACKGROUND_COLOR)

        # Dummy widget to help grid positioning
        self.dummy_widget = Label(background=BACKGROUND_COLOR, padx=250)
        self.dummy_widget.grid(column=1, row=1)

        # The entry field to accept guesses from the user
        self.guess_input = Entry(width=3, font=("Arial", 25, "normal"))
        self.guess_input.config(background="#0A2647", highlightthickness=0, borderwidth=0)
        self.guess_input.grid(column=1, row=3)

        # The submit button to submit the guesses in the entry
        self.submit_button = Button(text="Guess", command=self.update_hangman, highlightthickness=0,
                                    font=("Helvetica", 20, "bold"), borderwidth=0,
                                    width=6, height=2)
        self.submit_button.config(fg="#0A2647")
        self.submit_button.grid(column=1, row=4, pady=20)

        # The guesses array to display underneath the submit button
        self.guesses = []

        # Keep track of tries to update HANGMAN_STAGES
        self.tries = 0

        self.word = ""
        self.hangman_word = []

        self.guessed_font = ("Arial", 20, "normal")

        # The guessed letters
        self.guessed = Label(text="  ".join(self.guesses),
                             background=BACKGROUND_COLOR, font=self.guessed_font)
        self.guessed.grid(column=1, row=5, pady=15)

        # The hangman text, i.e. the alphabets and the dashes
        self.hangman = Label(text="---", font=("Arial", 50, "normal"))
        self.hangman.config(background=BACKGROUND_COLOR)
        self.hangman.grid(column=1, row=6)

        # The hangman stages
        self.hangman_stage = Label(text="", font=("Arial", 50, "normal"))
        self.hangman_stage.config(background=BACKGROUND_COLOR)
        self.hangman_stage.grid(column=1, row=7)

        # Setup random word, and configure dashes
        self.word = Hangman.generate_random_word()
        self.start_game()
        self.root.mainloop()

    @staticmethod
    def generate_random_word() -> str:
        """
        Returns a random word.

        :returns: The random word
        :rtype: str
        """

        # Pick a random word from ANIMALS
        word = random.choice(ANIMALS)
        return word

    @staticmethod
    def get_occurrences(word: str, letter: str) -> list:
        """
        Goes through the word and returns the indices of its occurrences in a list.

        :param word: the word to get occurrences in
        :type word: str
        :param letter: what to check the word against
        :type letter: str
        :returns: list containing the indices of all the occurrences of the letter
        in the word passed, or [-1]
        :rtype: list
        """
        # Convert everything to lower case
        letter = letter.lower()
        word = word.lower()

        # Array to store list indices of the occurrences
        occurrences = []

        # The index to append to the array incase an occurrence is found
        char_index = 0

        if letter in word:
            letters = list(word)
            # Goes through each letter, and appends index of occurrence to occurrences
            for char in letters:
                if char == letter:
                    occurrences.append(char_index)
                char_index += 1

            # Returns the occurrences array
            return occurrences

        # Incase no occurrences are found, return -1
        return [-1]

    @staticmethod
    def update_hangman_text(word: str, letter: str, hangman_word: list) -> list:
        """
        Updates the GUI by replacing each '__' in the word with the letter passed in after finding
        its occurrences.

        :param word: the word to update occurrences in
        :type word: str
        :param letter: the letter to find occurrences and update the list
        :type letter: str
        :param hangman_word: List of '__' and alphabets of the word to update the occurrences
        of 'letter' in
        :type hangman_word: list
        :returns: the updated list to display in the GUI
        :rtype: list
        """

        # Gets the occurrences of the letter in word
        occurrences = Hangman.get_occurrences(word, letter)

        # Updates the hangman_word by replacing appropriate indices
        for occurrence in occurrences:
            hangman_word[occurrence] = letter.upper()

        # Returns the updated list
        return hangman_word

    def update_hangman(self):
        """
        Updates the guesses array to reflect guesses, the hangman stage,
        as well as the hangman text.
        """
        # Converts guess to lower case
        text = self.guess_input.get().lower()

        # Checks if letter is one character and is an alphabet
        if not text.isalpha() or len(text) > 1:
            pass
        elif text in self.word:
            # Updates the displayed text
            new_hangman_text = self.update_hangman_text(self.word, text, self.hangman_word)
            self.hangman.config(text=" ".join(new_hangman_text))

            # Checks for game over
            if "__" not in self.hangman_word:
                self.game_over(VICTORY)
        else:
            # Updates the hangman stage as letter is not in word
            self.tries += 1
            self.hangman_stage.config(text=HANGMAN_STAGES[self.tries - 1])

            # Checks for defeat, otherwise updates guesses
            if self.tries >= len(HANGMAN_STAGES):
                self.game_over(DEFEAT)
            else:
                self.guesses.append(text)
                self.guessed = Label(text="  ".join(sorted(self.guesses)),
                                     background=BACKGROUND_COLOR, font=self.guessed_font)
                self.guessed.grid(column=1, row=5)

    def start_game(self):
        """Starts game generating the dashes ('__') and updating the GUI."""

        # Generates the starting __ in the hangman word
        for _ in self.word:
            self.hangman_word.append("__")

        # Updates the GUI
        self.hangman.config(text=" ".join(self.hangman_word))

    def game_over(self, color: str):
        """
        Colors the GUI according to the color passed, and then destroys input and submit.

        :param color: A string containing an RGB code or a color
        :type color: str
        """

        # Update the GUI background and reveal answer
        self.hangman.config(text=" ".join(self.word.upper()))
        self.root.config(background=color)
        self.hangman.config(background=color)
        self.hangman_stage.config(background=color)
        self.dummy_widget.config(background=color)
        self.submit_button.config(background=color)
        self.guessed.config(background=color)
        self.guess_input.config(background=color)

        # Destroy input and submit
        self.guess_input.destroy()
        self.submit_button.destroy()


hangman = Hangman()
