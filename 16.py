from math import log as l, e
class log(object):
	def __init__(s,a=0):
		if a==0: print("Here's your log wood:\n|##############|")
		else: print("Here's your log:\nln("+str(a)+") =",l(a,e))
		s.a = a
		s.s = [None]*a
		s.at = 0
	def record(s,order_id):
		s.s[s.at] = order_id
		s.at+=1
		s.at%=s.a
	def get_last(s,i):
		return s.s[(s.at-i)%s.a]
	def get_record(s):
		return [s.s[i%s.a]for i in range(s.at+s.a-1,s.at-1,-1)]
LOG = None
try:
	while 1:
		i = input((str(LOG.get_record())+"\n")if LOG is not None else""+"n$int$ new log\nr$int$ record order_id\ng$int$ get last i-th element\nq quit ur job\n")
		if i=="": continue
		elif i[0]=="n": LOG = log(int(i[1:]))
		elif i[0]=="r": LOG.record(int(i[1:]))
		elif i[0]=="g": print(LOG.get_last(int(i[1:])))
		elif i=="q": break
finally: input()