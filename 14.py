import random as r
from random import Random
from threading import Thread
def pi(ap=8000000,load_split=4):
	c=[]
	for i in range(load_split): c.append(0)
	def t(seed,ap=ap/load_split):
		r = Random()
		r.seed(seed)
		while ap>0:
			if ((r.random()-0.5)**2+(r.random()-0.5)**2)**0.5<=0.5:
				c[seed]+=1
			ap-=1
	th = []
	for i in range(load_split):
		thr = Thread(target=t,args=[i])
		thr.start()
		th.append(thr)
	for i in range(ap%load_split): 
		if ((r.random()-0.5)**2+(r.random()-0.5)**2)**0.5<=0.5: c+=1
	for i in th: i.join()
	return 4 * sum(c) / ap
input(pi())