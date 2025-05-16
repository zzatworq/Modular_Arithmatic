import random

score = 0
rounds = 0

print("🔢 Guess the Last Digit Game! Type 'exit' to quit.\n")

while True:
    base = random.randint(2, 20)          # Base between 2 and 20
    exponent = random.randint(2, 15)       # Exponent between 2 and 15

    correct_last_digit = pow(base, exponent, 10)  # Faster than full pow(base, exponent) % 10

    guess_input = input(f"What is the last digit of {base}^{exponent}? ")

    if guess_input.lower() == 'exit':
        print(f"\nGame over! You played {rounds} rounds with {score} correct guesses. 🎉")
        break

    try:
        guess = int(guess_input)
        rounds += 1

        if guess == correct_last_digit:
            score += 1
            print("✅ Correct!\n")
        else:
            print(f"❌ Wrong! The correct last digit is {correct_last_digit}.\n")

    except ValueError:
        print("⚠️ Please enter a valid digit or 'exit' to quit.\n")
