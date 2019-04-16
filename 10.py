import time, threading
def test1():
	print("Sieg Heil!")
tests = [[test1,8888,],]
def js(f,n):
	def ff():
		time.sleep(n/1000)
		f()
	threading.Thread(target=ff).start()

for i in range(len(tests)):
	print("start test #"+str(i),js(tests[i][0],tests[i][1],),)
input()