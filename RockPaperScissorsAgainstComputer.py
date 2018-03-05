from random import randint

winning_score = 3
user_score = 0
comp_score = 0

print("Welcome to Rock, Paper, Scissors 2.0!")
while (user_score < winning_score and comp_score < winning_score):
	print(f"Your score: {user_score} | Computer Score: {comp_score}")
	print("Make your choice: Rock, Paper, Scissors")
	
	random = randint(0,2)
	if random == 0:
		choice = "rock"
	elif random == 1:
		choice = "paper"
	elif random == 2:
		choice = "scissors"
	
	user_input = input().lower()
	print(f"Computer has picked {choice}!")
	if user_input == "q" or user_input == "quit":
		break
	elif user_input == choice:
		print("It's a tie, try again!")
	elif user_input == "rock":
		if choice == "paper":
			print("Computer wins!")
			comp_score += 1
		elif choice == "scissors":
			print("Player wins!")
			user_score += 1
	elif user_input == "paper":
		if choice == "scissors":
			print("Computer wins!")
			comp_score += 1
		elif choice == "rock":
			print("Player wins!")
			user_score += 1
	elif user_input == "scissors":
		if choice == "rock":
			print("Computer wins!")
			comp_score += 1
		elif choice == "paper":
			print("Player wins!")
			user_score += 1
	else:
		print("An error occured, please try again!")
if user_score > comp_score:
	print("Congrats, you win!")
elif user_score < comp_score:
	print("Oh no, the computer wins... :(")
elif user_score == comp_score:
	print("It's a tie!")
print(f"FINAL SCORE - User: {user_score} | Computer: {comp_score}")