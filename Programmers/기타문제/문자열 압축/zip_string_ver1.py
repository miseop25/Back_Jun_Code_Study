def solution(s):
    answer = 0
    ans_list = [len(s)]

    for w in range(1, len(s)//2 + 1) :
        temp = s[:w]
        cnt = 1
        buf = ""
        for i in range(w, len(s) , w) :
            if temp == s[i:i+w] :
                cnt += 1
            else :
                if cnt != 1 :
                    buf += str(cnt) + temp
                    cnt = 1
                else :
                    buf += s[i:i+w]
                temp = s[i:i+w]
        print(buf)
        if len(buf) != 0 :
            ans_list.append(len(buf))
    answer = min(ans_list)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
