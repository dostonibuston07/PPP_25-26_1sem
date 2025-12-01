def shortest_path(adj, start, end):
    n = len(adj)
    visited = [False] * n
    log = []

    def dfs(v, dist, path):
        visited[v] = True
        path.append(v)
        log.append(("visit", v, dist, path.copy()))

        if v == end:
            visited[v] = False
            path.pop()
            return dist, path.copy()

        best = (float('inf'), None)

        for i, j in enumerate(adj[v]):
            if j > 0 and not visited[i]:
                log.append(("try", v, i, j, path.copy(), dist))
                d, p = dfs(i, dist + j, path)
                if d < best[0]:
                    best = (d, p)
                    log.append(("update_min", best))

        visited[v] = False
        path.pop()
        return best

    return (*dfs(start, 0, []), log)


# пример
adj = [
    [0, 3, 0, 7],
    [3, 0, 2, 0],
    [0, 2, 0, 1],
    [7, 0, 1, 0]
]

dist, path, log = shortest_path(adj, 0, 3)

print("distance:", dist)
print("path:", path)
print("\nlog:")
for l in log:
    print(l)
