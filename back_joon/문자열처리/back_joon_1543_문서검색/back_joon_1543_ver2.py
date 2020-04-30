import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

p_len = len(p)
ans_list = []
if len(s) == 1 and p_len == 1:
    if s == p :
        ans_list.append(1)
for j in range(p_len) :
    answer = 0
    i = j
    while i < len(s) :
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