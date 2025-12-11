def shortest_path_recursive(adj, start, end):
    visited = set()           
    best_distance = [float('inf')]  
    best_path = [[]]          

    def dfs(current, path, distance):
        print(f"Шаг: сейчас в вершине {current}, путь: {path}, расстояние: {distance}")
        if current == end:
            print(f"  Нашли путь до {end}: {path}, длина = {distance}")
            if distance < best_distance[0]:
                best_distance[0] = distance
                best_path[0] = path.copy()
            return
        visited.add(current)
        for neighbor, weight in enumerate(adj[current]):
            if weight > 0 and neighbor not in visited:  
                print(f"  Пробуем перейти {current} → {neighbor} (вес {weight})")
                dfs(neighbor, path + [neighbor], distance + weight)
        visited.remove(current)
    dfs(start, [start], 0)
    print("\nИТОГ:")
    print("Кратчайший путь:", best_path[0])
    print("Длина пути:", best_distance[0])
    return best_path[0], best_distance[0]
# Пример таблицы смежности (граф)
#     0  1  2  3
graph = [
    [0, 5, 2, 0],   # 0 → 1 (5), 0 → 2 (2)
    [5, 0, 3, 4],   # 1 → 2 (3), 1 → 3 (4)
    [2, 3, 0, 6],
    [0, 4, 6, 0]
]
shortest_path_recursive(graph, 0, 3)
