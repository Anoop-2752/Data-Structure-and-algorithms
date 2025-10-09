
# Find index with Binary search 
sorted_arr = [2,4,10,40,50,60]
target = 10

def binary_search(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

result = binary_search(sorted_arr, target)
print(f"Element {target} at index: {result}")
    


