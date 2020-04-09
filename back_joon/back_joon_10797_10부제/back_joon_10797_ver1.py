day = int(input())
cnt = 0
num_list = map(int, input().split(" "))
for i in num_list :
    if day == i :
        cnt += 1
print(cnt)
