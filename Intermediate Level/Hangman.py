import random

# Word list
words = ["python", "computer", "hangman", "internet", "keyboard"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Remaining attempts:", attempts)
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Letter already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over! The word was:", word)