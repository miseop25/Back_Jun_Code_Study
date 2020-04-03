def solution(begin, target, words):
    answer = 0
    if target not in words :
        return 0
    stack = []
    buf = [begin]
    while True :
        buf_list = []
        for k in buf:
            for i in range(len(begin)):
                temp = k[:i] + "_" + k[i+1:]
                buf_list.append(temp)
        buf = []
        for i in range(len(buf_list)) :
            for j in words :
                temp = j[:i] + "_" + j[i+1:]
                if buf_list[i] == temp :
                    if j not in stack :
                        if j == target :

                            return answer + 1
                        else : 
                            stack.append(j)
                            buf.append(j)
        answer += 1



    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"] ))