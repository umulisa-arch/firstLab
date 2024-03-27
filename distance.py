import math

def distance(x1, y1, x2, y2):
    # Calculate the differences in x and y coordinates
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    # Calculate the square of the differences
    delta_x_squared = delta_x ** 2
    delta_y_squared = delta_y ** 2
    
    # Calculate the sum of the squares of the differences
    sum_of_squares = delta_x_squared + delta_y_squared
    
    # Calculate the square root of the sum of squares to get the distance
    distance = math.sqrt(sum_of_squares)
    
    return distance

# Example usage:
x1, y1 = 7, 2
x2, y2 = 4, 9
print(distance(x1, y1, x2, y2))  # Output will be 5.0
