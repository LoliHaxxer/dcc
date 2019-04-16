from collections import deque
import timeit
tests = [[[10, 5, 2, 7, 8, 7],3],[[24, 2, 18, 38, 1, 7, 6, 9, 14, 9, 13, 31, 18, 19, 38, 12, 32, 6, 19, 34, 37, 16, 23, 31, 2, 38, 28, 40, 16, 19, 12, 13, 37, 26, 21, 10, 27, 23, 7, 42, 20, 42, 14, 2, 0, 31, 14, 38, 29, 42, 14, 40, 42, 38, 3, 17, 2, 48, 6, 36, 6, 30, 44, 27, 1, 42, 16, 6, 3, 11, 25, 29, 29, 31, 3, 22, 33, 42, 45, 35, 10, 23, 24, 32, 2, 21, 37, 21, 25, 0, 22, 18, 31, 4, 48, 48, 22, 2, 43, 11, 39, 49, 6, 33, 48, 18, 43, 19, 20, 4, 30, 29, 43, 21, 25, 36, 15, 22, 12, 19, 2, 34, 29, 41, 21, 27, 43, 5, 20, 16, 43, 45, 17, 21, 1, 12, 41, 40, 12, 6, 43, 8, 35, 37, 12, 30, 27, 17, 14, 1, 24, 32, 1, 15, 42, 43, 48, 26, 26, 4, 32, 30, 22, 1, 49, 5, 39, 49, 14, 20, 33, 47, 21, 2, 22, 4, 19, 21, 7, 39, 15, 0, 6, 24, 13, 21, 19, 42, 34, 47, 13, 3, 14, 28, 41, 9, 2, 7, 14, 45, 21, 27, 29, 7, 31, 1, 30, 10, 11, 31, 6, 25, 23, 35, 19, 16, 44, 30, 44, 18, 45, 23, 46, 33, 1, 17, 0, 29, 16, 5, 11, 31, 34, 41, 3, 44, 46, 43, 9, 17, 22, 15, 16, 4, 35, 37, 31, 44, 8, 18, 17, 31, 38, 32, 38, 19, 38, 11, 42, 0, 25, 30, 9, 17, 8, 40, 14, 16, 7, 41, 40, 44, 44, 23, 45, 15, 29, 37, 10, 36, 14, 36, 44, 43, 6, 12, 25, 7, 20, 48, 20, 20, 31, 10, 5, 36, 41, 42, 2, 11, 36, 41, 4, 20, 11, 4, 6, 27, 17, 23, 6, 25, 26, 28, 18, 30, 20, 47, 31, 47, 4, 10, 41, 27, 37, 47, 4, 46, 18, 22, 6, 18, 39, 4, 21, 43, 25, 32, 40, 18, 32, 39, 4, 5, 34, 45, 6, 23, 31, 37, 11, 12, 21, 8, 47, 39, 18, 48, 20, 1, 40, 18, 26, 9, 4, 21, 40, 36, 21, 14, 15, 47, 14, 27, 47, 19, 6, 17, 0, 4, 37, 45, 12, 19, 23, 34, 33, 16, 32, 42, 48, 1, 22, 41, 7, 28, 43, 31, 15, 35],13]]
def subway(input):
	a,k,=input
	r=[]
	for i in range(len(a)-k+1):
		max = a[i]
		for j in range(i+1,i+k):
			if a[j]>max: max = a[j]
		r.append(max)
	return r
def sobway(input):
	'''Create a Double Ended Queue, q that will store indexes of array elements.
	The queue will store indexes of useful elements in every window and it will
	maintain decreasing order of values from front to rear in q, i.e.,
	arr[q.front[]] to arr[q.rear()] are sorted in decreasing order.
	Args:
		arr(list): input array of integers
		n(int): length of input array
		k(int): window size
	Returns:
		None
	'''
	r=[]
	q = deque()
	arr,k, = input
	n = len(arr)
	# Process first k (or first window) elements of array
	for i in range(k):

		# For every element, the previous smaller elements are useless so remove
		# them from q
		while q and arr[i] >= arr[q[-1]] :
			q.pop()

		# Add new element at rear of queue
		q.append(i)

	# Process rest of the elements, i.e. from arr[k] to arr[n-1]
	for i in range(k, n):

		# The element at the front of the queue is the largest element of
		# previous window, so print it
		r.append(arr[q[0]])

		# Remove the elements which are out of this window
		while q and q[0] <= i-k:
			# remove from front of deque
			q.popleft()

		# Remove all elements smaller than the currently being added element
		# (Remove useless elements)
		while q and arr[i] >= arr[q[-1]] :
			q.pop()

		# Add current element at the rear of q
		q.append(i)

	# Print the maximum element of last window
	return r+[arr[q[0]]]
print(timeit.timeit('[subway(test)for test in tests]',globals=globals(),number=1000))
print(timeit.timeit('[sobway(test)for test in tests]',globals=globals(),number=1000))
for test in tests:
	a,b,=subway(test),sobway(test),
	print(test," (sub):\n",a,)
	print(test," (sob):\n",b,)
	print(a==b)
input()