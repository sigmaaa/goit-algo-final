import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    previous_vertices = {vertex: None for vertex in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices


def restore_path(vertices_map, looking_vertex):
    path = []
    while vertices_map.get(looking_vertex) is not None:
        path.append(looking_vertex)
        looking_vertex = vertices_map.get(looking_vertex)
    path.append(looking_vertex)
    path.reverse()
    return path


weight_transport_network = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "D": 2},
    "C": {"A": 3, "E": 5},
    "D": {"B": 2, "F": 1},
    "E": {"C": 5, "F": 6},
    "F": {"D": 1, "E": 6, "G": 2, "H": 2},
    "G": {"F": 2, "H": 2},
    "H": {"F": 2, "G": 2}
}

# Запуск алгоритму Дейкстри
distances, vertices = dijkstra(weight_transport_network, 'A')

print("Відстані від A:")
for vertex, distance in distances.items():
    print(f"Вершина {vertex}: відстань {distance}")

# Відновлення шляху до вершини D
for vertex in vertices:
    print(f"Найкоротший шлях до {vertex}")
    print(restore_path(vertices, vertex))
