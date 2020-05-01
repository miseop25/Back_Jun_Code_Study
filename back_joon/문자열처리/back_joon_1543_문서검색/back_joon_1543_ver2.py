import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()
p_len = len(p)

#  검색해서 나온 중복값을 담는다.
ans_list = []

#  찾고자 하는 문자열의 길이만큼만 이동해서 반복한다.
for j in range(p_len) :
    answer = 0
    i = j
    while i < len(s) :
        #  i + p_len 이 문자열 s 보다 길다면 마지막에 왔다는 의미이다. -> Else로
        if i + p_len < len(s) :
            if p == s[i : i + p_len] :
                answer += 1
                i += p_len
            else :
                i += 1
        else :
            if p == s[i :] :
                answer += 1
            break
        
    ans_list.append(answer)
print(max(ans_list))