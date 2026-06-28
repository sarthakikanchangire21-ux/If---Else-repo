# Rock,Paper,Scissors 
user = input("Enter your choice (rock, paper, scissors): ").lower()
if user == computer:
    print("It's a Tie!")
elif user == "paper":
    print("You win!")
elif user == "sissors":
    print("Computer wins!")
elif user == "rock":
    print("It's a Tie!")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")