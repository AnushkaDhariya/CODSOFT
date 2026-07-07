import random

print("===== ROCK PAPER SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = input("Enter your choice (rock/paper/scissors): ").lower()

    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    print("Your Choice :", user)
    print("Computer Choice :", computer)

    if user == computer:
        print("It's a Tie!")

    elif user == "rock" and computer == "scissors":
        print("You Win!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You Win!")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You Win!")
        user_score += 1

    elif user not in options:
        print("Invalid Choice!")
        continue

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\n----- SCORE BOARD -----")
    print("Your Score :", user_score)
    print("Computer Score :", computer_score)

    play = input("\nDo you want to play again? (yes/no): ").lower()

    if play != "yes":
        break

print("\n===== FINAL RESULT =====")
print("Your Score :", user_score)
print("Computer Score :", computer_score)

if user_score > computer_score:
    print("Congratulations! You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("Match Draw!")

print("Thank You for Playing!")