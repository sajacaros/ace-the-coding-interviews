def get_next_position(position, d):
    direction_map = { 'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0) }
    min_pos, max_pos, dir_ = -5, 5, direction_map[d]
    if min_pos <= position[0]+dir_[0] <= max_pos and min_pos <= position[1]+dir_[1] <= max_pos:
        return position[0]+dir_[0], position[1]+dir_[1]
    else:
        return position


def solution(dirs):
    position_history = set()
    prev_position = (0, 0)
    for d in dirs:
        next_position = get_next_position(prev_position, d)
        if prev_position != next_position:
            position_history.add( (prev_position,next_position) )
            position_history.add( (next_position,prev_position) )
        prev_position = next_position
    return int(len(position_history)/2)
