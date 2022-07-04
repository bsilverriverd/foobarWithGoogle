def solution(xs):
	result = xs[0]
	for i in xs[1:]:
		if i != 0:
			result = result * i
	
	if result < 0 and len(xs) > 1:
		result = result // max([n for n in xs if n < 0])
	
	return str(result)

print(solution([-2, -3, 4, -5]))
