tests=[[{'quick', 'brown', 'the', 'fox',},"thequickbrownfox"],[{'bed', 'bath', 'bedbath', 'and', 'beyond',},"bedbathandbeyond"]]
def f(ss,s):
	r = []
	a = b = 0
	for b in range(1,len(s)+1):
		if s[a:b] in ss:
			r.append(s[a:b])
			a=b
	return r
for test in tests: print(test,f(*test),sep=" :\n")
input()