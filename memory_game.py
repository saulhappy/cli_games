import random
import time
import os

def display_sequence(sequence):
    print("\nMemorize this sequence:")
    print(" ".join(map(str, sequence)))
    time.sleep(3)  # Show the sequence for 3 seconds
    clear_screen()  # Clear screen after showing

def clear_screen():
    # This works for most CLI environments
    os.system('cls' if os.name == 'nt' else 'clear')

def memory_game():
    round_num = 1
    print("Welcome to the Memory Game!")
    print("You will be shown a sequence of numbers. Try to remember them and type them back in the correct order!\n")

    while True:
        # Generate a random sequence of numbers (1–9) with increasing length per round
        sequence = [random.randint(1, 9) for _ in range(round_num)]
        
        # Display the sequence briefly
        display_sequence(sequence)
        
        # Ask the player to input the sequence
        user_input = input("Enter the sequence you just saw, with spaces between numbers: ")
        
        # Convert the user's input into a list of integers
        try:
            user_sequence = list(map(int, user_input.split()))
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.\n")
            continue

        # Check if the player's input matches the generated sequence
        if user_sequence == sequence:
            print("Correct! Moving to the next round...\n")
            round_num += 1  # Increase difficulty for the next round
        else:
            print("Oops! That was incorrect.")
            print(f"The correct sequence was: {' '.join(map(str, sequence))}")
            print(f"You made it to round {round_num}.\n")
            break  # End the game on a wrong answer

    print("Game Over. Thanks for playing!")

# Start the game
memory_game()
