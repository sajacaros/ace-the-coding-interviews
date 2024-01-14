# ["Enter uid1234 Muzi","Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
def solution(record):
    answer = []
    nickname = {}
    for r in record:
        s = r.split(' ')
        if s[0] == 'Enter' or s[0] == 'Change':
            nickname[s[1]] = s[2]
    for r in record:
        s = r.split(' ')
        if s[0] == 'Enter':
            answer.append(f'{nickname[s[1]]}님이 들어왔습니다.')
        elif s[0] == 'Leave':
            answer.append(f'{nickname[s[1]]}님이 나갔습니다.')
    return answer
