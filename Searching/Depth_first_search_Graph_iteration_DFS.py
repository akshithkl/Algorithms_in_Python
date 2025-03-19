def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))  # Reverse to maintain order

# Example Graph
print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 'A')  # Output: A C F E B D


# 2. DFS for Trees (Recursive & Iterative)

# Time Complexity
# O(N) where N is the number of nodes in the tree
# Every node is visited exactly once.
# Space Complexity
# Recursive DFS:

# O(H) where H is the height of the tree
# Worst case for a skewed tree: O(N)
# Balanced tree: O(log N)
# Iterative DFS:

# O(H) due to stack usage (same as recursion)