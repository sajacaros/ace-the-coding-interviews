# 14 시뮬레이션
* 시뮬레이션이란?
- 문제에 주어진 상황을 완벽하게 이해하고 이를 코드로 구현하는 과정
* 시뮬레이션 문제를 푸는 방법
- 하나의 문제를 최대한 여러개로 분리
- 예외처리가 필요하다면 독립 함수로 구현
* 행렬 연산
- 행렬 덧셈과 뺄셈
  - 각 행렬에서 같은 위치에 있는 값끼리 더하거나 빼는 연산
  - 행과 열의 크기가 같아야 함
- 행렬 곱셈
  - 곱셈의 순서가 중요
  - AxB의 경우 A행렬의 열 크기가 B행렬의 행 크기와 같아야 함
  - 최종 결과 = (A행렬의 행 크기, B행렬의 열 크기)
- 전치 행렬
  - 행과 열 위치를 바꾸는 연산
- 좌표 연산을 좌표 배열로 표현
  - ex) `(3,4)위치 => arr[3][4] = 1`
- 좌표 이동 - 오프셋 활용
  ```
  왼쪽 위 위치 : arr[curr_y-1][curr_x-1]
  ...
  오른쪽 아래 위치 : arr[curr_y+1][curr_x+1]
  ```
- 좌표 이동 - 오프셋 배열 활용
  ```
  dy = [0, -1, -1, -1, 0, 0, 1, 1, 1]
  dx = [0, -1, 0, 1, -1, 1, -1, 0, 1]
  for i in range(1, 9):
    arr[curr_y+dy[i]][curr_x+dx[i]]
  ```
- 좌표 이동 - 90도 회전
  ``` 
   A[i][j]  => A[j][(N-1)-i]
     0 1 2         0 1 2
  0  1 2 3      0  3 5 8
  1  4 0 5  =>  1  2 0 7
  2  6 7 8      2  1 4 6
  ```
* practice - 캐릭터의 좌표
``` 
# https://school.programmers.co.kr/learn/courses/30/lessons/120861
def check_boundary(board, position, move_pointer):
    boundary_x, boundary_y = board[0] // 2, board[1] // 2
    return (-boundary_x <= position[0] + move_pointer[0] <= boundary_x
            and -boundary_y <= position[1] + move_pointer[1] <= boundary_y)


def solution(keyinput, board):
    cur_position = [0, 0]
    key_pointer = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}

    for key in keyinput:
        if check_boundary(board, cur_position, key_pointer[key]):
            cur_position[0] += key_pointer[key][0]
            cur_position[1] += key_pointer[key][1]
    print(cur_position)
    return cur_position


assert solution(["left", "right", "up", "right", "right"], [11, 11]) == [2, 1]
assert solution(["down", "down", "down", "down", "down"], [7, 9]) == [0, -4]
```