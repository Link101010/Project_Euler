import math

def num_of_possible_routes(grid_size):
    return math.factorial(grid_size*2) / (math.factorial(grid_size)**2)

print(num_of_possible_routes(20))