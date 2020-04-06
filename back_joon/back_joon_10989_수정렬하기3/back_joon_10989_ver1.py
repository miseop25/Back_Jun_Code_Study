import sys
input = sys.stdin.readline
num_str = ""
N = int(input())
for _ in range(N) :
    buf = input()
    buf = buf[ :-1]
    num_str += buf

for i in sorted(num_str) :
    sys.stdout.writelines(i)
    sys.stdout.writelines("\n")
