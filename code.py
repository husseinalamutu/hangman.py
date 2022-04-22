# Write your code here
import random

print("H A N G M A N")
words = ["python", "java", "swift", "javascript"]
random.seed()
won = 0
lost = 0

while True:
    menu_selection = ""
    while menu_selection not in ["play", "results", "exit"]:
        menu_selection = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if menu_selection == "exit":
        break
    elif menu_selection == "play":
        word = random.choice(words)
        word_length = len(word)
        hint = ["-"] * word_length
        lives = 8
        previous_guesses = []
        while lives > 0:
            print()
            print("".join(hint))
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("Please, input a single letter.")
                continue
            if not guess.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if guess in previous_guesses:
                print("You've already guessed this letter.")
                continue
            previous_guesses.append(guess)
            if guess in word:
                for i in range(word_length):
                    if word[i] == guess:
                        hint[i] = guess
                if "".join(hint) == word:
                    print(f"\nYou guessed the word {word}!")
                    print("You survived!")
                    if won == 0:
                        won += 1
                    else:
                        won +=0
                    break
            else:
                print("That letter doesn't appear in the word.")
                lives -=1

        if lives == 0:
            print("You lost!")
            if lost == 0:
              lost += 1
            else:
              won += 0
    elif menu_selection == "results":
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times")
