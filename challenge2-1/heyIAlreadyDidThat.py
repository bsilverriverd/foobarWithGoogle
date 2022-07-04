def solution(n, b):
	myDict = dict()
	cnt = 0
	myDict[n] = cnt
	cnt += 1

	solution = -1
	while True:
		desc = sorted(n, reverse=True)
		asce = sorted(n)
		
		z = []
		for i in range(len(desc)-1, -1, -1):
			sub = ord(desc[i]) - ord(asce[i]) ;
			if sub < 0:
				sub += b
				desc[i-1] = chr(ord(desc[i-1]) -1)
			z.append(chr(ord('0') + sub))
		z.reverse()
		n = ''.join(z)
		if n in myDict:
			return cnt - myDict[n]
		else:
			myDict[n] = cnt
			cnt += 1
