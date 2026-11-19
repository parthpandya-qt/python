import random
import math

# Take user input
user_input = input("Enter Snake (S), Water (W), or Gun (G): ").lower()

# List of computer choices
computer = ["s", "w", "g"]

# Generate a random index
random_number = math.floor(random.random() * 3)
computer_choice = computer[random_number]

print(f"Computer chose: {computer_choice.upper()}")

# Game logic
if user_input == computer_choice:
    print("It's a Draw!")
elif (user_input == "s" and computer_choice == "w") or \
     (user_input == "w" and computer_choice == "g") or \
     (user_input == "g" and computer_choice == "s"):
    print("You Win!")
else:
    print("Computer Wins!")
