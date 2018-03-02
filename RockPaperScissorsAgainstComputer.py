from random import randint

random = randint(0,2)
if random == 0:
	choice = "rock"
elif random == 1:
	choice = "paper"
elif random == 2:
	choice = "scissors"

print("Welcome to Rock, Paper, Scissors 2.0! \n Make your choice!")
user_input = input()

if user_input == choice:
	print(f"Computer has picked {choice}!")
	print("It's a tie, try again!")
elif user_input == "rock":
	if choice == "paper":
		print(f"Computer has picked {choice}!")
		print("Computer wins!")
	elif choice == "scissors":
		print(f"Computer has picked {choice}!")
		print("Player wins!")
	else:
		print("An error occured, please try again!")
elif user_input == "paper":
	if choice == "scissors":
		print(f"Computer has picked {choice}!")
		print("Computer wins!")
	elif choice == "rock":
		print(f"Computer has picked {choice}!")
		print("Player wins!")
	else:
		print("An error occured, please try again!")
elif user_input == "scissors":
	if choice == "rock":
		print(f"Computer has picked {choice}!")
		print("Computer wins!")
	elif choice == "paper":
		print(f"Computer has picked {choice}!")
		print("Player wins!")
	else:
		print("An error occured, please try again!")
else:
	print("An error occured, please try again!")
