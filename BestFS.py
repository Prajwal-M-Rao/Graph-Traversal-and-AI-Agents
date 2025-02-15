import heapq

def greedy_best_first_search(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        # Pop the node with the minimum heuristic value
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            print(f"Goal {goal} reached!")
            break

        if current_node not in visited:
            print(f"Visiting node: {current_node}")

            # Mark the current node as visited
            visited.add(current_node)

            # Explore neighbors and enqueue them with their heuristic values
            for neighbor, cost in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost, neighbor))

    else:
        print(f"Goal {goal} not reachable from {start}")

# Example usage
weighted_graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 6)],
    'D': [('G', 7)],
    'E': [('G', 4)],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'

greedy_best_first_search(weighted_graph, start_node, goal_node)

