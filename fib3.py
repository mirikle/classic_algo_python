from math import sqrt

def f(n):
	return 1.0 / sqrt(5) * (((1 + sqrt(5)) / 2) ** n - (- 2 / (1 + sqrt(5)))**n)

print f(3)
print f(4)
print f(5)
