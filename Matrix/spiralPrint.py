

def changeDirection(vertical, positive):
	
	if (not vertical) and positive: #right
		return (True, True) #down
	elif vertical and positive: #down
		return (False, False) #left
	elif (not vertical) and (not positive): #left
		return (True, False) #up
	else: #up
		return (False, True) #right

s= [ [1, 2, 3, 4],
	 [5, 6, 7, 8],
	 [9, 10, 11, 12]]

	 
	 
size = len(s) * len(s[0])

visited = {}

vertical = False
positive = True

i, j = 0, 0


while(len(visited) < size):
	
	if (i,j) not in visited:
		visited[(i,j)] = True
		print(s[i][j])
	
	if (not vertical) and positive: #right
		if (i + 1) > (len(s) - 1) or ((i+1, j) in visited):		
			vertical, positive = changeDirection(vertical, positive)
		else:
			
			i += 1
	
	elif vertical and positive: #down
		if (j + 1) > (len(s[0]) - 1) or ((i, j+1) in visited):
			vertical, positive = changeDirection(vertical, positive)
		else:
			j += 1
		
	elif (not vertical) and (not positive): #left
		if (i - 1) < 0  or ((i - 1, j) in visited):
			vertical, positive = changeDirection(vertical, positive)
		else:
			i -= 1

			
	else:
		if (j - 1) < 0 or ((i, j - 1) in visited):
			vertical, positive = changeDirection(vertical, positive)
		else:
			j -= 1
			
	
	

print("yo")