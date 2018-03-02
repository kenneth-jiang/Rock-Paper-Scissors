print("Rock, Paper, Scissors, shoot!")

user1 = input("Player 1, make your move: ")
print("*** NO CHEATING *** \n\n" * 20)
user2 = input("Player 2, make your move: ")

if user1 == user2:
	print("Both tie!")
elif user1 == "rock":
	if user2 == "paper":
		print("User 2 wins!")
	elif user2 == "scissors":
		print("User 1 wins!")
	else:
		print("An error occured, please try again!")	
elif user1 == "paper":
	if user2 == "rock":
		print("User 1 wins!")
	elif user2 == "scissors":
		print("User 2 wins!")
	else:
		print("An error occured, please try again!")		
elif user1 == "scissors":
	if user2 == "rock":
		print("User 2 wins!")
	elif user2 == "paper":
		print("User 1 wins!")
	else:
		print("An error occured, please try again!")
else:
	print("An error occured, please try again!")