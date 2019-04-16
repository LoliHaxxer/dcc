tests=[[4,{1,2,},],[4,{1,3,5,},],]
def f(stair_height,step_sizes,):
	r = 0
	step_sizes = list(step_sizes)
	step_sizes.sort(reverse=1)
	l = len(step_sizes)
	locked = [0,]
	while 1:
		n = 0
		for i in locked: n += step_sizes[i]
		if n>=stair_height:
			if n==stair_height:
				r+=1
			ll = len(locked)-1
			while 1:
				if ll==-1: return r
				locked[ll]+=1
				if locked[ll]<l: break
				locked.pop(ll)
				ll-=1
		else:
			locked.append(0)
def fr(stair_height,step_sizes,):
	if stair_height==0: return 1
	r = 0
	for ss in step_sizes:
		if ss==stair_height:
			r += 1
		elif ss<stair_height:
			r += fr(stair_height-ss,step_sizes,)
	return r
for test in tests:
	print(test," (iterative):\n",f(*test),"\n")
	print(test," (recursive):\n",fr(*test),"\n")
input()