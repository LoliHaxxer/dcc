tests = [[2, 4, 6, 2, 5],[2, 4, 1, 2, 5],[5, 1, 1, 5],[-1,-88,-69,-23],]

def maxsum(input):
	for i in range(len(input)):
		if i==0:
			curMax = input[i]
			lastMax = 0
		else:
			temp = curMax
			curMax = max(lastMax+input[i], curMax)
			lastMax = temp
	return curMax

for test in tests:
	print(test," :\n",maxsum(test),"\n")
input()