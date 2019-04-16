def minmoves(matrix, start, end):
	def h_cost(xy): return abs(end[0]-xy[0])+abs(end[1]-xy[1])
	def neighbours(xy):
		r=[]
		for move in moves:
			neigh = (xy[0]+move[0],xy[1]+move[1],)
			if neigh[0]>=0 and neigh[1]>=0 and neigh[0]<w and neigh[1]<h and not matrix[neigh[0]][neigh[1]]:
				r.append(neigh)
		return r
	def ret(xy):
		p,r,= parent[xy],0,
		while p:
			r+=1
			p=parent[p]
		return r
	w,h, = len(matrix),len(matrix[0]),
	moves = ((1,0,),(-1,0,),(0,1,),(0,-1,),)
	open,closed,=dict(),set(),
	parent,g_cost,=dict(),dict(),
	open[start]=h_cost(start)
	parent[start]=None
	g_cost[start]=0
	while 1:
		cur, lv, = None, w + h + 1
		for k,v, in open.items():
			if v<lv:
				cur = k
				lv = v
		open.pop(cur)
		closed.add(cur)
		if cur==end: return ret(cur)
		
		for neighbour in neighbours(cur):
			if neighbour in closed: continue
			cg=g_cost[cur]+1
			if neighbour not in open or cg<g_cost[neighbour]:
				parent[neighbour] = cur
				g_cost[neighbour] = cg
				open[neighbour] = cg+h_cost(neighbour)
matrix = [[0, 0, 0, 0],
[1, 1, 0, 1],
[0, 0, 0, 0],
[0, 0, 0, 0]]
start,end = (3, 0),(0, 0)
input(minmoves(matrix,start,end))