tests = [{"k":2,"s":"abcba",},{"k":3,"s":"ahsdfafafafafafajjjadfjaa",},]
def f(k, s,):
	start, end, = 0, 0,
	startc = 0
	last_at = {}
	l = len(s)
	for i in range(l):
		c = s[i]
		if c not in last_at:
			last_at[c] = i
			if len(last_at)>k:
				lk = None
				lv = l
				for key,v, in last_at.items():
					if v < lv:
						lv = v
						lk = key
				startc = last_at.pop(lk)+1
		else:
			last_at[c] = i
		if i+1 - startc > end - start:
			start = startc
			end = i+1
	return s[start:end]
for test in tests:
	print(test," :\n",f(*test.values()),"\n")
input()