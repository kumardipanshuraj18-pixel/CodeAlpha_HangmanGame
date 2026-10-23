import random

def play_hangman():
    words = ["python", "computer", "program", "coding", "developer"]
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("=" * 35)
    print("       WELCOME TO HANGMAN")
    print("=" * 35)
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses available.\n")

    while incorrect_guesses < max_attempts:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Incorrect guesses:", incorrect_guesses)
        print("Guesses remaining:", max_attempts - incorrect_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

    else:
        print("Game over! The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()