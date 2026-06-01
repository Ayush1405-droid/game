import random

choices = ["rock", "paper", "scissors"]

wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

score = {"you": 0, "computer": 0}

print("=" * 30)
print("   ROCK PAPER SCISSORS")
print("=" * 30)

while True:
    print(f"\nScore  →  You: {score['you']}  |  Computer: {score['computer']}")
    print("Enter rock / paper / scissors  (or 'quit' to exit)")

    user = input("Your choice: ").strip().lower()

    if user == "quit":
        print("\nFinal Score:")
        print(f"  You      : {score['you']}")
        print(f"  Computer : {score['computer']}")
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a TIE!")
    elif wins[user] == computer:
        print("You WIN!")
        score["you"] += 1
    else:
        print("Computer WINS!")
        score["computer"] += 1