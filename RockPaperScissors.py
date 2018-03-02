print("Rock, Paper, Scissors, shoot!")
user1 = input()
user2 = input()
if user1 == user2:
	print("Both tie!")
elif user1 == "rock":
	if user2 == "paper":
		print("User 2 wins!")
	elif user2 == "scissors":
		print("User 1 wins!")
	else:
		print("Please try again!")		
elif user1 == "paper":
	if user2 == "rock":
		print("User 1 wins!")
	elif user2 == "scissors":
		print("User 2 wins!")
	else:
		print("Please try again!")		
elif user1 == "scissors":
	if user2 == "rock":
		print("User 2 wins!")
	elif user2 == "paper":
		print("User 1 wins!")
	else:
		print("Please try again!")
else:
	print("Please try again!")