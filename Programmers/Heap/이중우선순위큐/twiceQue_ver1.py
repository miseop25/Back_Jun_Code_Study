import collections

def solution(operations):
    answer = []
    que = collections.deque()
    for i in operations :
        check, num = i.split(" ")
        if check == "I" :
            que.append(int(num))
        else :
            if que :
                if num == "1" :
                    que.pop()
                else :
                    que.popleft()
        que = collections.deque(sorted(que))

    if len(que) >= 2 :
        answer.append(que.pop())
        answer.append(que.popleft())
    else :
        answer = [0,0]
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))