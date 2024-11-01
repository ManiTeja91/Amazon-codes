import math
def min_cleaning_cost(dataset, x, y):
    stack = []
    cost = 0
    
    for char in dataset:
        if stack and stack[-1] == char:           
            stack.pop()
            cost += x
        elif char in stack and x < y:
            stack.pop(stack.index(char))
            cost += x
        else:
            stack.append(char)
    
    cost += math.ceil(len(stack)/2) * y
    
    
    return cost

# Example usage:
dataset = "aaabca"
x = 3
y = 2
print(min_cleaning_cost(dataset, x, y))  # Output should be 7
