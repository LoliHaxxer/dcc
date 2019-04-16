import sys

tests = [[3, 4, -1, 1], [1, 2, 0],]
k = [2, 3,]

def exe(input):
	min = 0
	pretenders = []
	for i in input:
		if i>min:
			if i==min+1:
				min = i
				k = 0
				while k<len(pretenders):
					if pretenders[k]==min+1:
						min = pretenders.pop(k)
					else:
						k += 1
			else:
				pretenders.append(i)
	return min+1
				
	
for i in range(len(tests)):
	print(tests[i],":\n",exe(tests[i]),"\nassertion: ",k[i],"\n")
import ast
print(exe(ast.literal_eval(input("input your test:\n"))))
input()
