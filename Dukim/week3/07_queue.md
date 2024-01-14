# 07 큐
## 07-1 큐의 개념
* 선입선출(FIFO; First In First Out)
## 07-2 큐의 정의
* 큐의 특성을 활용하는 분야
  - 작업 대기열
  - 이벤트 처리
* 큐의 ADT
  - 연산
    - boolean isFull()
      - 큐에 들어있는 데이터 개수가 maxsize인지 확인해 boolean값 리턴
    - boolean isEmpty()
      - 데이터가 하나라도 있으면 False, 아니면 True
    - void push(ItemType item)
      - 큐에 데이터를 푸시
    - ItemType pop()
      - 처음에 푸시한 데이터를 팝하고 그 데이터를 반환
  - 상태
    - Int front
      - 큐에서 가장 마지막에 팝한 위치를 기록
    - Int rear
      - 큐에서 최근에 푸시한 데이터의 위치를 기록
    - ItemType data[maxsize]
      - 큐의 데이터를 관리하는 배열, 최대 maxsize개의 데이터를 관리
* 큐 구현
  - 덱을 큐처럼 활용
  ``` python 
  from collections import deque
  queue = deque()
  # 큐에 데이터 추가
  queue.append(1)
  queue.append(2)
  queue.append(3)
  # 큐의 맨 앞 데이터 제거
  first_item = queue.popleft()
  print(first_item) # 1
  # 큐에 데이터 추가
  queue.append(4)
  queue.append(5)
  # 큐의 맨 앞 데이터 제거
  first_item = queue.popleft()
  print(first_item) # 2
  ```
* pop(0)와 popleft()의 성능 비교
  - pop(0)는 O(n)의 시간복잡도를 가짐
  - popleft()는 O(1)의 시간복잡도를 가짐
  - popleft()가 압도적으로 빠름