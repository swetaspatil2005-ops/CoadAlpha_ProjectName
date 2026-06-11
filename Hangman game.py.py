import random
import time
import pyttsx3
import sys

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

words = ("apple", "banana", "pineapple", "mango")

hangman_art = {
    0: (
        "   ",
        "   ",
        "   "
    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}

TIME_LIMIT = 60

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():

    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    start_time = time.time()

    speak("Welcome to Hangman Game")

    while True:

        elapsed_time = int(time.time() - start_time)
        remaining_time = TIME_LIMIT - elapsed_time

        if remaining_time <= 0:
            print("\nTime Over!")
            print("Answer was:", answer)
            speak("Game Over! Time is over. You lose in Hangman Game!")
            break

        print(f"\nTime Left: {remaining_time} seconds")

        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            speak("Invalid Input")
            continue

        if guess in guessed_letters:
            print("Already Guessed")
            speak("Already Guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            speak("Correct Guess")

            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1
            speak("Wrong Guess")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)

            print("\n🎉 YOU WIN! 🎉\n")
            speak("YOU WIN!")

            for i in range(25):
                sys.stdout.write(
                    "\r" + " " * i +
                    "⭐ 🎉 CONGRATULATIONS! YOU WIN! 🎉 ⭐"
                )
                sys.stdout.flush()
                time.sleep(0.08)

            print("\n")

            print("""
╔══════════════════════════════╗
║ 🎉 CONGRATULATIONS! 🎉      ║
║        YOU WIN!             ║
╚══════════════════════════════╝
""")
        
            speak("Congratulations! You win in Hangman Game!")
            break

        if wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            speak("Game Over! You lose in Hangman Game!")
            break

if __name__ == "__main__":
    main()
