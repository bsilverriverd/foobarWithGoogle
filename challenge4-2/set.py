cnt = 0
import fractions
for i in range(0, 1000):
	for j in range(0, 1000):
		if fractions.gcd(i, j) == 1:
			cnt = cnt + 1
print(cnt)
