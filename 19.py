from random import randrange 
def matrix(n,k,):
		r=[]
		for i in range(n):
			r.append([])
			for j in range(k): r[i].append(randrange(88))
		return r
def minimal_cost(matrix):
	def helper(matrix, results, curr_house, prev_color, curr_cost, curr_sequence):
		if curr_house == len(matrix):
			results.append((curr_cost, curr_sequence))
			return
		for i in range(0, len(matrix[0])):
			if i != prev_color:
				helper(matrix, results, curr_house + 1, i, matrix[curr_house][i] + curr_cost, curr_sequence + str(i))
	results = []
	helper(matrix, results, 0, -1, 0, "")
	print(results)
	return min(results)
matrix = matrix(10,5,)
print(matrix," :\n",minimal_cost(matrix))
input()