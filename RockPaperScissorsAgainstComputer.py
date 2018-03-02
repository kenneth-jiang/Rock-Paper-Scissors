from random import randint

random = randint(0,2)
if random == 0:
	choice = "rock"
elif random == 1:
	choice = "paper"
elif random == 2:
	choice = "scissors"

print("Welcome to Rock, Paper, Scissors 2.0! \n Make your choice!")
user_input = input().lower()

print(f"Computer has picked {choice}!")

if user_input == choice:
	print("It's a tie, try again!")
elif user_input == "rock":
	if choice == "paper":
		print("Computer wins!")
	elif choice == "scissors":
		print("Player wins!")
elif user_input == "paper":
	if choice == "scissors":
		print("Computer wins!")
	elif choice == "rock":
		print("Player wins!")
elif user_input == "scissors":
	if choice == "rock":
		print("Computer wins!")
	elif choice == "paper":
		print("Player wins!")
else:
	print("An error occured, please try again!")
