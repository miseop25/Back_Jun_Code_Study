import sys

read = lambda : sys.stdin.readline().strip()
write = lambda x: sys.stdout.write(str(x)+ "\n")

ans = []
for _ in range(int(read())):
    n, k, e, m = read().split()
    ans.append((n, int(k), int(e), int(m)))
ans=sorted(ans,key=lambda x: (-x[1],x[2],-x[3],x[0]))
# -를 줘서 그대로 하면된다.
for i in ans:
    print(i[0])