tests = ["111","",]

def number_of_ways(s):
	def douknowdawae(s):
		if s[0]=="0":
			return 0
		else:
			try: i = int(s)
			except: return 0
			if i>=1 and i<=26:
				return 1
			return 0
	l = len(s)
	if l==0:
		return 0
	elif l==1:
		return douknowdawae(s)
	elif l==2:
		return douknowdawae(s) + 1
	else:
		return douknowdawae(s[:1])*number_of_ways(s[1:])+douknowdawae(s[:2])*number_of_ways(s[2:])
		
for test in tests:
	print(test," :\n",number_of_ways(test),"\n")
input()