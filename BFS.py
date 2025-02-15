from collections import deque


def bfs(graph, start):
    # Initialize the queue and visited set.
    queue = deque([start])
    visited = set([start])

    # Initialize the distances and parents dictionaries.
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    parents = {vertex: None for vertex in graph}

    # While the queue is not empty, perform the search.
    while queue:
        # Dequeue the first vertex from the queue.
        current_vertex = queue.popleft()

        # For each adjacent vertex, if it has not been visited, add it to the queue and update its distance and parent.
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited:
                queue.append(adjacent_vertex)
                visited.add(adjacent_vertex)
                distances[adjacent_vertex] = distances[current_vertex] + 1
                parents[adjacent_vertex] = current_vertex

    # Return the distances and parents dictionaries.
    return distances, parents


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

distances, parents = bfs(graph, 'A')

# Print the distances and parents
print("Distances:", distances)
print("Parents:", parents)
