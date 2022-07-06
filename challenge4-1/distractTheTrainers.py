def solution(banana_list):
	adjacencyList = {}
	for i in range(len(banana_list)):
		adjacencyList[i] = []

	for i in range(len(banana_list)):
		for j in range(len(banana_list)):
			mean = (banana_list[i] + banana_list[j]) // 2
			if banana_list[i] == banana_list[j]:
				pass
			elif (banana_list[i] + banana_list[j]) % 2 == 1:
				adjacencyList[i].append(j)
			elif mean % 2 == 1:
				adjacencyList[i].append(j)
			else:
				less = min(banana_list[i], banana_list[j])
				while less < mean:
					less = less * 2
				if less != mean:
					adjacencyList[i].append(j)

	degree = {}
	for vertex in adjacencyList:
		if len(adjacencyList[vertex]) != 0:
			degree[vertex] = len(adjacencyList[vertex])

	while degree:
		minDegree = min(degree.values())
		minDegreeVertex = min(degree, key=degree.get)

		if minDegree == 0:
			del degree[minDegreeVertex]
			continue

		neighborMinDegreeVertex = adjacencyList[minDegreeVertex][0]
		neighborMinDegree = degree[neighborMinDegreeVertex]

		for neighbor in adjacencyList[minDegreeVertex][1:]:
			if degree[neighbor] < neighborMinDegree:
				neighborMinDegree = degree[neighbor]
				neighborMinDegreeVertex = neighbor

		del adjacencyList[minDegreeVertex]
		del adjacencyList[neighborMinDegreeVertex]
		del degree[minDegreeVertex]
		del degree[neighborMinDegreeVertex]

		for vertex in adjacencyList:
			if minDegreeVertex in adjacencyList[vertex]:
				adjacencyList[vertex].remove(minDegreeVertex)
				degree[vertex] = degree[vertex] - 1
			if neighborMinDegreeVertex in adjacencyList[vertex]:
				adjacencyList[vertex].remove(neighborMinDegreeVertex)
				degree[vertex] = degree[vertex] - 1

	return len(adjacencyList)
