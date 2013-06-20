"""
		C   A   T
	0	1	2	3
V   1   1   2   3
B   2   2   2   3
A   3   3   2   3
T   4   4   3   2

"""

from sys import *

str1 = stdin.readline().strip()
str2 = stdin.readline().strip()

lstr1 = len(str1); lstr2 = len(str2)
#This defines matrix of size (lstr2 + 1) x (lstr1 + 1)
distance = [[0] * (lstr1 + 1) for x in xrange(lstr2 + 1)]
# 1. horizontal is str1, vertical is str2
for i in xrange(lstr1 + 1):
	distance[0][i] = i
for i in xrange(lstr2 + 1):
	distance[i][0] = i

#The order of these two loops dosn't matter
#We only have to gurantee that i is from str2 and j is from str1, see 1
for j in xrange(lstr1):
	for i in xrange(lstr2):
		#distance[i + 1][j + 1] is actually the value of str2[i] and str1[j]
		if(str2[i] == str1[j]):
			distance[i + 1][j + 1] = distance[i][j]
		else:
			"""
			The path for B-> C is:
				transform V to C: [1][1] -> 1
				delete B: [2][1] -> 2
			"""
			deletion = distance[i][j + 1] + 1
			"""
			The path for B->C is:
				delete V [1][0] -> 1
				delete B [2][0] -> 2
				insert C [2][1] -> 3
			"""
			insertion = distance[i + 1][j] + 1
			"""
			The path for B->C is:
				delete V[1][0] -> 1
				transform B to C: [2][1] -> 2
			"""
			transformation = distance[i][j] + 1
			distance[i + 1][j + 1] = min(deletion, insertion, transformation)

print distance
print distance[lstr2][lstr1]