n = int(raw_input())
points = []
for i in range(n):
    points.append(map(int, raw_input().split()))

#print '\n'.join([' '.join([str(c) for c in r]) for r in dist])

def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

avg = [0, 0]
for i in range(n):
	avg[0] += points[i][0]
	avg[1] += points[i][1]
avg = map(lambda x : x / float(n), avg)


# find the point closest to the average point
min_dist = 10**18
min_point = None
for i in range(n):
	dist = distance(avg, points[i])
	if dist < min_dist:
		min_dist = dist
		min_point = i


def mahattan(i, j):
	return max(abs(points[i][0] - points[j][0]), abs(points[i][1] - points[j][1]))

min_len = 0
for i in range(n):
	min_len += mahattan(i, min_point)

print min_len
