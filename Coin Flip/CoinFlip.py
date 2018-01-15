import random

def coinFlip():
	numFlips = input("Number of flips: ")
	flips = [random.randint(0,1) for i in range(numFlips)]
	result = []
	for num in flips:
		if num == 0:
			result.append("Heads")
		elif num == 1:
			result.append("Tails")
	print result
coinFlip()