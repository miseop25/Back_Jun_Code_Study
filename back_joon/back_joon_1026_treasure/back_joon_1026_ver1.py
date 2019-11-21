N = int(input())

A_list = list(map(int, input().split(' ')))
B_list = list(map(int, input().split(' ')))

A_list.sort()
B_list.sort(reverse=True)

S = 0

for i in range(N) :
    S += A_list[i]*B_list[i]
print(S)
