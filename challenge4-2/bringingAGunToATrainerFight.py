def solution(dimensions, your_position, trainer_position, distance):
	import fractions
	x_dim, y_dim = dimensions
	your_x, your_y = your_position
	trainer_x, trainer_y = trainer_position
	ret = 0
	possibleDir = set()
	for y in range(0, distance + 1):
		for x in range(0, distance + 1):
			if (x ** 2 + y ** 2) > distance ** 2:
				break
			if abs(fractions.gcd(x, y)) == 1:
				possibleDir.add((x, y))
				possibleDir.add((-x, y))
				possibleDir.add((x, -y))
				possibleDir.add((-x, -y))

	ret = set()
	for dir in possibleDir:
		dir_x, dir_y = dir
		
		curr_dir_x = dir_x
		curr_dir_y = dir_y
		curr_x = your_x
		curr_y = your_y
		dist_coef = 1
		while True:
			curr_x = curr_x + curr_dir_x
			curr_y = curr_y + curr_dir_y
			curr_dist_pow = (dist_coef * dir_x) ** 2 + (dist_coef * dir_y) ** 2

			if curr_dist_pow > distance ** 2:
				break

			while curr_x < 0 or x_dim < curr_x:
				if curr_x < 0:
					curr_x = -curr_x
					curr_dir_x = -curr_dir_x
				elif x_dim < curr_x:
					curr_x = x_dim - (curr_x - x_dim)
					curr_dir_x = -curr_dir_x

			while curr_y < 0 or y_dim < curr_y:
				if curr_y < 0:
					curr_y = -curr_y
					curr_dir_y = -curr_dir_y
				elif y_dim < curr_y:
					curr_y = y_dim - (curr_y - y_dim)
					curr_dir_y = -curr_dir_y

			if curr_x == your_x and curr_y == your_y:
				break
			elif curr_x == trainer_x and curr_y == trainer_y:
				ret.add((dir_x, dir_y))
				break
			else:
				dist_coef = dist_coef + 1
	return len(ret)
print(solution([2,2], [1,1], [1,1], 4))
