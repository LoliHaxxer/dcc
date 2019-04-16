tests = [[(30, 75), (0, 50), (60, 150)],[(90,91), (94, 120), (95, 112), (110, 113), (150, 190), (180, 200)]]
#original
#https://github.com/Jedshady/daily-coding-problem/blob/master/Problem%201-30/problem_21.py
def find_min_rooms(time_list):
	start = sorted([num[0] for num in time_list])
	end = sorted([num[1] for num in time_list])
	room_occupied = max_room_num = 0
	i = j = 0
	n = len(time_list)
	while i < n and j < n:
		if start[i] < end[j]:
			room_occupied += 1
			max_room_num = max(room_occupied, max_room_num)
			i += 1
		else:
			room_occupied -= 1
			j += 1
	return max_room_num
#copied
#actually 3000 iq
#wtf?
def rooms_needed(ivs):
	s,e, = sorted([x[0] for x in ivs]),sorted([x[1] for x in ivs]),
	at=r=i=j=0
	l = len(ivs)
	while i<l:
		if s[i]<e[j]:
			at+=1
			r=max(r,at,)
			i+=1
		else:
			at-=1
			j+=1
	return r
for test in tests: print(test,find_min_rooms(test),sep=" :\n")
for test in tests: print(test,rooms_needed(test),sep=" :\n")
input()