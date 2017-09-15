
def findPathMemo(position_x, position_y, grid, path, operations, visited):
    operations[0] += 1
    visited[(position_x, position_y)] = True
    path.append((position_x, position_y))
    if grid[position_x][position_y] == 'o':
        return True
    if grid[position_x][position_y] == 'x':
        path.pop(len(path) - 1)
        return False
    else:
        if position_x - 1 >= 0 and (position_x < len(grid)) and (position_x - 1, position_y) not in visited: 
            if findPathMemo(position_x - 1, position_y, grid, path, operations, visited):
                return True
        if position_y + 1 >= 0 and position_y < len(grid[0]) and (position_x, position_y + 1) not in visited:
            if findPathMemo(position_x, position_y + 1, grid, path, operations, visited):
                return True
    
    path.pop(len(path) -1)
    return False

def findPath(position_x, position_y, grid, path, operations):
    operations[0] += 1
    path.append((position_x, position_y))
    if grid[position_x][position_y] == 'o':
        return True
    if grid[position_x][position_y] == 'x':
        path.pop(len(path) - 1)
        return False
    else:
        if position_x - 1 >= 0 and (position_x < len(grid)): 
            if findPath(position_x - 1, position_y, grid, path, operations):
                return True
        if position_y + 1 >= 0 and position_y < len(grid[0]):
            if findPath(position_x, position_y + 1, grid, path, operations):
                return True
    
    path.pop(len(path) -1)
    return False
        


grid = [['c','x','c','x','c','x','c','x','c','x','c','x','o'],['c','c','c','c','c','c','c','c','c','c','c','c','c']]


path = []
operations = [0]


print("we expect both functions to return the same path but the first one tries less paths")

findPathMemo(1,0, grid, path, operations, {})
print(path)
print(operations[0])

path = []
operations = [0]
findPath(1,0, grid, path, operations)
print(path)
print(operations[0])
