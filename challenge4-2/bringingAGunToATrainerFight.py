def solution(dimensions, your_position, trainer_position, distance):
	import fractions
	x_dim, y_dim = dimensions
	your_x_pos, your_y_pos = your_position
	trainer_x_pos, trainer_y_pos = trainer_position
	distance_pow = distance ** 2

	ret = 0
	xxx = []
	for y_dir in range(-distance, distance + 1):
		for x_dir in range(-distance, distance + 1):
			if abs(fractions.gcd(x_dir, y_dir)) != 1:
				continue
			if (x_dir ** 2 + y_dir ** 2) > distance_pow ** 2:
				continue
			(curr_x_dir, curr_y_dir) = (x_dir, y_dir)
			(curr_x_pos, curr_y_pos) = (your_x_pos, your_y_pos)
			dist_coef = 1
			while True:
				curr_x_pos = curr_x_pos + curr_x_dir
				curr_y_pos = curr_y_pos + curr_y_dir
				curr_dist_pow = (dist_coef * x_dir) ** 2 + (dist_coef * y_dir) ** 2

				if curr_dist_pow > distance_pow:
					break

				while curr_x_pos < 0 or x_dim < curr_x_pos:
					if curr_x_pos < 0:
						curr_x_pos = -curr_x_pos
						curr_x_dir = -curr_x_dir
					elif x_dim < curr_x_pos:
						curr_x_pos = x_dim - (curr_x_pos - x_dim)
						curr_x_dir = -curr_x_dir

				while curr_y_pos < 0 or y_dim < curr_y_pos:
					if curr_y_pos < 0:
						curr_y_pos = -curr_y_pos
						curr_y_dir = -curr_y_dir
					elif y_dim < curr_y_pos:
						curr_y_pos = y_dim - (curr_y_pos - y_dim)
						curr_y_dir = -curr_y_dir

				if curr_x_pos == your_x_pos and curr_y_pos == your_y_pos:
					break
				elif curr_x_pos == trainer_x_pos and curr_y_pos == trainer_y_pos:
					xxx.append((x_dir * dist_coef, y_dir * dist_coef))	
					ret = ret + 1
					break
				else:
					dist_coef = dist_coef + 1
	print(xxx)
	return ret
#print(solution([1250,1250], [1,1], [500,501], 10000))
#print(solution([3, 2],[1,1],[2,1],1000))
print(solution([300,275], [150,150], [185,100], 500))
