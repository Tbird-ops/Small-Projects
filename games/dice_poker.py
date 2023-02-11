import random as rand
import time

player = []
player_hand = {1:0,2:0,3:0,4:0,5:0,6:0}
computer = []
comp_hand = {1:0,2:0,3:0,4:0,5:0,6:0}

def play_dice():
	time.sleep(2)
	for x in range(5):
		roll = rand.randint(1,6)
		player.append(roll)
	player.sort()
	print("Your roll:",player)

def comp_dice():
	time.sleep(2)
	for x in range(5):
		roll = rand.randint(1,6)
		computer.append(roll)
	computer.sort()
	print("computer:",computer)

def reroll(list, index):
	for char in range(len(index)):
		list[int(index[char])-1] = rand.randint(1,6)
	if list == player:
		player.sort()
		print("Your roll:",player)
	else:
		computer.sort()
		print("computer:",computer)	

def check_hand():
	for num in player:
		if num == 1:
			player_hand[1] += 1
		elif num == 2:
			player_hand[2] += 1
		elif num == 3:
			player_hand[3] += 1
		elif num == 4:
			player_hand[4] += 1
		elif num == 5:
			player_hand[5] += 1
		else:
			player_hand[6] += 1
	

def main():
	play_dice()
	comp_dice()
	index = input("Which dice would you like to reroll?")
	reroll(player,index)


main()
check_hand()
print(player_hand)

