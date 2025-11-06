"""
Common Algorithmic Patterns
A comprehensive guide to frequently used algorithm patterns
"""

# 1. TWO POINTERS PATTERN
def two_pointers_example(arr, target):
    """Find pair that sums to target in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# 2. SLIDING WINDOW PATTERN
def sliding_window_max_sum(arr, k):
    """Find maximum sum of k consecutive elements"""
    if len(arr) < k:
        return None
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# 3. FAST & SLOW POINTERS (Floyd's Cycle Detection)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """Detect cycle in linked list"""
    if not head:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 4. BINARY SEARCH PATTERN
def binary_search(arr, target):
    """Standard binary search"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 5. BACKTRACKING PATTERN
def permutations(nums):
    """Generate all permutations"""
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    
    backtrack([], nums)
    return result

# 6. DYNAMIC PROGRAMMING PATTERN
def fibonacci_dp(n):
    """Fibonacci using dynamic programming"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# 7. BFS PATTERN (Level Order Traversal)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """BFS level order traversal"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# 8. DFS PATTERN (Recursion)
def dfs_traversal(root):
    """DFS inorder traversal"""
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result

# 9. MERGE INTERVALS PATTERN
def merge_intervals(intervals):
    """Merge overlapping intervals"""
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    
    return merged

# 10. PREFIX SUM PATTERN
def prefix_sum_range_query(arr):
    """Build prefix sum array for range queries"""
    n = len(arr)
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    def range_sum(left, right):
        return prefix[right + 1] - prefix[left]
    
    return prefix, range_sum

# 11. MONOTONIC STACK PATTERN
def next_greater_element(arr):
    """Find next greater element for each element"""
    result = [-1] * len(arr)
    stack = []
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    
    return result

# 12. UNION-FIND (Disjoint Set) PATTERN
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

# DEMONSTRATION
if __name__ == "__main__":
    print("=" * 60)
    print("ALGORITHMIC PATTERNS DEMONSTRATION")
    print("=" * 60)
    
    # Two Pointers
    print("\n1. TWO POINTERS:")
    arr = [1, 2, 3, 4, 5, 6]
    print(f"   Array: {arr}, Target: 9")
    print(f"   Pair: {two_pointers_example(arr, 9)}")
    
    # Sliding Window
    print("\n2. SLIDING WINDOW:")
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 3
    print(f"   Array: {arr}, Window size: {k}")
    print(f"   Max sum: {sliding_window_max_sum(arr, k)}")
    
    # Binary Search
    print("\n3. BINARY SEARCH:")
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    print(f"   Array: {arr}, Target: {target}")
    print(f"   Index: {binary_search(arr, target)}")
    
    # Backtracking
    print("\n4. BACKTRACKING:")
    nums = [1, 2, 3]
    print(f"   Array: {nums}")
    print(f"   Permutations: {permutations(nums)}")
    
    # Dynamic Programming
    print("\n5. DYNAMIC PROGRAMMING:")
    n = 10
    print(f"   Fibonacci({n}): {fibonacci_dp(n)}")
    
    # Prefix Sum
    print("\n6. PREFIX SUM:")
    arr = [1, 2, 3, 4, 5]
    prefix, range_sum = prefix_sum_range_query(arr)
    print(f"   Array: {arr}")
    print(f"   Prefix: {prefix}")
    print(f"   Range sum [1-3]: {range_sum(1, 3)}")
    
    # Monotonic Stack
    print("\n7. MONOTONIC STACK:")
    arr = [4, 5, 2, 10, 8]
    print(f"   Array: {arr}")
    print(f"   Next greater: {next_greater_element(arr)}")
    
    print("\n" + "=" * 60)