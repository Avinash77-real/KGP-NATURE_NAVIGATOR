import heapq

def find_path(graph, start, end, mode='shortest'):
    """
    Implementation of Dijkstra's Algorithm with a custom cost function for scenic mode.
    'shortest': minimizes physical distance.
    'scenic': balances distance with a greenery index.
    """
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        (current_cost, current_node, path) = heapq.heappop(queue)

        if current_node in visited: continue
        path = path + [current_node]
        visited.add(current_node)

        if current_node == end: return current_cost, path
        if current_node not in graph: continue

        for neighbor, data in graph[current_node].items():
            dist = data['dist']
            greenery = data['greenery']
            
            # Custom weight logic: Scenic mode reduces 'cost' based on greenery
            weight = dist / (1 + (greenery * 0.2)) if mode == 'scenic' else dist
                
            if neighbor not in visited:
                heapq.heappush(queue, (current_cost + weight, neighbor, path))
    return float("inf"), []

# IIT Kharagpur Adjacency List (Distances in meters, Greenery scale 1-10)
kgp_graph = {
    'Main Building': {
        'Vikramshila': {'dist': 500, 'greenery': 5},
        'Library': {'dist': 150, 'greenery': 3},
        'Pan Loop': {'dist': 1500, 'greenery': 9}
    },
    'Vikramshila': {
        'Main Building': {'dist': 500, 'greenery': 5},
        'Nalanda': {'dist': 200, 'greenery': 4}
    },
    'Nalanda': {
        'Vikramshila': {'dist': 200, 'greenery': 4},
        'LBS Hall': {'dist': 2200, 'greenery': 7}
    },
    'LBS Hall': {
        'Nalanda': {'dist': 2200, 'greenery': 7},
        'Pan Loop': {'dist': 600, 'greenery': 4}
    },
    'Pan Loop': {
        'LBS Hall': {'dist': 600, 'greenery': 4},
        'Main Building': {'dist': 1500, 'greenery': 9}
    }
}

if __name__ == "__main__":
    print("--- IIT Kharagpur Nature Navigator ---")
    start = input("Enter Start: ")
    end = input("Enter Destination: ")
    cost, path = find_path(kgp_graph, start, end, mode='scenic')
    print(f"Path: {' -> '.join(path)}")
