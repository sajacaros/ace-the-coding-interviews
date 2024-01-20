import copy
from collections import defaultdict


def dfs(graph, start_v):
    visited = []

    def dfs_inner(cur_v):
        visited.append(cur_v)
        for node in graph[cur_v]:
            if node not in visited:
                dfs_inner(node)

    dfs_inner(start_v)
    return len(visited)

def generate_graph(nodes):
    graph = defaultdict(list)
    for u, v in nodes:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def solution(n, wires_):
    print('wires : ', wires_)
    diff = float('inf')
    for remove_idx in range(0, len(wires_)):
        print(f'제거 : {wires_[remove_idx]}')
        wires = copy.deepcopy(wires_)
        wires.remove(wires_[remove_idx])
        connected_graph = generate_graph(wires)
        left_nodes = dfs(connected_graph, 1)
        right_nodes = n-left_nodes
        diff = min(diff, abs(left_nodes-right_nodes))
        print(f'graph : {list(connected_graph.items())}')
        print(f'노드 개수 : {left_nodes}, diff : {diff}\n')
    print('-' * 20)
    return diff

assert solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])==3
assert solution(4, [[1,2],[2,3],[3,4]])==0
assert solution(7, [[1,2],[2,7],[3,7],[4,5],[6,7]])==1