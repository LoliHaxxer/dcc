tests = [[10, 15, 3, 7],]
k = [17,]

def exe(input,k):
	print(input,k," :")
	a = []
	for i in tests:
		for j in a:
			if i+j==k:
				return True
		a.append(i)
	return False

for i in range(len(tests)):
	print(exe(tests[i], k[i]),"\n")
input()