# Hangman
#### Description:
An implementation of Hangman using the tkinter module, complete with hangman ASCII art and
a list of guessed alphabets

## Project Overview
An implementation of Hangman with a GUI.


## Project Files
#### ```hangman.py```
Contains the implementation of ```class Hangman```. To play, an instance of ```Hangman```
needs to be created which will create the GUI and logic to play Hangman.
- ```__init__(self)```:  Creates the GUI: the user input and submit buttons, the hangman word and the hangman stage.
- ```def get_occurrences(word: str, letter: str) -> list```:  Goes through the word and returns the indices of its 
   occurrences in a list. For example, ```get_occurrences("hello", "h")``` will return ```[0]```
- ```def update_hangman_text(word: str, letter: str, hangman_word: list) -> list```: Updates the GUI text.
- ```def update_hangman(self)```: Contains the logic that updates the Hangman stage, the GUI, and calls 
 ```update_hangman_text()```
- ```def start_game(self)```: Generates the starting dashes for the GUI
- ```def game_over(self, color: str)```: Updates the GUI background color
- ```def generate_random_word() -> str```: Generates a random word from ```ANIMALS``` in ```hangman_stages.py```.

To modify the words generated, consider changing the list of ```ANIMALS``` in ```hangman_stages.py```,
alternatively, you can modify ```generate_random_word()``` in class ```Hangman``` to get random words from MIT's 
wordlist as follows-
  ```python
import requests
import random

class Hangman:
  ...
  @staticmethod
  def generate_random_word():
      response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000", timeout=10)
      words = response.content.splitlines()

      word = random.choice(words)
      return word.decode('ascii')
  ...
    
  ```


## How do I get started?
- Clone the repository
- Run ```hangman.py``` to play Hangman


## How do I clone the repository?
Run the following command-
```
git clone https://github.com/agentblack-6000/hangman.git
```

## Credits and Authors
Created by [agentblack-6000](https://github.com/agentblack-6000)

The project would not have been possible without these libraries-
- tkinter
