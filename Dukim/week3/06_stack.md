# 06 스택
## 06-1 스택 개념
* 선입후출(FILO; First In Last Out)
## 06-2 스택의 정의
* 스택의 ADT
  - 연산
    - boolean isFull()
      - 스택이 가득차 있으면 True, 아니면 False
    - boolean isEmpty()
      - 데이터가 하나라도 있으면 False, 아니면 True
    - void push(ItemType item)
      - 스택에 데이터를 푸시
    - ItemType pop()
      - 최근에 푸시한 데이터를 팝하고 그 데이터를 반환
  - 상태
    - Int top
      - 스택에서 최근에 푸시한 데이터의 위치
    - ItemType data[maxsize]
      - 스택의 데이터를 관리하는 배열, 최대 maxsize개의 데이터를 관리
* 스택 구현
  - 파이썬은 리스트의 크기를 동적을 관리
  ``` python 
  stack = []
  # 데이터 추가
  stack.append(1)
  stack.append(2) 
  stack.append(3)
  # 데이터 추출
  top_element = stack.pop()
  next_element = stack.pop()
  # 스택 크기
  stack_size = len(stack)
  print(top_element, next_element)
  ```