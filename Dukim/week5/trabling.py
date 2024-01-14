def preorder(nodes, cur_idx, arr):
    if len(nodes)<=cur_idx:
        return
    cur_value = nodes[cur_idx]
    arr.append(cur_value)
    preorder(nodes, cur_idx*2+1, arr)
    preorder(nodes, cur_idx*2+2, arr)


def solution(nodes):
    arr = []
    preorder(nodes, 0, arr)
    return arr

print(solution([1,2,3,4,5,6,7]))
# inorder(nodes), postorder(nodes)
# assert solution([1,2,3,4,5,6,7]) == ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]