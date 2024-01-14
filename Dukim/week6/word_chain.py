# https://school.programmers.co.kr/learn/courses/30/lessons/12981

# 3 ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
# 5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
# 2	["hello", "one", "even", "never", "now", "world", "draw"]	[1,3]


def solution(n, words):
    answer = [0, 0]
    word_set = set()
    prev_last_char = None
    for idx, word in enumerate(words):
        is_invalid_chain = prev_last_char and prev_last_char != word[0]
        is_duplicated = word in word_set
        if is_invalid_chain or is_duplicated:
            answer = [idx%n+1, idx//n+1]
            return answer

        prev_last_char = word[-1]
        word_set.add(word)

    return answer

def solution2(n, words):
    answer = [0, 0]
    word_set = set()
    prev_last_char = words[0][0]
    for idx, word in enumerate(words):
        if prev_last_char != word[0] or word in word_set:
            answer = [idx%n+1, idx//n+1]
            return answer

        prev_last_char = word[-1]
        word_set.add(word)

    return answer

assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3,3]
assert solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0,0]
assert solution(2,	["hello", "one", "even", "never", "now", "world", "draw"]) == [1,3]