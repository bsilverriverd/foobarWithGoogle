def solution(x, y):
	x.sort()
	y.sort()

	import itertools
	for (i, j) in zip(x, y):
		if i != j:
			return j if len(x) < len(y) else i
	return y[-1] if len(x) < len(y) else x[-1]
