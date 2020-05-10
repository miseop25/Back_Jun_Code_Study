import sys
input = sys.stdin.readline

s = input().split()
t = input().split()

s_len = len(s[0])
t_len = len(t[0])
answer = 0
if s_len != t_len :
    buf_s = s[0]*t_len
    buf_t = t[0]*s_len
    if buf_t == buf_s :
        answer = 1
else :
    if s[0] == t[0] :
        answer = 1

print(answer)