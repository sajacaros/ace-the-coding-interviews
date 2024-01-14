# 11 그래프
## 11-1 그래프의 개념
* 그래프 용어 정리
  - 데이터를 담고 있는 노드
  - 노드를 잇는 간선
  - 간선의 방향
  - 간선의 가중치
* 그래프의 특징과 종류
  - 흐름을 표현하는 방향성
    - 방향 그래프
      - 방향이 있는 간선을 포함
    - 무방향 그래프
      - 방향이 없는 간선을 포함
  - 흐름의 정도를 표현하는 가중치
  - 시작과 끝의 연결 여부를 보는 순환
* 그래프 구현
  - 인접 행렬 그래프 표현
    - 배열을 활용해 구현
    - 장점
      - 시간 복잡도가 O(1)
    - 단점
      - 희소 그래프를 표현
    ```python
    matrix = [
      [0, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 0],
      [0, 0, 1, 0, 1, 1],
      [0, 1, 0, 1, 0, 1],
      [0, 0, 0, 1, 1, 0],
    ] 
    ```
  - 인접 리스트 그래프 표현
    - 값(v), 가중치(w), 다음 노드(next)를 묶어 관리
    - 장점
      - 메모리를 아낄 수 있음
    - 단점
      - O(N)
    ```python
    graph = {
      "A": ["B"],
      "B": ["A", "C", "E"],
      "C": ["B", "D"],
      "D": ["C", "E", "F"],
      "E": ["B", "D", "F"],
      "F": ["D", "E"],
    }
    ```
## 11-2 그래프 탐색
* 깊이 우선 탐색
  - 시작 노드부터 탐색을 시작하여 간선을 따라 최대 깊이 노드까지 이동하며 차례대로 방문
  - 스택과 재귀를 활용하여 구현 가능
* 너비 우선 탐색
  - 시작 노드와 거리가 가장 가까운 노드를 우선하여 방문 
  - 큐를 활용하여 구현 가능
* 깊이 우선 탐색과 너비 우선 탐색 비교
  - 깊이 우선 탐색
    - 모든 가능한 해를 찾는 백트래킹 알고리즘
    - 그래프의 사이클 감지해야 하는 가능
  - 너비 우선 탐색
    - 최단 경로 찾기 문제
## 11-3 그래프 최단 경로 구하기
* 다익스트라 알고리즘
  - 시작 지점과의 거리를 계산
  - distance table에는 이전 노드와 시작 지점과의 거리가 저장됨
  - 노드는 단 한번만 방문함
  - 노드를 한번만 방문하기에 음의 가중치를 갖을 경우 적용할 수 없음
  - 기본 준비
    - 모든 노드의 최소 비용을 무한대로 세팅
    - 시작 노드의 최소 비용을 0으로 세팅하고 이전노드를 자신으로 세팅
  - 구현
    - 방문한적 없는 노드 중 방문 할 수 있는 최소 비용의 노드를 방문
    - 해당 노드에서 방문할 수 있는 노드의 거리를 계산하고 기존보다 짧다면
    - distance table의 거리를 위 계산 값으로 갱신하고 이전 노드를 현재 노드로 세팅
    - 위 과정 반복  
* 벨만-포드 알고리즘
  - 다익스트라와 기본 로직은 동일함
  - 음의 가중치를 가지는 그래프에서도 최단 경로를 구할 수 있음
  - 매 단계마다 모든 간선의 가중치를 다시 확인하여 최소 비용 갱신
  - 위 작업을 N-1 회 진행
  - 마지막으로 1회 더 진행했을 때 갱신이 된다면 음의 순환이 있다고 판단
## 11-4 몸풀기 문제
* 깊이 우선 탐색 순회
```python
def dfs(graph, start_v):
    visited = []

    def dfs_inner(cur_v):
        visited.append(cur_v)
        for node in graph[cur_v]:
            if node not in visited:
                dfs_inner(node)

    dfs_inner(start_v)
    return visited
```
* 너비 우선 탐색 순회
```python
from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited
```
* 다익스트라 알고리즘
  - 소스 코드
  ```python 
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
  ```
  - 실행 결과
  ```
  graph={'A': {'B': 12, 'C': 5}, 'B': {'A': 3, 'C': 5}, 'C': {'A': 4, 'B': 6, 'D': 1}, 'D': {'B': 4}}
  ----------
  visit : A, distance : 0, distance['A'] : 0
  distances : {'A': 0, 'B': 12, 'C': inf, 'D': inf}
  distances : {'A': 0, 'B': 12, 'C': 5, 'D': inf}
  visit : C, distance : 5, distance['C'] : 5
  distances : {'A': 0, 'B': 11, 'C': 5, 'D': inf}
  distances : {'A': 0, 'B': 11, 'C': 5, 'D': 6}
  visit : D, distance : 6, distance['D'] : 6
  distances : {'A': 0, 'B': 10, 'C': 5, 'D': 6}
  visit : B, distance : 10, distance['B'] : 10
  visit : B, distance : 11, distance['B'] : 10
  reject node : B
  visit : B, distance : 12, distance['B'] : 10
  reject node : B
  ----------
  final distances : {'A': 0, 'B': 10, 'C': 5, 'D': 6}
  best path : {'A': ['A'], 'B': ['A', 'C', 'D', 'B'], 'C': ['A', 'C'], 'D': ['A', 'C', 'D']}
  ```
* 벨만-포드 알고리즘
```python
def bellman_ford(graph, source):
    num_vertices = len(graph)
    distance = [float('inf')] * num_vertices
    distance[source] = 0
    predecessor = [None] * num_vertices
    for temp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                distance[v] = distance[u] + weight
                predecessor[v] = u
    for u in range(num_vertices):
        for v , weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return [-1]
    return [distance, predecessor]
```

