import random

# Word list with hints
words_with_hints = {
    "python": "A popular programming language",
    "computer": "An electronic machine for processing data",
    "hangman": "A classic word guessing game",
    "internet": "A global network for communication",
    "keyboard": "An input device used for typing"
}

word = random.choice(list(words_with_hints.keys()))
hint = words_with_hints[word]

guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("💡 Hint:", hint)

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Remaining attempts:", attempts)
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ Letter already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
