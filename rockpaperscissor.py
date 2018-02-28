#rock Paper Scissior console game.

import random

game_Choice = ["rock","paper","scissor"]


play = True

while play:
	player_Choice = input("Player enter your choice[rock,paper,scissor]: ")
	cpu_Choice = random.choice(game_Choice)
	if player_Choice == cpu_Choice:
		print("Same choice as Cpu play again...")
	elif player_Choice == "rock":
		if cpu_Choice == "paper":
			print("You loose! Cpu choosed Paper and won...")
		else:
			print("You Win! Cpu choosed Scissior and loose...")
		play = False	
	elif player_Choice == "paper":
		if cpu_Choice == "scissor":
			print("You loose! Cpu choosed scissor and won...")
		else:
			print("You Win! Cpu choosed rock and loose...")
		play = False
	else:
		if cpu_Choice == "rock":
			print("You loose! Cpu choosed rock and won...")
		else:
			print("You Win! Cpu choosed paper and loose...")
		play = False

print("cpu_Choice: " + cpu_Choice)		


