import sys

def possiblePaths(number_of_stairs, dictionary):
    if number_of_stairs in dictionary:
        return dictionary[number_of_stairs]
    if number_of_stairs == 0:
        return 0
    if number_of_stairs == 1:
        return 1
    if number_of_stairs == 2:
        return 1 + possiblePaths(1, dictionary)
    if number_of_stairs == 3:
        return 1 + possiblePaths(2, dictionary) + possiblePaths(1, dictionary)
    else:
        number_of_paths = possiblePaths(number_of_stairs - 3, dictionary)
        number_of_paths += possiblePaths(number_of_stairs - 2, dictionary)
        number_of_paths += possiblePaths(number_of_stairs - 1, dictionary)
        dictionary[number_of_stairs] = number_of_paths
        return number_of_paths
    

 
if len(sys.argv) > 1:
    number_of_stairs = sys.argv[1]
    print(possiblePaths(int(number_of_stairs), {}))
else:
    print("An argument is required to run the algorithm")