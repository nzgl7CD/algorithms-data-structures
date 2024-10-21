'''
Given a weighted graph and a source vertex in the graph, find the shortest paths from the source to all the other vertices in the given graph.

Note: The given graph does not contain any negative edge.
'''
import heapq

# Space Complexity: O(V+E) space for the adjacency list, which is more space-efficient, especially for sparse graphs.
# Time complexity: O((V+E)logV)

def dijkstra(graph, start):
    # Create a priority queue to store (distance, vertex) pairs
    queue = []
    # Initialize distances with infinity
    distances = {vertex: float('infinity') for vertex in graph}
    # Set the distance to the start vertex to zero
    distances[start] = 0
    # Add the start vertex to the queue
    heapq.heappush(queue, (0, start))

    while queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(queue)

        # Nodes can only be processed once they are extracted from the priority queue
        if current_distance > distances[current_vertex]:
            continue

        # Check the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If the calculated distance is less than the known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Define a graph as a dictionary
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)

    print(f"Shortest paths from {start_vertex}: {shortest_paths}")
