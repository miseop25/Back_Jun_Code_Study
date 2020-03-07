import sys
input = sys.stdin.readline

N , M = map(int, input().split(" "))

num = []
for i in range(1, N+1) :
    num.append(i)

for _ in range(M) :
    i, j, k = map(int , input().split(" "))
    first = []
    end = []
    first = num[k-1 : j]
    end = num[i-1 :k-1]
    first.extend(end)
    num[i-1:j] = first

print(" ".join(map(str, num)))
print(num)

