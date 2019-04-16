tests=[["ray","ra.",],["raymond","ra.",],["chat",".*at",],["chats",".*at",],]
def match(s,re,):
	pp=[]
	for ree in re:
		if ree=='*':pp[len(pp)-1][1]=1
		else:pp.append([ree,0,],)
	ls,lre,=len(s),len(pp),
	def rem(s,re,):
		if re==".":return True
		return s==re
	def ppmatch(s,re,si,rei,):
		if rei>=lre:
			if si>=ls:
				return True
			return False
		reat=re[rei]
		type=reat[1]
		if type:
			sp=0
			while 1:
				if ppmatch(s,re,si+sp,rei+1,):
					return True
				sp+=1
				if si+sp>=ls or not rem(s[si+sp],reat[0]): return False
		else:
			if not rem(s[si],reat[0]): return False
			return ppmatch(s,re,si+1,rei+1,)
	return ppmatch(s,pp,0,0)
for test in tests: print(test,match(*test),sep=" :\n")
input()fefe