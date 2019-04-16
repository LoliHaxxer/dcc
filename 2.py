tests = [[1, 2, 3, 4, 5,],[1, 2, 3,],]

def exe(input):
	result = []
	lens = len(input)
	for i in range(lens):
		result.append(1)
	for i in range(lens):
		item = input[i]
		for k in range(lens):
			if i!=k:
				result[k]*=item
	return result

for test in tests:
	print(test,":")
	print(exe(test),"\n")
	
import ast
print(exe(ast.literal_eval(input("input your test:\n"))))
input()