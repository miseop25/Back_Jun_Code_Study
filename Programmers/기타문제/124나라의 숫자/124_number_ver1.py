import collections
def solution(n):
    answer = ''
    num = ["4", "1", "2"]
    buf = collections.deque([])
    val, leave = divmod(n, 3)

    buf.append(num[leave])
    while val > 0 and n != 3:
        if leave == 0 :
            val -= 1
        new_val , new_leave = divmod(val, 3)
        if val == 0 :
            break
        buf.append(num[new_leave])
        val = new_val
        leave = new_leave
    while buf :
        answer += buf.pop()
    return answer

a = int(input())
print(solution(a))