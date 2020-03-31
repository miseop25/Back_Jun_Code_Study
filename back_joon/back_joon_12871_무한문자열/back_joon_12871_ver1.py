import sys
input = sys.stdin.readline

s = input().split()
t = input().split()

s_len = len(s[0])
t_len = len(t[0])

if s_len < t_len :
    buf = t[0][:s_len]
    if buf == s[0] :
        print(1)
    else :
        print(0)
elif s_len > t_len :
    buf = s[0][:t_len]
    if buf == t[0]:
        print(1)
    else :
        print(0)
else :
    if s[0] == t[0] :
        print(1)
    else :
        print(0)
