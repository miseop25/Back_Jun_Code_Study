def chechRightWord(word) :
    stack = []
    for i in word :
        if i == "(" :
            stack.append(i)
        else : 
            if stack :
                stack.pop()
            else :
                return False
    if stack :
        return False
    return True

def divdeUV(word) :
    left = 0
    right = 0
    for i in range(len(word)) :
        if left != 0 and right != 0 and left == right :
            u = word[:i]
            v = word[i:]
            return u, v
        if word[i] == "(" :
            left += 1
        else :
            right += 1
    u = word
    v = ''
    return u, v

def reverseBracket(word) :
    result = ''
    for i in word :
        if i == "(" :
            result += ")"
        else :
            result += "("
    return result

def makeBalanceWord(word) :
    result = ''
    if word == "" :
        return word
    u, v = divdeUV(word)
    if chechRightWord(u) :
        result = u + makeBalanceWord(v)
    else :
        temp = "(" + makeBalanceWord(v) + ")"
        buf = u[1:-1]
        buf = reverseBracket(buf)
        result = temp + buf
    return result

def solution(p):
    answer = ''
    answer = makeBalanceWord(p)
    return answer


print(solution("()))((()"))