

def changeDirection(direction):
	
	if direction == "right": #right
		return "down" # go down
		
	elif direction == "down": #down
		return "left" #go left
		
	elif direction == "left": #left
		return "up" #go up
		
	else: #up
		return "right" #go right

s= [ [1, 2, 3, 4],
	 [5, 6, 7, 8],
	 [9, 10, 11, 12]]

	 
	 
size = len(s) * len(s[0])

visited = {}

direction = "right"

i, j = 0, 0


while(len(visited) < size):
	
	if (i,j) not in visited:
		visited[(i,j)] = True
		print(s[i][j])
	
	if direction == "right": #right
		if (i + 1) > (len(s) - 1) or ((i+1, j) in visited):		
			direction = changeDirection(direction)
		else:
			
			i += 1
	
	elif direction == "down": #down
		if (j + 1) > (len(s[0]) - 1) or ((i, j+1) in visited):
			direction = changeDirection(direction)
		else:
			j += 1
		
	elif direction == "left": #left
		if (i - 1) < 0  or ((i - 1, j) in visited):
			direction = changeDirection(direction)
		else:
			i -= 1

			
	else: #up
		if (j - 1) < 0 or ((i, j - 1) in visited):
			direction = changeDirection(direction)
		else:
			j -= 1

