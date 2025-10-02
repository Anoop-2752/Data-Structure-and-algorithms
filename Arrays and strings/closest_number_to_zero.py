"""
Leetcode: 2239

Find the closest number to zero
"""


def find_closest_number(nums):
    closest = nums[0]

    for x in nums:
        if abs(x) < abs(closest):
            closest = x

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


nums = [-4, -2, 1, 4, 8]
result = find_closest_number(nums)
print(result)

# Time complexity: O(n) looping twice through the list of n elements
# Space complexity: O(1) no extra space used
