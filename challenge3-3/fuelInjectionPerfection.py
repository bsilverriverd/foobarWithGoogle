def solution(n):
	# Your code here
	recursiveStack = []
	initParam = int(n)
	initStage = 0
	recursiveStack.append((initParam, initStage))
	
	lookupTable = {1: 0}
	while recursiveStack:
		param, stage = recursiveStack.pop()
		
		if param == 1:
			continue
		elif param % 2 == 0:
			if stage == 0:
				recursiveStack.append((param, stage+1))
				if param//2 not in lookupTable:
					recursiveStack.append((param//2, initStage))
			elif stage == 1:
				lookupTable[param] = lookupTable[param//2] + 1
		else:
			if stage == 0:
				recursiveStack.append((param, stage+1))
				if param+1 not in lookupTable:
					recursiveStack.append((param+1, initStage))
			elif stage == 1:
				recursiveStack.append((param, stage+1))
				if param-1 not in lookupTable:
					recursiveStack.append((param-1, initStage))
			elif stage == 2:
				lookupTable[param] = min(lookupTable[param+1], lookupTable[param-1]) + 1
	return lookupTable[initParam]
