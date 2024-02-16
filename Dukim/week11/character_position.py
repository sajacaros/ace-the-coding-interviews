# https://school.programmers.co.kr/learn/courses/30/lessons/120861
from typing import Tuple


def check_boundary(board, position, move_pointer):
    boundary_x, boundary_y = board[0] // 2, board[1] // 2
    return (-boundary_x <= position[0] + move_pointer[0] <= boundary_x
            and -boundary_y <= position[1] + move_pointer[1] <= boundary_y)


def get_move_position(board, position, direction) -> Tuple[int, int]:
    key_pointer = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    if check_boundary(board, position, key_pointer[direction]):
        return key_pointer[direction]
    else:
        return 0, 0


def solution(keyinput, board):
    cur_position = [0, 0]

    for key in keyinput:
        move_pointer = get_move_position(board, cur_position, key)
        cur_position[0] += move_pointer[0]
        cur_position[1] += move_pointer[1]
    print(cur_position)
    return cur_position


assert solution(["left", "right", "up", "right", "right"], [11, 11]) == [2, 1]
print('-'*20)
assert solution(["down", "down", "down", "down", "down"], [7, 9]) == [0, -4]
