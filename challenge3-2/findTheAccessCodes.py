def solution(l):
	hist = {}
	list = []
	for i in range(len(l)):
		hist[i] = 0
	for i, denominator in enumerate(l[0:-1]):
		for j, numerator in enumerate(l[i+1:], i+1):
			if numerator % denominator == 0:
				hist[i] = hist[i] + 1
				list.append(j)
	ret = 0
	for i in list:
		ret = ret + hist[i]
	return ret
