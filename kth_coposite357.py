INFITE = 65536

#k = int(raw_input('pls input k: '))
from sys import stdin 
k = int(stdin.readline())

q1 = [3]
q2 = [5]
q3 = [7]

print 1
for i in range(1, k):
	head1 = q1[0] if len(q1) > 0 else INFITE
	head2 = q2[0]
	head3 = q3[0]
	mi = min(head1, head2, head3)
	print mi
	q3.append(mi * 7)
	if mi == head3:
		del q3[0]
		continue
	q2.append(mi * 5)
	if mi == head2:
		del q2[0]
		continue
	q1.append(mi * 3)
	if mi == head1:
		del q1[0]


