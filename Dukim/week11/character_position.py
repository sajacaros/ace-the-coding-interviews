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
print('-'*20)
assert solution(["down", "down", "down", "down", "down"], [7, 9]) == [0, -4]
