def solution(map):
	path = []
	for i in range(len(map)):
		row = []
		for j in range(len(map[i])):
			row.append(1000)
		path.append(row)
	
	removeDict = {}
	nonRemoveDict = {}
	nonRemoveDict[(0,0)] = 1

	dir = [(1,0), (0,1), (-1,0), (0,-1)]
	while nonRemoveDict:
		(x, y), val = nonRemoveDict.popitem()
		if path[y][x] < val:
			continue
		path[y][x] = val
		for i in range(len(dir)):
			dx, dy = dir[i]
			nx = x + dx
			ny = y + dy
			if nx < 0 or nx >= len(map[0]) or ny < 0 or ny >= len(map):
				continue
			if path[ny][nx] > val+1:
				if map[ny][nx] == 0:
					if (nx, ny) in nonRemoveDict:
						nonRemoveDict[(nx, ny)] = min(nonRemoveDict[(nx, ny)], val+1)
					else:
						nonRemoveDict[(nx, ny)] = val+1
				else:
					if (nx, ny) in removeDict:
						removeDict[(nx, ny)] = min(removeDict[(nx, ny)], val+1)
					else:
						removeDict[(nx, ny)] = val+1

	while removeDict:
		(x, y), val = removeDict.popitem()
		if path[y][x] < val:
			continue
		path[y][x] = val
		for i in range(len(dir)):
			dx,dy = dir[i]
			nx = x + dx
			ny = y + dy
			if nx < 0 or nx >= len(map[0]) or ny < 0 or ny >= len(map):
				continue
			if path[ny][nx] > val+1 and map[ny][nx] == 0:
				if (nx, ny) in removeDict:
					removeDict[(nx, ny)] = min(removeDict[(nx, ny)], val+1)
				else:
					removeDict[(nx, ny)] = val+1

	return path[-1][-1]
