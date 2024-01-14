import heapq


def dijkstra(graph, start):
    print(f'{graph=}')
    print('-'*10)
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    paths = {start: [start]}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        print(f"visit : {current_node}, distance : {current_distance}, distance['{current_node}'] : {distances[current_node]}")
        if distances[current_node] < current_distance:
            print(f'reject node : {current_node}')
            continue
        # print(f'visit : {current_node}, distance : {current_distance}')
        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                print(f'distances : {distances}')
                paths[adjacent_node] = paths[current_node] + [adjacent_node]
                heapq.heappush(queue, [distance, adjacent_node])
    sorted_paths = {node: paths[node] for node in sorted(paths)}
    return [distances, sorted_paths]

if __name__=='__main__':

    graph = {
        'A': {'B': 9, 'C': 3},
        'B': {'A': 5},
        'C': {'B': 1}
    }
    graph = {
        'A': {'B': 12, 'C': 5, 'D':2},
        'B': {'A': 3, 'C': 5},
        'C': {'A': 4, 'B': 6, 'D': 1},
        'D': {'B': 3}
    }
    distances, paths = dijkstra(graph, 'A')
    print('-'*10)
    print(f'final distances : {distances}')
    print(f'best path : {paths}')