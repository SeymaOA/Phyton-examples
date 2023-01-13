from random import randint


print("Rock...")
print("Paper...")
print("Scissors...")


player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}")



if player == computer:
	print("It's a tie!")
elif player == "rock" and computer == "scissors":
	print("Player wins!")
elif player == "rock" and computer == "paper":
	print("computer wins!")
elif player == "paper" and computer == "rock":
	print("player wins!")
elif player == "paper" and computer == "scissors":
	print("computer wins!")
elif player == "scissors" and computer == "rock":
	print("computer wins!")
elif player == "scissors" and computer == "paper":
	print("player wins!")

else:
	print("Please enter a valid move")