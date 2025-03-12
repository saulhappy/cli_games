def number_guesser():
    print("\n🤖 Welcome to Number Guesser! 🤖")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("After each guess, respond with:")
    print("  - 'y' if I guessed right ✅")
    print("  - 'h' if your number is greater 📈")
    print("  - 'l' if your number is smaller 📉\n")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2  # Binary search guess
        attempts += 1
        print(f"🤔 Is your number {guess}?")

        response = input("Type 'y', 'h', or 'l': ").strip().lower()

        if response == "y":
            print(f"🎉 I guessed your number {guess} in {attempts} tries! 🚀")
            break
        elif response == "h":
            low = guess + 1  # Adjust search range upwards
        elif response == "l":
            high = guess - 1  # Adjust search range downwards
        else:
            print("⚠️ Invalid response! Please type 'y', 'h', or 'l'.")

    print("\nThanks for playing! 🎮")

# Run the game
number_guesser()
