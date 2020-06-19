def solution(p):
    if p == "" :
        return p
    answer = []
    left = []
    for i, var in enumerate(p) :
        if var == "(" :
            answer.append(var)
            left.append(i)
        else :
            if left :
                answer.append(")")
                left.pop()
            else :
                left.append(i)
                answer.append("(")
    if left :
        temp = len(left)//2
        for i in left[: temp] :
            answer[i + temp] = ")"
            temp -= 1




    return "".join(answer)

print(solution("()))((()"))