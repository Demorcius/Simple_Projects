

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
lives = 6

print(f'PSSt, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)


end_of_game = False 

while not end_of_game:
    guess = input("Guess a letter ").lower()

    if guess not in chosen_word:
        print(f"You've made a wrong {guess}")

    if guess in display:
        print("You've already guessed {guess}")  

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{''.join(display)}")
    print(display)


if guess not in chosen_word:
    lives -=1
    if lives == 0:
        end_of_game = True
        print("You lose")
print(f"{' '.join(display)}")

if "_" not in display:
    end_of_game=True
    print("You win")

print(stages[lives])