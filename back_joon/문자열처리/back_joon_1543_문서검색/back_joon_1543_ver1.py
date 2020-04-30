import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()
answer = 0
i = 0
p_len = len(p)
if len(s) == 1 and p_len == 1:
    if s == p :
        answer += 1
while i + len(p) < len(s) :
    if p == s[i : i + p_len] :
        answer += 1
        i += p_len
    else :
        i += 1
print(answer)