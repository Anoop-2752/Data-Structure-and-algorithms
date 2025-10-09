# Linear search algorithm
# Method 1: Return first occurrence

numbers = [5,2,5,7,5,9,5,3]
target = 5

def linear_search_first(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

result1 = linear_search_first(numbers, target)
print(f"Method 1 (first occurrence): Element index = {result1}")


#----------------------------------------------------------------

# Method 2: Return all occurrences

def linear_search_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1  # moved return outside loop!

result2 = linear_search_all(numbers, target)
print(f"Method 2 (all occurrences): Element indices = {result2}")