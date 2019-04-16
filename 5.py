tests = [[2, 3,],]

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def r(*a):return a[0]
	return pair(r)
def cdr(pair):
	def r(*a):return a[1]
	return pair(r)
	
for test in tests:
	print(test," :")
	print("car: ",car(cons(test[0],test[1])))
	print("cdr: ",cdr(cons(test[0],test[1])))
input()